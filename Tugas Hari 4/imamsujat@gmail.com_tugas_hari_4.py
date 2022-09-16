# Data Structure
'''
Soal 1: Perbedaan Data Structure

Jawab Pertanyaan di bawah ini:

Jelaskan perbedaan dari List, Tuple, Set dan Dictionary!

    List adalah salah satu tipe data untuk mengoleksikan data di python.
    Sama seperti list, tuple juga merupakan struktur data yang digunakan untuk menyimpan satu atau lebih data di dalamnya

'''

#------------------------------------------------------------------
# List
'''
Soal 2: Akses List
Lengkapi kode untuk menghasilkan suatu output yang di harapkan

a = ['1', '13b', 'aa1', 1.32, 22.1, 2.34]
# lengkapi disini dengan slicing list

Expected Output :

[ '13b', 'aa1', 1.32, 22.1 ]

'''
a = ['1', '13b', 'aa1', 1.32, 22.1, 2.34]

print(a[1:5])

#-------------------------------------------------------------------
'''
Soal 3: Akses Nested List
Lengkapi kode untuk menghasilkan suatu output yang di harapkan


a = [
    [5, 9, 8],
    [0, 0, 6]
    ]
# lengkapi disini dengan subsetting list

Expected Output :


[0, 6]
'''
a = [
    [5, 9, 8],
    [0, 0, 6]
    ]

print(a[1][1:])
#---------------------------------------------------------------------
'''
Soal 4: List Manipulation

Lengkapi kode untuk menghasilkan suatu output yang di harapkan

a = [
    [5, 9, 8],
    [0, 0, 6]
    ]
# lengkapi disini change list value



print(a)

Expected Output :

[ [5, 9, 10], [11, 0, 6] ]
'''

a = [
    [5, 9, 8],
    [0, 0, 6]
    ]

a[1][0] = 11
print(a)
#---------------------------------------------------------------------
'''
Soal 5: Delete Element List

Lengkapi kode untuk menghasilkan suatu output yang di harapkan


areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Hilangkan elemen yang bernilai "bathroom" dan 10.50 dalam satu statement code



print(areas)

Expected Output:

['hallway',
 11.25,
 'kitchen',
 18.0,
 'chill zone',
 20.0,
 'bedroom',
 10.75,
 'poolhouse',
 24.5,
 'garage',
 15.45]


'''

areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
            "bathroom", 10.50, "poolhouse", 24.5,
            "garage", 15.45]

del areas[8:10]
print(areas)
#-----------------------------------------------------------------------------------
'''
## Soal 6: List Comprehension

Gunakan metode **list comprehension** untuk mencari anggota dari S yang habis di bagi 2, kemudian assign hasilnya dalam bentuk list ke dalam variabel T.


S = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

T = 

print(T)

Expected Output:

[0, 4, 16, 36, 64]



'''

S = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

T = [x for x in S if x % 2 == 0]
print(T)
#----------------------------------------------------------------------------------
'''
# Tuple

## Soal 7. Mengakses Tuple

Gunakan cara sclicing untuk mengakses tuple sehingga mendapatkan hasil sesuai expected output


tuple_1 = (1, 2, 6, 7, 8, 9, 10)

#akses tuple

Expected Outpout:


(6, 7, 8)



'''
    
tuple_1 = (1, 2, 6, 7, 8, 9, 10)

print(tuple_1[2:5])
#-------------------------------------------------------------------------------
'''
# Dictionary

Soal 8: Menambahkan key-value baru ke Dictionary

Lengkapi kode untuk menghasilkan suatu output yang di harapkan


europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# tambahkan key itali ke objek dictionary dengan value roma


# cek apakah itali ada di dalam objek dictionary

Expected Output:
    
True

'''
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

europe['itali'] = 'roma'

print ('itali' in europe)
#--------------------------------------------------------------------------------
'''
Soal 9: Update dan Remove Dictinary
    
Lengkapi kode untuk menghasilkan suatu output yang di harapkan


europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# update nilai ibukota german ke berlin


# remove australia dari europa


print(europe)

Expected Output:

{'spain': 'madrid', 'france': 'paris', 'germany': 'berlin', 'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw'}
'''
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
            'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
            'australia':'vienna' }

europe['germany'] = 'berlin'
del europe['australia']
print(europe)
#-----------------------------------------------------------------------------------
'''
Soal 10: Nested Dictionary
    
Lengkapi kode untuk menghasilkan suatu output yang di harapkan


country = { 
           'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } 
         }

# berapa populasi dari kota german?


# update data baru, yaitu negara indonesia dengan capital jakarta dan poulasi 250


print(country)

Expected Output:

80.62

{'spain': {'capital': 'madrid', 'population': 46.77}, 'france': {'capital': 'paris', 'population': 66.03}, 'germany': {'capital': 'berlin', 'population': 80.62}, 'norway': {'capital': 'oslo', 'population': 5.084}, 'indonesia': {'capital': 'jakarta', 'population': 250}}

'''

country = {
            'spain': { 'capital':'madrid', 'population':46.77 },
            'france': { 'capital':'paris', 'population':66.03 },
            'germany': { 'capital':'berlin', 'population':80.62 },
            'norway': { 'capital':'oslo', 'population':5.084 }
            }

print(country['germany']['population'])
#------------------------------------------------------------------------------------
'''
Soal 11: Loop Dictionary
    
Lengkapi kode untuk menghasilkan suatu output yang di harapkan


country = { 
           'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 },
           'indonesia' : {'capital':'jakarta', 'population':250}
         }

for ..., .... in country.items():
    print('Ibukota '+....+' adalah ' + ....)

Expected Output:
    
Ibukota spain adalah madrid

Ibukota france adalah paris

Ibukota germany adalah berlin

Ibukota norway adalah oslo

Ibukota indonesia adalah jakarta


'''


country = { 
           'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 },
           'indonesia' : {'capital':'jakarta', 'population':250}
         }


for key, value in country.items():
    print('Ibukota '+key+' adalah ' + value['capital'])
#------------------------------------------------------------------------------
'''
# Set

## Soal 12: Remove Duplicate using set


Hilangkan nilai duplikat dari sebuah objek list dengan menggunakan cara set sehingga menjadi sebuah tipe set


obj_list = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10]

#using set

Expected output: 

{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

'''
obj_list = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10]

obj_set = set(obj_list)

print(obj_set)
#---------------------------------------------------------------------------------
'''
## Soal 13: Mengubah dan menghapus anggota set

Ubahlah dan hapus anggota set sehingga mendapatkan hasil yang diinginkan


set_1 = {1, 2, 3, 4, 5}

#tambahkan anggota set dengan nilai {6,7,8}

#hapus nilai anggota set 8

Expected output:

{1, 2, 3, 4, 5, 6, 7}

'''
set_1 = {1, 2, 3, 4, 5}


set_1.add(6)
set_1.add(7)
set_1.add(8)
set_1.remove(8)
#----------------------------------------------------------------------------------
'''
## Soal 14: Operasi pada Set

Carilah irisan dari ke dua set dengan menggunakan metode intersection


set_2 = {6, 8, 9, 10, 24}
set_3 = {6, 10, 8, 25, 13}

#intersection set

Expected output:


{6, 8, 10}


'''

set_2 = {6, 8, 9, 10, 24}
set_3 = {6, 10, 8, 25, 13}

print(set_2.intersection(set_3))