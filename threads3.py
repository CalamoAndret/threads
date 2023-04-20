#Implementação de Threads
#Cálamo Andret - 2110383

import threading

n = 1000
escalar = 2
vetor = list(range(n))

def multiplicar(inicio, fim):
    for i in range(inicio, fim):
        vetor[i] *= escalar

threads = []

tamanho_parte = n // 10

for i in range(10):
    inicio = i * tamanho_parte
    fim = (i + 1) * tamanho_parte
    thread = threading.Thread(target=multiplicar, args=(inicio, fim))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(vetor)