import crudMenu, crudTransaksi

selesai = False
while not selesai:
    crudMenu.clearSystem()
    print(""" ----- Catat Roti.in -----
1. Transaksi baru
2. Melihat transaksi
3. Daftar menu
4. Menutup program""", '\n')

    pilih = int(input('Memilih menu : '))

    if pilih == 1:
        crudMenu.clearSystem()
        crudMenu.read()
        nama = input('Nama : ')
        jenis = []
        jumlah = []
        fin =  False
        while not fin:
            n_jenis = int(input('Jenis roti (no) : '))
            n_jumlah = int(input('Jumlah : '))
            jenis.append(n_jenis)
            jumlah.append(n_jumlah)
            q = input('Apakah ingin menambah pesanan? y/n : ')
            if q == 'y':
                pass
            elif q == 'n':
                # print(jenis, jumlah)
                fin=True
            else:
                pass
        total= 0
        a=0
        for i in jenis:
            # print(jenis, jumlah)
            total = total + (crudMenu.r_dataMenu()[i-1]['harga']*jumlah[a])
        bayar = int(input('Dibayar : '))
        kembalian = bayar-total
        crudTransaksi.createTransaksi(nama, jenis, jumlah, total, kembalian)

    elif pilih == 2:
        crudTransaksi.readTransaksi()

    elif pilih == 3:
        daftar = False
        while not daftar:
            crudMenu.clearSystem()
            print('-'*5,'Daftar Menu','-'*5)
            print("""1. Melihat daftar menu
2. Menambah menu
3. Mengedit menu
4. Menghapus menu
5. Kembali
6. Keluar dari program""", '\n')
            pilih_dft = int(input('Memilih menu : '))

            if pilih_dft == 1:
                crudMenu.clearSystem()
                print('-'*5,'Melihat Menu','-'*5)
                crudMenu.read()
                input('Enter untuk kembali')
            elif pilih_dft == 2:
                jenis = input('Jenis roti : ')
                harga = int(input("Harga : "))

                # for i in :
                #     if i['jenis'] == jenis:
                #         print('Jenis roti sudah ada')
                #         break
                #     else:
                #         pass
                crudMenu.create(jenis, harga, )

            elif pilih_dft == 3:
                crudMenu.update()
            elif pilih_dft == 4:
                crudMenu.delete()
            elif pilih_dft == 5:
                daftar = True
            elif pilih_dft == 6:
                daftar = True
                selesai = True
            else:
                pass

    elif pilih == 4:
        selesai = True
    else : pass

