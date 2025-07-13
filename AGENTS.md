# Repository Guidelines

- Run `pytest -q` before committing changes to verify unit tests.
- If tests fail due to missing dependencies, install them with `pip install -r requirements-dev.txt`.
- The CI workflows build firmware from the `dev` branch by default, so ensure pull requests target `dev` unless otherwise noted.

