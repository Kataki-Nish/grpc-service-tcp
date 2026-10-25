

import server

from threading import Thread



PRODUCTS_DB = {
    101: {"title": "Laptop", "price": 1200.0, "is_available": True,"check_count":0,"remain":10},
    102: {"title": "Mouse", "price": 25.0, "is_available": False,"check_count":0,"remain":12}
}


class Service:

    def __init__(self,service_name: str,resolver_authority: str):

        self.resolver_authority = resolver_authority

        self.name = service_name

        self.server_and_BC = server.serve(self.name,resolver_authority=self.resolver_authority)

        self.server = self.server_and_BC.server

        self.base_class = self.server_and_BC.base_class

        self.thread = None

    def start_run(self):

        print(f"starting server of service {self.name} ...")

        self.server.start()

        print(f"server of service {self.name} started")

        self.thread = Thread(target=self.server.wait_for_termination)

        self.thread.start()

        print(f"starting base_class of service {self.name} ...")

        self.base_class.start_run()

        print(f"base_class of service {self.name} started")


    def stop_run(self):

        print(f"stopping base_class of service {self.name} ...")

        self.base_class.stop_run()

        print(f"base_class of service {self.name} stopped")

        print(f"stopping server of service {self.name} ...")

        shutdwon_event = self.server.stop(grace=10)

        shutdwon_event.wait()

        if not self.thread is None:

            self.thread.join()

        if self.thread.is_alive():

            raise Exception(f"Error: server of service {self.name} cant be stopped")

        self.thread = None
        
        print(f"serverr of service {self.name} stoped")





