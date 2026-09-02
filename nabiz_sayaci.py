dusuk = 0
normal = 0
yuksek = 0

for i in range(10):
    nabiz = int(input(("nabız değerini giriniz: ")))
    if nabiz <= 60:
       print("düşük nabız")
       dusuk += 1
    elif nabiz > 60 and nabiz < 100:
       print("normal nabız")
       normal += 1
    else:
       print("yuksek nabız")
       yuksek += 1

print("düşük nabız sayısı:", dusuk)
print("normal nabız sayısı:", normal)
print("yüksek nabız sayısı:", yuksek)