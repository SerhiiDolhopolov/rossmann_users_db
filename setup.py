from setuptools import setup, find_packages

setup(
    name="rossmann_users_db",
    version="0.1",
    packages=find_packages(include=[
        "users_db_models",
        "users_db_models.*"
    ]),
    install_requires=[
        "sqlalchemy"
    ]
)