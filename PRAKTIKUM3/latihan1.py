import random  
n = int(input("Masukkan jumlah bilangan acak (n): "))

count = 0

while count < n:
    for i in range(5): 
        if count >= n:
            break

        angka = random.random()
        if angka < 0.5:
            print(angka)
            count += 1