import logging
import os
import subprocess
import sys
from enum import StrEnum

from dccpath import (
    DCCPathError,
    get_blender,
    get_maya,
    get_mayapy,
    get_mobu,
    get_mobupy,
)

logger = logging.getLogger(__name__)


class DCC(StrEnum):
    MAYA = "maya"
    MAYAPY = "mayapy"
    MOBU = "mobu"
    MOBUPY = "mobupy"
    BLENDER = "blender"


def call_dcc(dcc: DCC, version: str) -> int:
    match dcc:
        case DCC.MAYA:
            search_fn = get_maya
        case DCC.MAYAPY:
            search_fn = get_mayapy
        case DCC.MOBU:
            search_fn = get_mobu
        case DCC.MOBUPY:
            search_fn = get_mobupy
        case DCC.BLENDER:
            search_fn = get_blender
        case _:
            logger.error("invalid DCC argument: %s", dcc)
            return 1

    try:
        executable = search_fn(version=version).resolve().as_posix()
    except DCCPathError:
        logger.exception(
            "an error occurred when trying to get the %s executable",
            dcc.value,
        )
        return 1

    logger.debug("running dcc executable: %s", executable)
    return subprocess.call(  # noqa: S603
        [executable, *sys.argv[1:]],
        env=os.environ,
        encoding="utf-8",
        text=True,
    )
