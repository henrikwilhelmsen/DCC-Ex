import logging

from dccex import DCC, call_dcc

logger = logging.getLogger(__name__)
logging.basicConfig(
    level="INFO",
    format="%(levelname)s: %(message)s",
)


def blender_4_5() -> None:
    call_dcc(dcc=DCC.BLENDER, version="4.5")


def blender_4() -> None:
    call_dcc(dcc=DCC.BLENDER, version="4")


def blender_5_0() -> None:
    call_dcc(dcc=DCC.BLENDER, version="5.0")


def blender_5_1() -> None:
    call_dcc(dcc=DCC.BLENDER, version="5.1")


def blender_5_2() -> None:
    call_dcc(dcc=DCC.BLENDER, version="5.2")


def blender_5() -> None:
    call_dcc(dcc=DCC.BLENDER, version="5")
