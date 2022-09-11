
from dataclasses import dataclass

# Class to store data 
@dataclass(frozen=True, order=True)
class IP:
    source: str = ""
    destination: str = ""
    port: str = ""
    port_number: str = ""