from setuptools import setup, find_packages

setup(
    # Package name used when installing with pip
    name="jformat",

    # Current package version
    version="0.0.1",

    # Short package description
    description="Reformats files to stdout",

    # Dependencies that will be installed automatically
    # when the package is installed via:
    #
    #     pip install jformat
    #
    # If any dependency is not available in the environment,
    # pip will download and install it.
    install_requires=[
        "click",      # Command-line interface creation
        "colorama",   # Cross-platform terminal colors
    ],

    # Creates executable commands available from the terminal.
    #
    # Format:
    #
    #     command_name=module:function
    #
    # When the user runs:
    #
    #     jformat file.json
    #
    # Python will execute:
    #
    #     jformat.main.main()
    #
    entry_points="""
    [console_scripts]
    jformat=jformat.main:main
    """,

    # Package author information
    author="Joao Franca",
    author_email="jvictorfranca@yahoo.com.br",

    # Automatically discover all Python packages
    # (directories containing __init__.py)
    packages=find_packages(),
)