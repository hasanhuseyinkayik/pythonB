# PythonB
import keyword
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
            print("Değişken adı boş olamaz.")
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

            degiskenler[int_name] = {int_value}
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

            degiskenler[float_name] = {float_value}
            print(f"Tebrikler yeni bir float değişkeni oluşturdunuz, {float_name} = {float_value}")