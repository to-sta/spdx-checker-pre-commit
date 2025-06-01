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
    - repo: https://github.com/to-sta/spdx-checker-pre-commit
        rev: v0.1.1 # Add the most recent version here
        hooks:
        - id: spdx-license-checker
            name: spdx-license-checker
            args: [-l, AGPL-3.0-or-later]
            types_or: [python, ts, javascript, vue, css, html]
    ```

3. **Install the hook:**

    ```bash
    pre-commit install
    ```


## Requirements

- Python >=3.11 for Linux and MacOS
- Python >=3.13 for Windows
- [`spdx-checker`](https://pypi.org/project/spdx-checker/)

## License

[MIT](LICENSE)