#Implementação de Threads
#Cálamo Andret - 2110383

import threading
import time

def ordem_crescente():
    for i in range(1, 501):
        print(i)
        time.sleep(0.01)

def ordem_decrescente():
    for i in range(500, 0, -1):
        print(i)
        time.sleep(0.01)

t1 = threading.Thread(target=ordem_crescente)
t2 = threading.Thread(target=ordem_decrescente)

t1.start()
t2.start()

t1.join()
t2.join()