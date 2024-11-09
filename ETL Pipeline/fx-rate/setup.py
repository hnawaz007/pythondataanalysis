from setuptools import find_packages, setup

setup(
    name="fx_rate",
    packages=find_packages(exclude=["fx_rate_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
