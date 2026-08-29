# Copyright (C) 2026 Henrik Wilhelmsen.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at <https://mozilla.org/MPL/2.0/>.

"""DCCEX - A package for finding and running DCC executables."""

import logging
import os
import subprocess
from typing import Literal

from dccpath import (
    DCCPathError,
    get_blender,
    get_maya,
    get_mayapy,
    get_mobu,
    get_mobupy,
)

logger = logging.getLogger(__name__)


SupportedDCCs = Literal["maya", "mayapy", "mobu", "mobupy", "blender"]


def call_dcc_exe(
    dcc_exe: SupportedDCCs,
    version: str,
    args: list[str] | None = None,
) -> int:
    """Locate and call the given DCC executable for the given version.

    Args:
        dcc_exe: The DCC to call
        version: The DCC version
        args: Optional extra arguments to pass to the DCC

    Returns:
        The return code of the subprocess call to the executable, or 1 if an error
        occurred during setup.
    """
    if args is None:
        args = []

    match dcc_exe:
        case "maya":
            search_fn = get_maya
        case "mayapy":
            search_fn = get_mayapy
        case "mobu":
            search_fn = get_mobu
        case "mobupy":
            search_fn = get_mobupy
        case "blender":
            search_fn = get_blender
        case _:
            logger.error("invalid DCC argument: %s", dcc_exe)
            return 1

    try:
        executable = search_fn(version=version).resolve().as_posix()
    except DCCPathError:
        logger.exception(
            "an error occurred when trying to get the %s executable",
            dcc_exe,
        )
        return 1

    logger.debug("running dcc executable: %s", executable)
    return subprocess.call(  # noqa: S603
        [executable, *args],
        env=os.environ,
        encoding="utf-8",
        text=True,
    )
