import csv
import os

import datasets


_DESCRIPTION = "My example dataset"

_HOMEPAGE = "https://github.com/jvictorfranca/repo_name"

_LICENSE = "MIT"

_CITATION = ""


class MeuDataset(datasets.GeneratorBasedBuilder):

    VERSION = datasets.Version("1.0.0")

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "text": datasets.Value("string"),
                    "label": datasets.Value("string"),
                }
            ),
            homepage=_HOMEPAGE,
            license=_LICENSE,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        data_dir = os.path.dirname(__file__)

        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                gen_kwargs={
                    "filepath": os.path.join(data_dir, "train.csv"),
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.VALIDATION,
                gen_kwargs={
                    "filepath": os.path.join(data_dir, "validation.csv"),
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                gen_kwargs={
                    "filepath": os.path.join(data_dir, "test.csv"),
                },
            ),
        ]

    def _generate_examples(self, filepath):
        with open(filepath, encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for idx, row in enumerate(reader):
                yield idx, {
                    "text": row["text"],
                    "label": row["label"],
                }