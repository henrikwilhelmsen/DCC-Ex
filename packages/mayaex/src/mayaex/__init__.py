import logging

from dccex import DCC, call_dcc

logger = logging.getLogger(__name__)
logging.basicConfig(
    level="INFO",
    format="%(levelname)s: %(message)s",
)


def maya2024() -> None:
    call_dcc(dcc=DCC.MAYA, version="2024")


def mayapy2024() -> None:
    call_dcc(dcc=DCC.MAYAPY, version="2024")


def maya2025() -> None:
    call_dcc(dcc=DCC.MAYA, version="2025")


def mayapy2025() -> None:
    call_dcc(dcc=DCC.MAYAPY, version="2025")


def maya2026() -> None:
    call_dcc(dcc=DCC.MAYA, version="2026")


def mayapy2026() -> None:
    call_dcc(dcc=DCC.MAYAPY, version="2026")


def maya2027() -> None:
    call_dcc(dcc=DCC.MAYA, version="2027")


def mayapy2027() -> None:
    call_dcc(dcc=DCC.MAYAPY, version="2027")
