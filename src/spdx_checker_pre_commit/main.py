# SPDX-License-Identifier: MIT
from __future__ import annotations

from argparse import ArgumentParser
from typing import Sequence
import spdx_checker


def main(argv: Sequence[str] | None = None) -> None:
    """
    Main function to parse command line arguments and pass them to the zig complied SPDX license checker.

    Parameters:
    -----------
        args (Sequence[str] | None): Command line arguments. If None, uses sys.argv.

    Returns:
    --------
        None

    Raises:
        SystemExit: If the arguments are not valid or if the license is not found.
    """
    parser = ArgumentParser()
    parser.add_argument(
        "-l",
        "--license",
        type=str,
        required=True,
        help="SPDX license identifier to check for.",
    )
    parser.add_argument(
        "filenames",
        type=str,
        nargs="+",
        help="List of files to check for SPDX license identifiers.",
    )
    parser.add_argument(
        "-f",
        "--fix",
        action="store_true",
        help="Add SPDX license identifier to files missing it.",
    )
    parser.add_argument(
        "-c",
        "--continue-on-error",
        action="store_true",
        help="Continue checking files even if an error occurs.",
    )

    args = parser.parse_args(argv)

    try:
        spdx_checker.check_license(
            args.license,
            args.filenames,
            fix=args.fix,
            continue_on_error=args.continue_on_error,
        )
    except ValueError:
        raise SystemExit(1)


if __name__ == "__main__":
    raise SystemExit(main())
