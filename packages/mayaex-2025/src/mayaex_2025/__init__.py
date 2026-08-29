# Copyright (C) 2026 Henrik Wilhelmsen.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at <https://mozilla.org/MPL/2.0/>.

"""A CLI wrapper for maya.

Adds a command that will locate and run the maya executable.

This package has been auto-generated as part of the
`dccex` package to add the specific DCC versioned command.
"""

import logging
import sys

from dccex import call_dcc_exe

logger = logging.getLogger(__name__)


def setup_logging() -> None:
    """Set up basic logging."""
    logging.basicConfig(
        level="INFO",
        format="%(levelname)s: %(message)s",
    )


def maya() -> None:
    """Run maya."""
    setup_logging()
    sys.exit(
        call_dcc_exe(dcc_exe="maya",
        version="2025",
        args=sys.argv[1:],
        ),
    )


def mayapy() -> None:
    """Run mayapy."""
    setup_logging()
    sys.exit(
        call_dcc_exe(dcc_exe="mayapy",
        version="2025",
        args=sys.argv[1:],
        ),
    )
