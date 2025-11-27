# MLFlow Template with Poetry

This is a template repo that contains a barebones structure for machine learning projects using MLFlow for experiment tracking and poetry for package management

# External dependencies

Install `direnv` to load initial configuration environmental variables

# Installation

1. Clone the repo
2. Copy the dist.envr into .env with `cp dist.envrc .envrc`
3. Execute `direnv allow` to load .envrc variables
4. Change the project name in pyproject.toml
5. Run `poetry install` to get the base dependencies (if the preivous step is done, then it also initializes a virtual environment in the repo)
6. Run the mlflow server with `docker-compose up -d` in the root directory. This will create a postgress database as the backend for cleaner storage of experiments.

# TODO

- Create some sort of poetry scripts?
