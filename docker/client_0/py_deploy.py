
from client import Client

import signal


from threading import Event


c = Client()

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




