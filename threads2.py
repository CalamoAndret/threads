#Implementação de Threads
#Cálamo Andret - 2110383

import threading
import random

matriz = [[random.randint(1, 10) for j in range(5)] for i in range(5)]
print("Matriz:")
for linha in matriz:
    print(linha)

def soma_linha(matriz, linha):
    soma = sum(matriz[linha])
    print(f"Soma da linha {linha+1}: {soma}")

threads = []

for i in range(5):
    t = threading.Thread(target=soma_linha, args=(matriz, i))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()
