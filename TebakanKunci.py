kunci = int(input("Kunci : "))
tebakan = int(input("Tebakan : "))
salah = tebakan != kunci
while (salah) :
    tebakan = int(input("Tebakan : "))
    salah = tebakan != kunci 
print ("tebakan benar") 
 