

from dataclasses import dataclass

@dataclass
class Service_Data:
    name: str
    res_auth: str


service_A = Service_Data(name="A",res_auth="127.0.0.1:5050")
