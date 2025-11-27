# MLFlow Template with Poetry

This is a template repo that contains a barebones structure for machine learning projects using MLFlow for experiment tracking and poetry for package management

# External Dependencies

- [Poetry](https://python-poetry.org/) - Package management
- [direnv](https://direnv.net/) - Environment variable loading
- [Docker](https://www.docker.com/) - MLFlow server

# Installation

1. Clone the repo
2. Run `./init.sh` and enter your project name (snake_case) to rename the package
3. Copy env template: `cp dist.envrc .envrc`
4. Load environment: `direnv allow`
5. Install dependencies: `poetry install`
6. Start MLFlow server: `docker-compose up -d`

# Development

```bash
ruff check src/    # Lint code
ruff format src/   # Format code
ty check src/      # Type check
pytest             # Run tests
```
