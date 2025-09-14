jenis_cupang = ["Cupang HMPK", "Cupang Blue Rim", "Cupang Plakat"]

layak_kontes = []

while True:
    print("-----------------MENU------------------")
    print("1. Lihat Jenis Ikan Cupang")
    print("2. Tambah Jenis Ikan Cupang")
    print("3. Singkirkan Ikan Cupang")
    print("4. Validasi Kelayakan Untuk Kontes Ikan Cupang")
    print("5. Keluar")
    print("---------------------------------------")

    menu = (input("Pilih Menu dengan Angka: "))

    if menu == "1":
        print("List Jenis Ikan Cupang\n",jenis_cupang)
    elif menu == "2":
        tambah = input("Masukkan Jenis Ikan Cupang: ")
        jenis_cupang.append(tambah)
        print("\nAnda telah menambahkan", tambah)
        print(jenis_cupang)
    elif menu == "3":
        hapus_ikan = input("Masukkan Jenis Ikan Cupang Yang Ingin Disingkirkan: ")
        if hapus_ikan in jenis_cupang:
            jenis_cupang.remove(hapus_ikan)
            print(hapus_ikan, "Telah Disingkirkan")
            print(jenis_cupang)
        elif hapus_ikan not in jenis_cupang:
            print("Ikan Cupang Tidak Valid")
        else:
            print("Error")
    elif menu == "4":
        cek_nama = input("\nJenis Ikan Cupang: ")
        if cek_nama not in jenis_cupang:
            print("Ikan Cupang Tidak Valid")
        else:
            cek_umur = int(input("Umur?(Bulan): "))
            cek_penyakit = input("Penyakit?(Ada/Tidak Ada): ")
            cek_fisik = input("Kondisi Fisik?(Luka/Normal): ")
            if cek_penyakit == "Ada" or cek_fisik == "Luka":
                print("\nIkan Cupang Tidak Layak Ikut Kontes")
            else:
                print("\nIkan Cupang Layak Ikut Kontes")
                layak_kontes.append(cek_nama)
                print(cek_nama, "Ditambahkan Ke Daftar Lolos Validasi Kelayakan Kontes")
                print(layak_kontes)
    elif menu == "5":
        print("Terimakasih Sudah Menggunakan Program Ini")
        break
    else:
        print("\nError")

