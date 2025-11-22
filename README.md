# MLFlow Template with Poetry

This is a template repo that contains a barebones structure for machine learning projects using MLFlow for experiment tracking and poetry for package management

# Installation

1. Clone the repo
2. Change the project name in pyproject.toml
3. Copy the dist.env into .env with `cp dist.env .evn`
4. Run `poetry install` to get the base dependencies (if the preivous step is done, then it also initializes a virtual environment in the repo)
5. Use mlflow ui with `mlflow ui`

# TODO

- Add docker compose for easy mlflow setup
- Create some sort of poetry scripts?
