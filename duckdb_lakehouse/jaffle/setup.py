from setuptools import find_packages, setup

setup(
    name="jaffle",
    packages=find_packages(exclude=["jaffle_tests"]),
    install_requires=[
        "dagster",
            "pandas",
            "duckdb",
            "sqlescapy",
            "html5lib",
            "lxml",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest", "localstack", "awscli", "awscli-local"]},
)
