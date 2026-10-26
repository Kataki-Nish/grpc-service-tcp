

import grpc

import test_pb2_grpc

from base_class import Base_class

from concurrent import futures

from dataclasses import dataclass


@dataclass
class Server_BC:
    server: grpc.Server
    base_class: Base_class




def serve(service_name: str,resolver_authority: str) -> Server_BC:

    print(f"creating of server of service {service_name} ...")

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))

    base_class = Base_class()

    test_pb2_grpc.add_ProductServiceServicer_to_server(servicer=base_class,server=server)

    if ":" not in resolver_authority:

        resolver_authority = "unix://" + resolver_authority

    port = server.add_insecure_port(resolver_authority)

    # debug

    print(f"DEBUG: add_insecure_port returned: {port}")

    # -----

    print(f"server of service {service_name} created")

    return Server_BC(server=server,base_class=base_class)





