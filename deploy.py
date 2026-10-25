
import my_code

import signal

from services_data import service_A

from client import Client


service_a = my_code.Service(service_name=service_A.name,resolver_authority=service_A.res_auth)

c = Client()


def shutdwon(signum , frame):

    print("docker is stopping container ...")

    service_a.stop_run()

    print("docker stopped conatiner")


signal.signal(signalnum=signal.SIGTERM , handler=shutdwon)



service_a.start_run()

c.start_run()

c.stop_run()

r = c.GetProduct(product_id=101)

r2 = c.GetProduct(product_id=101)


print(r.product_id,r.title,r.price,r.is_available)

c.stop_run()

service_a.stop_run()

print(my_code.PRODUCTS_DB)



