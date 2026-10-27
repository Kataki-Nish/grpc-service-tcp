

from my_code import Service

import signal

from threading import Event

from services_data import service_B


# need for working none-blocking in grpc:

stop_event = Event()


service_b = Service(service_name=service_B.name,resolver_authority=service_B.res_auth)

def shutdwon(signum , frame):

    print("docker is stopping container ...")

    service_b.stop_run()

    stop_event.set()

    print("docker stopped container")


signal.signal(signalnum=signal.SIGTERM , handler=shutdwon)


service_b.start_run()



print("waiting for stop_event ...")

stop_event.wait()

print("stop_event stopped")

