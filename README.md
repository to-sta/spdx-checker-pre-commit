# SPDX License Checker Pre-commit Hook

This repository provides a [pre-commit](https://pre-commit.com/) hook for validating and analyzing SPDX license headers in your codebase using the [`spdx-checker`](https://pypi.org/project/spdx-checker/) Python package.

## Features

- Fast SPDX license header validation for source files
- Integrates seamlessly with [pre-commit](https://pre-commit.com/)
- Helps ensure license compliance across your project

## Usage

1. **Install pre-commit** (if not already):

    ```bash
    pip install pre-commit
    ```

2. **Add the hook to your `.pre-commit-config.yaml`:**

    ```yaml
    - repo: https://github.com/your-org/spdx-checker-pre-commit
      rev: v0.1.0  # Use the latest tag or commit
      hooks:
         - id: spdx-checker
    ```

3. **Install the hook:**

    ```bash
    pre-commit install
    ```

4. **Run on all files:**

    ```bash
    pre-commit run --all-files
    ```

## Requirements

- Python 3.13+
- [`spdx-checker`](https://pypi.org/project/spdx-checker/)

## License

[MIT](LICENSE)