import os, json

datatransaksi= 'dataTransaksi.json'


def clearSystem():
    os.system('cls')


def r_dataTransaksi():
        with open(datatransaksi, 'r') as data:
            return json.load(data)


def createTransaksi(nama, jenis, jumlah, total, kembalian):
    clearSystem()
    tmp,ket_trans = [],{}
    try:
        reader = r_dataTransaksi()
        tmp=reader
    except: pass
    
    print('-'*5,'Menambah Transaksi','-'*5)
    ket_trans['nama'] = nama
    ket_trans['jenis roti'] = jenis
    ket_trans['jumlah'] = jumlah
    ket_trans['total'] = total
    ket_trans['kembalian'] = kembalian
    tmp.append(ket_trans)

    with open(datatransaksi, 'w') as json_file:
        json.dump(tmp, json_file, indent=4)

    clearSystem()
    print ('Menu telah ditambahkan')
    input('Enter untuk kembali')


def readTransaksi():
    clearSystem()
    try:
        reader = r_dataTransaksi()
    except: pass

    print('-'*5,'Melihat Transaksi','-'*5)
    print('-'*30)
    print(f"{'No.':^3} {'Nama':^15} {'Total':^12}") #{'Jumlah':^15} {'Total':^12}")
    print('-'*30)
    a=0
    for i in range(len(reader)):
        print(f"{i+1:^3} {reader[i]['nama']:^15} {reader[i]['total']:^12}")
        # print(i['jenis'])
    input('Enter untuk kembali')

