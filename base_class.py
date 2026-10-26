
import test_pb2_grpc

import test_pb2

import my_code

from threading import RLock

from typing import TYPE_CHECKING

if TYPE_CHECKING:

    import grpc



class Base_class(test_pb2_grpc.ProductServiceServicer):

    def __init__(self):

        self.rlock = RLock()

        self.running = False

    def start_run(self):

        self.running = True

    def stop_run(self):

        self.running = False

    def GetProduct(self , request: "test_pb2.GetProductRequest" , context: "grpc.ServicerContext") -> test_pb2.GetProductResponse:

        if not self.running:

            context.abort(grpc.StatusCode.UNAVAILABLE , "server is not started yet")

        product_id = request.product_id

        if product_id in my_code.PRODUCTS_DB:

            item = my_code.PRODUCTS_DB[product_id]

            item["check_count"] += 1

            with self.rlock:

                if item["remain"] > 0:

                    item["remain"] -= 1

            response = test_pb2.GetProductResponse(
                product_id=product_id,
                title=item["title"],
                price=item["price"],
                is_available=item["is_available"]
            )

        else:

            response = test_pb2.GetProductResponse(
                product_id=product_id,
                title="NOT found",
                price=0.0,
                is_available=False
            )

        return response

    def UpdatePrice(self, request: test_pb2.UpdatePriceRequest , context: "grpc.ServicerContext") -> test_pb2.UpdatePriceResponse:

        if not self.running:

            context.abort(grpc.StatusCode.UNAVAILABLE , "server is not started yet")

        product_id = request.product_id

        if product_id in my_code.PRODUCTS_DB:

            item = my_code.PRODUCTS_DB[product_id]

            last_price: float = item["price"]

            item["price"] = request.new_price

            response = test_pb2.UpdatePriceResponse(
                success=True,
                message=f"price updated from {last_price} to {request.new_price}"
            )

        else:

            response = test_pb2.UpdatePriceResponse(
                success=False,
                message="NO such product EXIST"
            )

        return response


