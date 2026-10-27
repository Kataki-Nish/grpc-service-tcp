
import grpc

import test_pb2

import test_pb2_grpc

from time import sleep

from threading import Thread

class Client:

    id = 0

    def __init__(self , service_name: str , res_auth: str) -> None:

        self.id = Client.id

        Client.id += 1

        self.service_name = service_name

        if not ":" in res_auth:

            res_auth = "unix://" + res_auth

        self.res_auth = res_auth

        self.testing = False

        self.thread = None

        self.start_run()

    def start_run(self) -> None:

        print(f"starting of client {self.id} ...")

        self.channel = grpc.insecure_channel(target=self.res_auth)

        self.client = test_pb2_grpc.ProductServiceStub(channel=self.channel)

        print(f"client {self.id} started")

    def stop_run(self) -> None:

        self.testing = False

        if not self.thread is None:

            self.thread.join(timeout=5)

            if self.thread.is_alive():

                raise Exception("test thread cant be stopped")

        print(f"stopping of client {self.id} ...")

        self.channel.close()

        print(f"client {self.id} stopped")

    def GetProduct(self , product_id: int , retry_count: int = 3) -> test_pb2.GetProductResponse | grpc.RpcError | TimeoutError:

        while retry_count > 0:

            req = test_pb2.GetProductRequest(product_id=product_id)

            try:

                res = self.client.GetProduct(req, timeout=2)

                return res

            except TimeoutError:

                retry_count -= 1

                continue
            
            except ValueError:

                print("channel is closed")

                self.start_run()

                continue

            except grpc.RpcError as e:

                print(f"server of service {self.service_name} is NOT started yet")

                # raise

                res = e

                return res

        else:

            return TimeoutError("Error: retry_count finished")


    def UpdatePrice(self , product_id: int , new_price: float , retry_count: int = 3) -> test_pb2.UpdatePriceResponse | grpc.RpcError | TimeoutError:

        while retry_count > 0:

            req = test_pb2.UpdatePriceRequest(product_id=product_id,new_price=new_price)

            try:

                res = self.client.UpdatePrice(req,timeout=2)

                return res

            except TimeoutError:

                retry_count -= 1

                continue
            
            except ValueError:

                print("channel is closed")

                self.start_run()

                continue

            except grpc.RpcError as e:

                print(f"server of service {self.service_name} is NOT started yet")

                # raise

                res = e

                return res

        else:

            return TimeoutError("Error: retry_count finished")




    def true_test(self,product_id):

        def test():

            self.testing = True

            i = 10

            while self.testing:

                print(self.GetProduct(product_id=product_id))

                print(self.UpdatePrice(product_id=product_id,new_price=i))

                i += 3

                sleep(0.1)
        
        self.thread = Thread(target=test)

        self.thread.start()


