
from client import Client

import signal

from services_data import service_A

from threading import Event


c = Client(service_name=service_A.name,res_auth=service_A.res_auth)

stop_event = Event()

def shutdwon(signum , frame):

    print("docker is stopping container ...")

    c.stop_run()

    stop_event.set()

    print("docker stopped conatiner")


signal.signal(signalnum=signal.SIGTERM , handler=shutdwon)


# c.start_run()

c.true_test(product_id=101)



print("waiting for stop_event ...")

stop_event.wait()

print("stop_event stopped")




