print("""FERGIAWAN SATRIO BAGASKORO
312210169""")
print()
#LATIHAN 1

# PENGGUNAAN END
print ('A', end='')
print ('B', end='')
print ('C', end='')
print ()
print ('D')
print ('E')
print ('F')

# PENGGUNAAN SEPARATOR
v,w, x, y, z = 100, 200, 300, 400, 500
print (v, w, x, y, z)
print (v, w, x, y, z, sep=',')
print (v, w, x, y, z, sep='')
print (v, w, x, y, z, sep=':')
print (v, w, x, y, z, sep='-----')

# STRING FORMAT
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

# STRING FORMAT
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

#LATIHAN 2

a=input("masukkan nilai a:")
b=input("masukkan nilai b:")

print("variable a=",a)
print("variable b=",b)

print("hasil penggabungan {1}&{0}=%s".format(a,b) %(a+b))

a=int(8)
b=int(8)

print("hasil penjumlahan {1}+{0}=%d".format(a,b) %(a+b))
print("hasil pembagian {1}/{0}=%d".format(a,b) %(a/b))

# LATIHAN3

print("""FERGIAWAN SATRIO BAGASKORO
312210169""")
print()
num = int(input("masukan jumlah barisnya:"))
for i in range(1,num+1) :
    print(" "*(num-i)+"* "*i)
for i in range(num-1,0,-1) :
    print(" "*(num-i)+"* "*i)
