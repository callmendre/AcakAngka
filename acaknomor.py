import random

for i in range(5):
    #untuk mengacak nomor
    value1 = random.randint(1,20)
    value2 = random.randint(1,20)
    #rumus dan input dari user
    formula = value1 + value2
    print("\n",value1,"+",value2,"= ", end="")
    user = int(input())
    if user == formula:
        print("\n ===== Selamat Kamu Benar =====")
        break
    else:
        print("\n ===== Sepertinya Jawaban Mu Salah, Silahkan Masukkan Jawaban Dengan Benar!!!! =====")
else:
    print("\n ===== Kesempatan Menjawab Kamu Sudah Habis =====")