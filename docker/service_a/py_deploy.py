

from my_code import Service

import signal

from threading import Event

from services_data import service_A


# need for working none-blocking in grpc:

stop_event = Event()


service_a = Service(service_name=service_A.name,resolver_authority=service_A.res_auth)

def shutdwon(signum , frame):

    print("docker is stopping container ...")

    service_a.stop_run()

    stop_event.set()

    print("docker stopped container")


signal.signal(signalnum=signal.SIGTERM , handler=shutdwon)


service_a.start_run()



print("waiting for stop_event ...")

stop_event.wait()

print("stop_event stopped")

