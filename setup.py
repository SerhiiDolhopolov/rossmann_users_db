from setuptools import setup, find_packages

setup(
    name="rossmann_users_db",
    version="0.2",
    packages=find_packages(include=[
        "rossmann_users_db_models",
        "rossmann_users_db_models.*"
    ]),
    install_requires=[
        "sqlalchemy"
    ]
)