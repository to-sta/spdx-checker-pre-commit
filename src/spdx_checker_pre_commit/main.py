from __future__ import annotations

from argparse import ArgumentParser
from typing import Sequence
from spdx_checker import spdx_checker


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
        "-l", "--license", type=str, help="SPDX license identifier to check for."
    )
    parser.add_argument(
        "filenames",
        type=str,
        nargs="*",
        help="List of files to check for SPDX license identifiers.",
    )

    args = parser.parse_args(argv)

    if not args.license or not args.filenames:
        parser.print_help()
        raise ValueError("License and filenames are required arguments.")

    spdx_checker.spdx_license_checker(args.license, args.filenames)


if __name__ == "__main__":
    raise SystemExit(main())
