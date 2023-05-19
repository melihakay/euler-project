import threading

N = 1234567
n_cores = 12


def T_n(n):
    a_n = n
    S_n = []
    T_n = 0
    for m in range(1,10000):
        a_n = a_n + (n+m)
        if a_n % (n+m) == 0:
            S_n.append(m)
            T_n += m
    return T_n


sum = 0
remainder = (N-3) % 8
last_index = N - remainder


def T_n_add(n):
    global sum
    sum += T_n(n)

for n in range(3, last_index, 8):
    threads = [None] * n_cores
    for i in range(n_cores):
        threads[i] = threading.Thread(target=T_n_add, args=(n + i,))
        threads[i].start()
        print(n+i)

for n in range(last_index, N+1):
    print(n)
    sum += T_n(n)

print(sum)


        
