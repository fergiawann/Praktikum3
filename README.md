# Praktikum3
## FERGIAWAN SATRIO BAGASKORO
## Menghitung Luas Dan Keliling Lingkaran Menggunakan Python
Pertama perlu kita ketahui terlebih dahulu rumus dari luas dan keliling lingkaran sebelum kita ingin menghitungnya, rumusnya adalah

```
Luas     = π × r²
Keliling = 2 x π × r`
```

Setelah kita mengetahui rumasnya mari kita mulai masuk ke dalam pycharm

![ss1](https://user-images.githubusercontent.com/115530180/198537380-9b5f093e-87f4-4763-85b9-9f77ca7041a4.png)


Setelah itu kita masukan pi dan nilai jari-jarinya

``` 
pi = 3.14
r = 10
```

![ss2](https://user-images.githubusercontent.com/115530180/198751324-291f1d4f-f651-4272-b5d2-403f84d8a2ec.png)


Lalu selanjutnya masukan rumus luas dan keliling lingkarannya

```
luas = pi*(r*r)
keliling = 2*pi*r
```

![ss3](https://user-images.githubusercontent.com/115530180/198751346-0bde2f0e-ccbd-4fda-a12f-4b30b7cd1a93.png)


Dan terakhir masukkan code berikut

```
print ("Luas Lingkaran \t\t= ",luas)
print ("Keliling Lingkaran\t= ",keliling)
```

![ss4](https://user-images.githubusercontent.com/115530180/198751378-c3ee3c2d-c11b-4d33-87de-56c0ba2becf3.png)


Oke lalu kita run code programnya

![ss5](https://user-images.githubusercontent.com/115530180/198751911-d1201a1f-d009-49b5-ac70-11a0f6b61da0.png)

Maka akan keluar output seperti diatas dan kita sudah mendapatkan hasil dari luas dan keliling lingkarannya

## Flowchart Luas Dan Keliling Lingkaran

![ss6](https://user-images.githubusercontent.com/115530180/198752704-01cf9b2b-9347-4e70-a2fb-bf20db6ffb79.jpg)


```
Deskripsi :
1. Pertama kita masukan terlebih dahulu pi nya
2. Lalu kemudian nilai r nya kita masukan
3. Hitung luas dan keliling lingkaran dengan rumus 
   luas = pi*(r*r)
   keliling = 2*pi*r
4. Tampilkan luas dan keliling lingkaran
```
## Latihan 1
* Penggunaan End

Pada latihan 1 ini pertama kita akan mengetahui fungsi dari penggunaan end dan code programnya seperti di bawah ini
```
print ('A', end='')
print ('B', end='')
print ('C', end='')
print ()
print ('X')
print ('Y')
print ('Z')
```

![ss-latihan1](https://user-images.githubusercontent.com/115530180/198863530-1b6d6117-3139-4301-9260-0a28e475f7f6.png)

Lalu kita run dan outputnya akan menjadi seperti ini

![ss-latihan7](https://user-images.githubusercontent.com/115530180/198863543-736b5619-503f-4629-be66-37e4be313d87.png)

Seperti yang bisa kita lihat di gambar atas fungsi dari penggunaan end adalah membuat inputan 3 baris A,B,C menjadi 1 baris output ABC,
dan bisa kita banding dengan inputan D,E,F yang tanpa menngunakan end outputnya menjadi vertical kebawah.

* Penggunaan Separator

Latihan 1 selanjutnya adalah penggunaan separator dan code programnya dibawah ini
```
v,w, x, y, z = 100, 200, 300, 400, 500
print (v, w, x, y, z)
print (v, w, x, y, z, sep=',')
print (v, w, x, y, z, sep='')
print (v, w, x, y, z, sep=':')
print (v, w, x, y, z, sep='-----')
```

![ss-latihan2](https://user-images.githubusercontent.com/115530180/198863721-b017cdec-49d9-441c-bbf7-c998a9ad6ff8.png)

Lalu kita run dan outputnya akan menjadi seperti ini

![ss-latihan8](https://user-images.githubusercontent.com/115530180/198863731-c282d8eb-6320-4bf2-966c-4af8a2cf5f89.png)

Disini saya menginputkan 5 variabel v,w,x,y,z dengan nilainya 100, 200, 300, 400, 500 dan bisa kita lihat di gambar atas bahwa
dengan menggunakan separator kita bisa menambahkan simbol-simbol yang kita inginkan diantara nilai variabelnya.

* String Format 1

contoh penggunaan dan code programnnya bisa kita lihat dibawah ini
```
print (0, 10**0)
print (1, 10**1)
print (2, 10**2)
print (3, 10**3)
print (4, 10**4)
print (5, 10**5)
print (6, 10**6)
print (7, 10**7)
print (8, 10**8)
print (9, 10**9)
print (10, 10**10)
```

![ss-latihan3](https://user-images.githubusercontent.com/115530180/198863885-e29c3ad6-f2ff-46ac-b1f2-6ca6219b0942.png)

Lalu kita run dan outputnya akan menjadi seperti ini

![ss-latihan9](https://user-images.githubusercontent.com/115530180/198863897-00ffd17b-9449-4fbf-ab9a-0d93fb09ddb7.png)

Dengan penggunaan string format ini kita bisa menambahkan seberapa banyak angka 0 yang kita inginkan.

* String Format 2

Contoh lain dari penggunaan string format bisa kita lihat code programnya di bawah ini
```
print ('{0:>3} {1:>16}'.format(0, 10**0))
print ('{0:>3} {1:>16}'.format(1, 10**1))
print ('{0:>3} {1:>16}'.format(2, 10**2))
print ('{0:>3} {1:>16}'.format(3, 10**3))
print ('{0:>3} {1:>16}'.format(4, 10**4))
print ('{0:>3} {1:>16}'.format(5, 10**5))
print ('{0:>3} {1:>16}'.format(6, 10**6))
print ('{0:>3} {1:>16}'.format(7, 10**7))
print ('{0:>3} {1:>16}'.format(8, 10**8))
print ('{0:>3} {1:>16}'.format(9, 10**9))
print ('{0:>3} {1:>16}'.format(10, 10**10))
```

![ss-latihan4](https://user-images.githubusercontent.com/115530180/198864188-747ccc77-24e4-440f-854e-447fbb183588.png)

Lalu kita run dan outputnya akan menjadi seperti ini

![ss-latihan10](https://user-images.githubusercontent.com/115530180/198864198-d8904526-1420-4ac3-8fe6-46e042bcde18.png)

Contoh string format yang ke 2 ini kita bisa menambahkan seberapa banyak spasi yang kita mau di awalannya
## Latihan 2
Pada latihan 2 ini kita akan menginput 2 variabel yaitu a dan b, dan kita akan menggabungkan, menambahkan dan membagi kedua variabel
dengan code pemrograman dibawah ini
```
a=input("masukkan nilai a:")
b=input("masukkan nilai b:")

print("variable a=",a)
print("variable b=",b)

print("hasil penggabungan {1}&{0}=%s".format(a,b) %(a+b))

a=int(8)
b=int(8)

print("hasil penjumlahan {1}+{0}=%d".format(a,b) %(a+b))
print("hasil pembagian {1}/{0}=%d".format(a,b) %(a/b))
```

![ss-latihan5](https://user-images.githubusercontent.com/115530180/198864903-44d75341-0d96-4475-8fab-f07efd1c8925.png)

Kita run dan kita input nilai dari variabel a dan b

![ss-latihan11](https://user-images.githubusercontent.com/115530180/198864914-b2ff99e4-95af-40ce-bd8f-e385150abf78.png)

![ss-latihan12](https://user-images.githubusercontent.com/115530180/198864929-549db864-9639-4be5-8926-97e0e4dff877.png)

Maka kita sudah mendapatkan hasil dari penggabungan, penambahan dan pembagian dari variabel a dan b

## Latihan 3
Pada latihan terakhir kita ini, kita akan menyusun simbol "*" menjadi bentuk seperti di bawah ini menggunakan python

![ss-latihan14](https://user-images.githubusercontent.com/115530180/198865932-ea9cff5f-4afe-4337-96df-d04d27e12c15.png)





