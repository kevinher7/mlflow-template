# MLFlow Template with Poetry

This is a template repo that contains a barebones structure for machine learning projects using MLFlow for experiment tracking and poetry for package management

# External Dependencies

- [Poetry](https://python-poetry.org/) - Package management
- [direnv](https://direnv.net/) - Environment variable loading
- [Docker](https://www.docker.com/) - MLFlow server

# Installation

1. Clone the repo with `git clone --depth 1`. If necessay remove the .git folder and `git init` again to have a clean history.
2. Run `./init.sh` and enter your project name (snake_case) to rename the package, create initial commit and remove origin. You may need to give it executable permissions with `chmod +x init.sh`
3. Copy env template: `cp .dist.envrc .envrc`
4. Load environment: `direnv allow`
5. Install dependencies: `poetry install`
6. This will create a python environment in the project root directory, activate it with `source .venv/bin/activate` for unix systems. Additionally check your IDE chooses this as the `Selected Interpreter`
7. Setup pre-commit hooks (mostly auto formatting, useful when vibe coding): `pre-commit install`
8. Start MLFlow server: `docker-compose up -d`
9. Run the test script via `poetry run demo`

Once this is done you can visit `localhost:5000` to see the default experiment with the demo run.

# Development

```bash
make lint       # Lint and fix code
make format     # Format code
make typecheck  # Type check
make test       # Run tests
make all        # Run all checks
```

Or run tools directly:

```bash
ruff check src/    # Lint code
ruff format src/   # Format code
ty check src/      # Type check
pytest             # Run tests
```

# Project Structure

```
src/
  project_name/
    __init__.py
    train.py       # Sample MLFlow training script
tests/
data/
  raw/             # Raw data (gitignored by default)
  processed/       # Processed data (gitignored by default)
notebooks/
```

# License

MIT License - see [LICENSE](LICENSE) for details.
