# ganti aja ke database
table_mahasiswa = []

# perulangan
while True:
    print("Selamat Datang")
    print()
    nama = input("Masukan nama anda, minimal 4 karakter: ")
    # percabangan
    if (len(nama) < 4):
        print('Error: ')
        print('Ganti nama dulu sampai 4 karakter kalau mau daftar kuliah!!!!')
        break
    usia = input("Berapa usia anda: ")
    print()
    if (int(usia) < 17):
        print('Error')
        print('Usianya tambahin dikit, kurang bos')
        break
    table_mahasiswa.append({'nama': nama, 'usia': usia})
    print('Registrasi Berhasil, selamat bergabung!')
    print(table_mahasiswa)
    print()