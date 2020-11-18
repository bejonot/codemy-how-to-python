# Nama file : latihan1-2.py
# Tanggal : 18 November 2020
# Programmer : bejonot
# Deskripsi : Code Python ini merupakan latihan Problem 1.2 yang bersumber dari Codemy.
# Tuan Yon memiliki sebuah bilangan yang terdiri dari tepat 5 digit.
# Kini ia bertanya, berapakah hasil perkalian semua digit-digitnya?
# Buatlah program untuk menjawab pertanyaan Tuan Yon!

limabil = int(input("Masukkan lima bilangan : "))

# Harus pakai for atau while.
# Kalau limabil kurang atau lebih dari lima angka, program bakal minta masukkan input ulang.

if limabil > 99999:
    #Cari tahu cara bikin line baru kalau nulis string dalam satu komando print.
    print("Angka yang kamu masukan lebih dari lima digit.")
    print("Mohon masukkan kembali lima bilangan yang diinginkan.")

elif limabil < 9999:
    print("Angka yang kamu masukkan kurang dari lima digit.")
    print("Mohon masukkan kembali lima bilangan yang diinginkan.")

else:
    #if elif else hanyalah improvisasi programmer. Jawaban latihan1-2.py cukup mulai dari digi_1 sampai print hasil_kali.
    digi_1 = limabil // 10000
    digi_2 = (limabil // 1000) % 10 #modulus dari dua digit di depan dibagi 10, menghasilkan satuannya.
    digi_3 = (limabil // 100) % 10 #modulus dari tiga digit di depan dibagi 10, menghasilkan satuannya.
    digi_4 = (limabil // 10) % 10
    digi_5 = limabil % 10

    hasil_kali = digi_1 * digi_2 * digi_3 * digi_4 * digi_5
    print("Hasil perkalian : %d" % hasil_kali)


