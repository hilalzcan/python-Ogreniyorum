nabiz = int(input("nabız değerini girin: "))
if nabiz < 0:
    print("nabız değeri eksi olamaz")
elif nabiz == 0:
    print("nabız değeri sıfır olamaz")
elif nabiz < 60:
    print("nabız düşük")
elif nabiz >= 60 and nabiz <= 100:
    print("nabız normal aralıkta")
elif nabiz > 100 and nabiz <= 120:
    print("nabız yüksek")
else:
    print("nabız çok yüksek, doktora gidin!")   
