#Tipe Data Integer (Angka Satuan)

data_integer = 1
print("Data ini bernilai", data_integer)
print("Dan data ini ber tipe data ",type(data_integer))

#Tipe Data Float (Angka Berkoma)
data_float = 1.5
print("Data ini bernilai", data_float)
print("Dan data ini ber tipe data ",type(data_float))

#Tipe Data String (Kumupulan Karakter)
data_tulisan = "Ini Adalah Tulisan :)"
print("Data ini berisi", data_tulisan)
print("Dan data ini ber tipe data ",type(data_tulisan))

#Tipe Data Boolean (TRUE/FALSE)
data_boolean1 = bool("Aku")
print("Data ini bernilai", data_boolean1)
print("Dan data ini ber tipe data ",type(data_boolean1))

##Tipe data khusus

#Bilangan Kompleks
data_complex = complex(5,6)
print("Data ini bernilai", data_complex)
print("Dan data ini ber tipe data ",type(data_complex))

##Tipe data dari bahasa C
from ctypes import c_double
data_c_double = c_double(5.6)
print("Data ini bernilai", data_c_double)
print("Dan data ini ber tipe data ",type(data_c_double))


