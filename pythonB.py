# PythonB
import keyword
import re
import string
import time

print("PythonB'ye hoş geldin. Bu konsol uygulamasında "
      "Python ile yapabileceğin tüm temel kodları talep edebiliyor olacaksın.")

degiskenler = {} #Kullanıcının eklediği tüm değişkenler ve değerler bu dict'de tutulacak

delay = 3
while delay > 0:
    time.sleep(1)
    print(delay)
    delay = delay - 1

time.sleep(1)
print("Başlayalım.")

keywords = keyword.kwlist  # python keywordlerinin listesi
dogru_isimlendirme = string.ascii_letters + string.digits + "_"  # değişken adında geçebilecek karakterler

def degisken_ismi():    #Değişken ismi kontrol fonks.
    while True:
        var_name = input("Değişkenin adı:")
        if not var_name:  # değişken adı boş mu?
            print("Değişken adı boş olamaz. Tekrar giriniz.")
            continue
        elif var_name[0].isdigit():  # ilk karakter rakam mı?
            print("Değişken adı rakam ile başlayamaz. Tekrar giriniz.")
            continue
        elif var_name in keywords:  # değişken adı bir keyword mü?
            print("Python anahtar kelimeleri değişken adı olarak kullanılamaz. Tekrar giriniz.")
            continue
        elif "," in var_name:  # değişken adı içerisinde "," geçiyor mu?
            print("Değişken adı özel karakter içeremez. Tekrar giriniz.")
            continue
        elif any(degiskenAdi not in dogru_isimlendirme for degiskenAdi in
                 var_name):  # aksi durumlarda özel karakter içerecektir.
            print("Değişken adı özel karakter içeremez. Tekrar giriniz.")
            continue
        else:
            return var_name

ilk_islem = input("\n1. Değişkenler\n"
              "Hangi alanla ilgili işlem yapmak istiyorsun? Yukarıdaki seçeneklerden birini tuşla:\n")

if ilk_islem == "1":
    degiskenler_islem = input("\nDEĞİŞKENLER... Güzel. Değişkenlerle ilgili ne yapmak istersin?:\n"
          "1. Bir değişken oluştur\n")

    if degiskenler_islem == "1":
        degiskenler_no = input("\n1. Integer (int)\n"
                       "2. Float (float)\n"
                       "3. Kompleks (complex)\n"
                       "4. Karakter Dizisi/String (str)\n"
                       "5. Boolean (bool)\n"
                       "6. Liste (list)\n"
                       "7. Demet (tuple)\n"
                       "8. Aralık/Range (range)\n"
                       "9. Sözlük/Dictionary (dict)\n"
                       "10. Küme (set)\n"
                       "11. Dondurulmuş Küme (frozenset)\n"
                       "Hangi tür bir değişken oluşturmak istersin?:\n")

        if degiskenler_no == "1":   #int
            print("\nInteger... Tabii, önce değişkeninin adını ardından da değerini girebilir misin?")

            int_name = degisken_ismi()

            while True:
                int_value = input("Değişkenin değeri:")
                try:    #girilen değer int mı?
                    int_value = int(int_value)
                    break
                except ValueError:
                    print('Lütfen "int" türünde bir değer giriniz.')

            degiskenler[int_name] = int_value
            print(f"Tebrikler yeni bir int değişkeni oluşturdunuz, {int_name} = {int_value}")

        elif degiskenler_no == "2": #float
            print("\nFloat. Önce değişkeninin adını ardından da değerini girebilir misin?")

            float_name = degisken_ismi()

            while True:
                float_value = input("Değişkenin değeri:")
                virgul_ceviri = float_value.maketrans({',': '.'})  #virgülü noktaya çevirme işlemi
                float_value = float_value.translate(virgul_ceviri)
                try:    #girilen değer float mı?
                    float_value = float(float_value)
                    break
                except ValueError:
                    print('Lütfen "float" türünde bir değer giriniz.')

            degiskenler[float_name] = float_value
            print(f"Tebrikler yeni bir float değişkeni oluşturdunuz, {float_name} = {float_value}")

        elif degiskenler_no == "4": #string
            print('\n"String". Önce değişkeninin adını ardından da değerini girebilir misin?')

            string_name = degisken_ismi()

            string_value = input("Değişkenin değeri:")

            degiskenler[string_name] = string_value
            print(f'Tebrikler yeni bir string değişkeni oluşturdunuz, {string_name} = "{string_value}"')

        elif degiskenler_no == "5": #bool
            print('\n("Boolean") 01000010 01101111 01101111 01101100 01100101 01100001 01101110.\n'
                  'Önce değişkeninin adını ardından da değerini girebilir misin?')

            bool_name = degisken_ismi()

            bool_value = input("Değişkenin değeri:")
            virgul_ceviri = bool_value.maketrans({',': '.'})  # virgülü noktaya çevirme işlemi
            bool_value = bool_value.translate(virgul_ceviri)
            if bool_value == "False" or bool_value == "None" or bool_value == "0" or bool_value == "0.0" or bool_value == "0.00" or bool_value == "0j" or bool_value == "" or bool_value == "range(0)" or bool_value == "[]" or bool_value == "{}":
                bool_value = False  #False olan durumlar

            bool_value = bool(bool_value)

            degiskenler[bool_name] = bool_value
            print(f'Tebrikler yeni bir bool değişkeni oluşturdunuz, {bool_name} = {bool_value}')

        elif degiskenler_no == "6": #list
            print('\nList. Önce değişkeninin adını ardından da değerini girebilir misin?')

            list_name = degisken_ismi()

            list_value = input("Değişkenin değeri:")

            if list_value != "" and list_value[0] == "[" and list_value[-1] == "]": #boş liste girişi ve eğer köşeli parantez ile list girişi yapılırsa parantezleri silmek için
                list_value = list_value[1:-1]

            list_value = list_value.split(",")  #virgüllere ayırarak liste oluşturuyoruz

            degiskenler[list_name] = list_value
            print(f'Tebrikler yeni bir list oluşturdunuz, {list_name} = {list_value}')

        elif degiskenler_no == "7": #tuple
            print('\nTuple/Demet. Önce değişkeninin adını ardından da değerini girebilir misin?')

            tuple_name = degisken_ismi()

            tuple_value = input("Değişkenin değeri:")

            if tuple_value != "" and tuple_value[0] == "(" and tuple_value[-1] == ")": #boş tuple girişi ve eğer parantez ile tuple girişi yapılırsa parantezleri silmek için
                tuple_value = tuple_value[1:-1]

            print(type(tuple_value))

            tuple_value = tuple(tuple_value.split(","))  #virgüllere ayırarak list oluşturuyoruz ve ardından tuple'a dönüştürüyoruz

            print(type(tuple_value))

            degiskenler[tuple_name] = tuple_value
            print(f'Tebrikler yeni bir tuple oluşturdunuz, {tuple_name} = {tuple_value}')

