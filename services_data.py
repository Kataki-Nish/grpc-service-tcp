

from dataclasses import dataclass

@dataclass
class Service_Data:
    name: str
    res_auth: str


service_A = Service_Data(name="A",res_auth="service_a1:5050")
