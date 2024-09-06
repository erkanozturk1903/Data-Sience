###############################################
# GÖREV 1: Veri yapılarının tipleriniz inceleyiniz.
###############################################

x = 8
print(type(x))

y = 3.2
type(3.2)

print(type(y))


z = 8j + 18

print(type(z))
print(type('y'))


a = "Hello World"
print(type(a))

b = True
print(type(b))


c = 23 < 22
print(type(c))

l = [1, 2, 3, 4,"String",3.2, False]
print(type(l))


d = {"Name": "Jake",
     "Age": [27,56],
     "Adress": "Downtown"}
print(type(d))

t = ("Machine Learning", "Data Science")
print(type(t))


s = {"Python", "Machine Learning", "Data Science","Python"}

print(type(s))

###############################################
# GÖREV 1: Veri yapılarının tipleriniz inceleyiniz.
###############################################

x = 8
print(type(x))

y = 3.2
type(3.2)

print(type(y))


z = 8j + 18

print(type(z))
print(type('y'))


a = "Hello World"
print(type(a))

b = True
print(type(b))


c = 23 < 22
print(type(c))

l = [1, 2, 3, 4,"String",3.2, False]
print(type(l))


d = {"Name": "Jake",
     "Age": [27,56],
     "Adress": "Downtown"}
print(type(d))

t = ("Machine Learning", "Data Science")
print(type(t))


s = {"Python", "Machine Learning", "Data Science","Python"}

print(type(s))


###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
###############################################

text = "The goal is to turn data into information, and information into insight."
text1 = text.upper()
print(text1)

text2 = text1.replace(",", " ").replace(".", " ")
print(text2)

text3 = text2.split()
print(text3)

#text4 = [f'"{word}"' for word in text3]
#final_text = ', '.join(text4)
#print(f'[{final_text}]')

###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Adım 1: Verilen listenin eleman sayısına bakın.
#print(len(lst))
len(lst)

# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.
print("Sıfırıncı = "+lst[0] +"  onuncu = " +lst[10])
#[lst[0], lst[10]]

# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.
yeni_liste = lst[0:4]
print(yeni_liste)

# Adım 4: Sekizinci index'teki elemanı silin.
lst.pop(8)
#del lst[8]
print(lst)

# Adım 5: Yeni bir eleman ekleyin.

lst.append(4)
print(lst)

# Adım 6: Sekizinci index'e  "N" elemanını tekrar ekleyin.

#lst.append("N")
lst.insert(8, "N")
print(lst)

###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
###############################################

dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}


# Adım 1: Key değerlerine erişiniz.
dict.keys()
#print(k)

# Adım 2: Value'lara erişiniz.

v=dict.values()
print(v)

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.

dict["Daisy"] = ["England", 13]
print(dict)
#dict["Daisy"][1] = 13

# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
dict.update({"Ahmet" : ["Turkey",24]})
#dict["Ahmet"] = ["Turkey", 24]

# Adım 5: Antonio'yu dictionary'den siliniz
dict.pop("Antonio")

###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve bu listeleri return eden fonskiyon yazınız.
###############################################
l = [2, 13, 18, 93, 22]
def func(l):
    groups = [[],[]]
    for m in l:
        if m % 2 == 0:
            groups[0].append(m)
        else:
            groups[1].append(m)
    print(groups)
    return groups

func(l)

___________________________________
# indekse göre tek çift ayırma

l = [2, 13, 18, 93, 22]
group_l = [[], []]
def tek_cift(l):
    for i, value in enumerate(l):
        if i % 2 == 0:
            group_l[0].append(value)
        else:
            group_l[1].append(value)
    return group_l
tek_cift(l)

------------

def func( lst : list):
    even_numbers = [number for number in lst if (number % 2) == 0]
    odd_numbers = [number for number in lst if (number % 2) != 0]
    return even_numbers, odd_numbers

lst = [1,2,3,4,5,34,5,656,7]
print(func(lst))
-----------------------

l = [2, 13, 18, 93, 22]
groups = [[], []]

def func(x):

    for x in l:
        if x % 2 == 0:
            groups[0].append(x)
        else:
            groups[1].append(x)
    return groups

func(l)

-----------------
l = [2, 13, 18, 93, 22]

def cift_tek(numaralar):
    cift_numara = []
    tek_numara = []

    for num in numaralar:
        if num % 2 == 0:
            cift_numara.append(num)
        else:
            tek_numara.append(num)

    return cift_numara, tek_numara

cift_numara, tek_numara = cift_tek(l)
print("Çift sayılar:", cift_numara, "\nTek sayılar:", tek_numara)

###############################################
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
###############################################

# bu çözümü vermiyor 4. 5. 6. diye devam ediyor
ogrenciler = ["Ali", "Veli", "Ayse", "Talat", "Zeynep", "Ece"]

for index, ogrenci in enumerate(ogrenciler):
    if index < 3:
        print(f"Mühendislik Fakültesi {index + 1} . ogrenci: {ogrenci}")
    else:
        print(f"Tip Fakültesi {index + 1} . ogrenci: {ogrenci}")


---------------------
ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]
sayac = 1

for i, value in enumerate(ogrenciler, start=1):
    if i <= 3:
        print(f"Muhendislik Fakultesi {i}. Ogrenci, {value}")
    if i > 3:
        print(f"Tip Fakultesi {sayac}. Ogrenci, {value}")
        sayac += 1

----------------------------------
# beklenen çıktıdan farklı bir çıktı ama doğru çalışıyor
ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

print("Mühendislik Fakültesi:")
for i, ogrenci1 in enumerate(ogrenciler):
    if i < 3:
        print(f"{i + 1}. {ogrenci1}")

print("\nTıp Fakültesi:")
for i, ogrenci2 in enumerate(ogrenciler):
    if i >= 3:
        print(f"{i - 2}. {ogrenci2}")

____________________
# Farklı bir yöntem

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

A = ogrenciler[0:3]
B = ogrenciler[3:6]

    for index, ogr in enumerate(A,1):
        print("Muhendislik Fakultesi", index, ".", "öğrenci:", ogr)

    for index, ogr in enumerate(B, 1):
    print("Tıp Fakultesi", index, ".", "öğrenci:", ogr)


###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
###############################################

ders_kodu = ["CMP1005", "PSY1005", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

for k, kod, kon in zip(kredi, ders_kodu, kontenjan):
    print(f"Kredi {k} olan {kod} kodlu dersin kontenjanı {kon} kişidir.")

   ------------
ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]

kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

ders_kredi_kontenjan=zip(ders_kodu, kredi, kontenjan)
print("Ders Bilgileri:")
for ders, kredi, kontenjan in ders_kredi_kontenjan:
    print(f"Kredisi {kredi} olan {ders}  kodlu dersin Kontenjanı {kontenjan} kişidir.")


###############################################
# GÖREV 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
###############################################

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def kume_gorevi(kumea, kumeb):
    if kumea.issuperset(kumeb):
        ortaklar = kumea.intersection(kumeb)
        print("Ortak elemanlar:", ortaklar)
    else:
        farklı = kumeb.difference(kumea)
        print("2de olan 1de olmayan:", farklı)
kume_gorevi(kume1, kume2)
___________

# Deniz
kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

if kume2.issubset(kume1):
    print (kume1.intersection(kume2))
else:
    print(kume2 - kume1)

# Dilek

def kumeler(kume1, kume2):
    if kume1.issuperset(kume2):
        print(kume1.intersection(kume2))
    else:
        print(kume2.symmetric_difference(kume1))
kumeler(kume1, kume2)


##################################################
# List Comprehensions
##################################################

# ###############################################
# # GÖREV 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
# ###############################################
#
# # Beklenen Çıktı
#
# # ['NUM_TOTAL',
# #  'NUM_SPEEDING',
# #  'NUM_ALCOHOL',
# #  'NUM_NOT_DISTRACTED',
# #  'NUM_NO_PREVIOUS',
# #  'NUM_INS_PREMIUM',
# #  'NUM_INS_LOSSES',
# #  'ABBREV']
#
# # Notlar:
# # Numerik olmayanların da isimleri büyümeli.
# # Tek bir list comp yapısı ile yapılmalı.

import seaborn as sns
import pandas as pd
df = sns.load_dataset("car_crashes")
numcols = ["NUM_" + col.upper() for col in df.columns if df[col].dtype != "O"]

------------------------------------------------
# Dilek

import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")

num_cols_upper = ["NUM_" + col.upper() if df[col].dtypes in [int, float] else col.upper() for col in df.columns]
print(num_cols_upper)
#output ['NUM_TOTAL', 'NUM_SPEEDING', 'NUM_ALCOHOL', 'NUM_NOT_DISTRACTED', 'NUM_NO_PREVIOUS', 'NUM_INS_PREMIUM', 'NUM_INS_LOSSES', 'ABBREV']


# Diger cözüm

import seaborn as sns
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")

print("sutun_adlari:")
print(df.columns)
yeni_kolon= ["NUM_" + col.upper() if df[col].dtype in ['int64', 'float64'] else col.upper() for col in df.columns]
dataf = yeni_kolon

numcols = ["NUM_" + col.upper() for col in df.columns if df[col].dtype != "O"]

print("yeni_sutun_adlari:")
print(dataf)




# ###############################################
# # GÖREV 2: List Comprehension yapısı kullanarak car_crashes verisindeki isminde "no" barındırmayan değişkenlerin isimlerininin sonuna "FLAG" yazınız.
# ###############################################
#
# # Notlar:
# # Tüm değişken isimleri büyük olmalı.
# # Tek bir list comp ile yapılmalı.
#
# # Beklenen çıktı:
#
# # ['TOTAL_FLAG',
# #  'SPEEDING_FLAG',
# #  'ALCOHOL_FLAG',
# #  'NOT_DISTRACTED',
# #  'NO_PREVIOUS',
# #  'INS_PREMIUM_FLAG',
# #  'INS_LOSSES_FLAG',
# #  'ABBREV_FLAG']


# Dilek

col_flag = [col.upper() + '_FLAG' if "no" not in col else col.upper() for col in df.columns ]
print(col_flag)

# Diger çözüm

import seaborn as sns
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
print("sutun_adlari:")
print(df.columns)
yeni_kolon = [col.upper() + "_FLAG" if "NO" not in col.upper() else col.upper() for col in df.columns]
print("yeni_sutun_adlari:")
print(yeni_kolon)


# ###############################################
# # Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
# ###############################################

og_list = ["abbrev", "no_previous"]
pd.options.display.float_format = '{:.3f}'.format

# # Notlar:
# # Önce yukarıdaki listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# # Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz adını new_df olarak isimlendiriniz.
#
# # Beklenen çıktı:
#
# #    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# # 0 18.800     7.332    5.640          18.048      784.550     145.080
# # 1 18.100     7.421    4.525          16.290     1053.480     133.930
# # 2 18.600     6.510    5.208          15.624      899.470     110.350
# # 3 22.400     4.032    5.824          21.056      827.340     142.390
# # 4 12.000     4.200    3.360          10.920      878.410     165.630
#


import seaborn as sns
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

og_list = ["abbrev", "no_previous"]
df = sns.load_dataset("car_crashes")
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
print(new_cols)
print(new_df.head())









