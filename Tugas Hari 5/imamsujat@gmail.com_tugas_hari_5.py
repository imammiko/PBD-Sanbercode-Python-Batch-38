'''Soal 1: Comparison Operator

- Berikan contoh comparison dari tipe data string
- Berikan contoh comparison dari tipe data boolean
- Berikan contoh comparison dari tipe data integer
'''

#kerjakan disini
#string
print("a" == "a")
#boolean
print(True == False)
#integer
print(1 == 2)





#---------------------------------------------------------------------------
'''Soal 2: Boolean Comparison

- Berikan contoh gabungan multiple comparison menggunkan Boolean Comparisin 'and'
- Berikan contoh gabungan multiple comparison menggunkan Boolean Comparisin 'or'
- Berikan contoh gabungan multiple comparison menggunkan Boolean Comparisin 'not'
'''

#kerjakan disini

#and            
print(1 == 1 and 2 == 2)
#or
print(1 == 1 or 2 == 2)
#not
print(not 1 == 1)


#-----------------------------------------------------------------------------
'''Soal 3: If-Else Statement

Lengkapi kode untuk menghasilkan suatu output yang di harapkan

- Bualah sebuah if-else statement yang dimana akan mem-print 'High' jika grade adalah 'A' dan price lebih dari 100000, kemudian mem-print 'Medium' jika grade adalah 'A' dan price lebih dari 50000 dan memprint 'low' jika grade adalah 'A' dan price lebih kecil dan sama dengan 50000.
'''

#kerjakan disini
grade = 'A'
price = 100000

if grade == 'A' and price > 100000:
    print('High')
elif grade == 'A' and price > 50000:
    print('Medium')
elif grade == 'A' and price <= 50000:
    print('Low')



#----------------------------------------------------------------------------------
'''Soal 4: Comparison Operator dengan fungsi

Buatlah sebuah fungsi yang menerima satu argument bertipe data numeric dan menghasilkan sebuah return sebagai berikut :
- menghasilkan return 'Aneh' jika nilai dari argument tersebut adalah bilangan ganjil
- menghasilkan return 'Tidak Aneh' jika nilai dari argument tersebut adalah bilangan genap dan diantara nilai 2 sampai 5 (2 dan 5 termasuk)
- menghasilkan return 'Aneh' jika nilai dari argument tersebut adalah bilangan genap dan diantara nilai 6 sampai 20 (6 dan 20 termasuk)
- menghasilkan return 'Tidak Aneh' jika nilai dari argument tersebut adalah bilangan genap dan lebih besari dari 20
'''

#kerjakan disini
def fungsi(x):
    if x % 2 == 1:
        return 'Aneh'
    elif x % 2 == 0 and x >= 2 and x <= 5:
        return 'Tidak Aneh'
    elif x % 2 == 0 and x >= 6 and x <= 20:
        return 'Aneh'
    elif x % 2 == 0 and x > 20:
        return 'Tidak Aneh'