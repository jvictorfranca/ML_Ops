import mlflow
import pandas as pd

logged_model = 'runs:/6ffba672db3c43f589903ff18e06f74e/model'


# Predict with Spark UDF

loaded_model = mlflow.pyfunc.spark_udf(
    spark,
    model_uri=logged_model,
    result_type='double'
)

columns = list(df.columns)
df.withColumn('predictions', loaded_model(*columns)).collect()


# Predict with pandas

loaded_model = mlflow.pyfunc.load_model(logged_model)

predictions = loaded_model.predict(pd.DataFrame(data))

print(predictions)