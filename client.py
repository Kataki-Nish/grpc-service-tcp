
import grpc

import test_pb2

import test_pb2_grpc

from services_data import service_A

class Client:

    id = 0

    def __init__(self) -> None:

        self.id = Client.id

        Client.id += 1

    def start_run(self) -> None:

        print(f"starting of client {self.id} ...")

        self.channel = grpc.insecure_channel(target=service_A.res_auth)

        self.client = test_pb2_grpc.ProductServiceStub(channel=self.channel)

        print(f"client {self.id} started")

    def stop_run(self) -> None:

        print(f"stopping of client {self.id} ...")

        self.channel.close()

        print(f"client {self.id} stopped")

    def GetProduct(self , product_id: int) -> "test_pb2.GetProductResponse":

        req = test_pb2.GetProductRequest(product_id=product_id)

        try:

            res = self.client.GetProduct(req)

        except ValueError:

            print("channel is closed")

            self.start_run()

            res = self.GetProduct(product_id=product_id)

        except grpc.RpcError:

            print(f"server of service {service_A.name} is NOT started yet")

            raise

        return res

    def UpdatePrice(self , product_id: int , new_price: float) -> "test_pb2.UpdatePriceResponse":

        req = test_pb2.UpdatePriceRequest(product_id=product_id,new_price=new_price)

        res = self.client.UpdatePrice(req)

        return res


