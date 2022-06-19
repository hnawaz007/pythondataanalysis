import setuptools

setuptools.setup(
    name="etl",
    packages=setuptools.find_packages(exclude=["etl_tests"]),
    install_requires=[
        "dagster==0.15.0",
        "dagit==0.15.0",
        "pytest",
    ],
)
