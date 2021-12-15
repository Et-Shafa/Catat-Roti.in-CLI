import os, json

datamenu = 'datamenu.json'

def clearSystem():
    os.system('cls')

def r_data():
    with open(datamenu, 'r') as data:
        return json.load(data)

def create(jenis, harga):
    clearSystem()
    print('-'*5,'Menambah Menu','-'*5)
    tmp,ket_roti = [],{}

    try:
        with open(datamenu, 'r') as data:
            reader =  json.load(data)
            tmp=reader
    except:
        pass

    ket_roti['jenis'] = jenis
    ket_roti['harga'] = harga
    tmp.append(ket_roti)

    with open(datamenu, 'w') as json_file:
        json.dump(tmp, json_file, indent=4)
    
    clearSystem()
    print ('Menu telah ditambahkan')
    input('Enter untuk kembali')

# create('a', 123, r_data())
def read():
    try:
        with open(datamenu, 'r') as data:
            reader =  json.load(data)
    except:
        pass
    print('-'*30)
    print(f"{'No.':^3} {'Jenis':^15} {'Harga':^12}")
    print('-'*30)
    a=0
    for i in range(len(reader)):
        print(f"{i+1:^3} {reader[i]['jenis']:^15} {reader[i]['harga']:^12}")
        # print(i['jenis'])
    
def update():
    clearSystem()
    try:
        with open(datamenu, 'r') as data:
            reader =  json.load(data)
    except:
        pass
    print('-'*5,'Mengubah Menu','-'*5)
    tmp,ket_roti = [],{}
    tmp = reader
    read()
    # print('\n')
    indx =  int(input('Nomor menu : '))
    print('''--- yang akan diedit ---
1. Jenis
2. Harga
3. Jenis dan Harga
''')
    pilihan = input()
    if pilihan == '1':
        ket_roti['jenis'] = input('Jenis roti : ')
        ket_roti['harga'] = tmp[indx-1]['harga']

    elif pilihan == '2':
        ket_roti['jenis'] = tmp[indx-1]['jenis']
        ket_roti['harga'] = int(input("Harga : "))
    elif pilihan == '3':
        ket_roti['jenis'] = input('Jenis roti : ')
        ket_roti['harga'] = int(input("Harga : "))
    else:
        pass
    
    print('Apakah anda yakin akan mengubah menu nomor {}'. format(indx))
    q = input('y/n : ')
    if q == 'y':
        tmp[indx-1]=(ket_roti)
        with open(datamenu, 'w') as json_file:
            json.dump(tmp, json_file, indent=4)
        clearSystem()
        print ('Menu telah diubah')
        input('Enter untuk kembali')
    if q == 'n':
        pass

    
def delete():
    clearSystem()
    try:
        with open(datamenu, 'r') as data:
            reader =  json.load(data)
    except:
        pass
    print('-'*5,'Menghapus Menu','-'*5)
    read()
    # print('\n')
    indx =  int(input('Nomor menu : '))
    print('Apakah anda yakin akan menghapus menu nomor {}'. format(indx))
    q = input('y/n : ')
    if q == 'y':
        reader.pop(indx - 1)
        with open(datamenu, 'w') as json_file:
            json.dump(reader, json_file, indent=4)
        clearSystem()
        print ('Menu telah dihapus')
        input('Enter untuk kembali')
    if q == 'n':
        pass

    # input('Enter untuk kembali')



# x=r_data()
# print(x)
