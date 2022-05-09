from dataclasses import dataclass


@dataclass(frozen=True)
class Env:
    host: str
    defipayPub: str
