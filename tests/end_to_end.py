# Copyright (C) 2026 Henrik Wilhelmsen.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at <https://mozilla.org/MPL/2.0/>.

"""Simple CLI to run end-to-end tests for a given --package and --command arg.

Usage: `uv run ./tests/end_to_end.py --package mayaex-2026 --command mayapy2026`

Can be used in CI with a matrix to test multiple packages.
"""

import argparse
import logging
import subprocess
import sys
from pathlib import Path

PACKAGES_DIR = (Path(__file__).parent.parent / "packages").resolve()

logger = logging.getLogger(__name__)
logging.basicConfig(
    level="DEBUG",
    format="%(levelname)s: %(message)s",
)


def main() -> None:
    """Run an end-to-end test for the given --package and --command args with uvx."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--package")
    parser.add_argument("--command")
    args = parser.parse_args()
    # The argument passed to the DCC to test
    dcc_arg = (
        "--version" if "mayapy" in args.command or "mobupy" in args.command else "-v"
    )

    # Run the test
    ret_code = subprocess.call(  # noqa: S603
        [  # noqa: S607
            "uvx",
            "--from",
            (PACKAGES_DIR / args.package).as_posix(),
            args.command,
            dcc_arg,
        ],
        encoding="utf-8",
        text=True,
    )

    # Log the result
    if ret_code == 0:
        logger.info(
            "Test for package '%s' and command '%s' successful!",
            args.package,
            args,
        )
    else:
        logger.error(
            "Test for package '%s' and command '%s' failed",
            args.package,
            args,
        )
    sys.exit(ret_code)


if __name__ == "__main__":
    main()
