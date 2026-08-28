import logging

from dccex import DCC, call_dcc

logger = logging.getLogger(__name__)
logging.basicConfig(
    level="INFO",
    format="%(levelname)s: %(message)s",
)


def mobu2024() -> None:
    call_dcc(dcc=DCC.MOBU, version="2024")


def mobupy2024() -> None:
    call_dcc(dcc=DCC.MOBUPY, version="2024")


def mobu2025() -> None:
    call_dcc(dcc=DCC.MOBU, version="2025")


def mobupy2025() -> None:
    call_dcc(dcc=DCC.MOBUPY, version="2025")


def mobu2026() -> None:
    call_dcc(dcc=DCC.MOBU, version="2026")


def mobupy2026() -> None:
    call_dcc(dcc=DCC.MOBUPY, version="2026")


def mobu2027() -> None:
    call_dcc(dcc=DCC.MOBU, version="2027")


def mobupy2027() -> None:
    call_dcc(dcc=DCC.MOBUPY, version="2027")
