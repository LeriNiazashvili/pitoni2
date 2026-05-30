import threading

def is_prime(n):
    if n <= 1:
        print(f"რიცხვი {n}: შედგენილია")
        return
    for i in range(2, n):
        if n % i == 0:
            print(f"რიცხვი {n}: შედგენილია")
            return
    print(f"რიცხვი {n}: მარტივია")

num_list = [17, 25, 74, 199, 101, 41, 39, 50, 20, 19, 51]
threads = []

for num in num_list:
    t = threading.Thread(target=is_prime, args=(num,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()