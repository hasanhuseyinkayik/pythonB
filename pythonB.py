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

        if degiskenler_no == "1":
            print("\nInteger... Tabii, önce değişkeninin adını ardından da değerini girebilir misin?")

            keywwords = keyword.kwlist  #python keywordlerinin listesi
            dogru_isimlendirme = string.ascii_letters + string.digits + "_" #değişken adında geçebilecek karakterler

            while True:
                intName = input("Değişkenin adı:")
                if not intName:   #değişken adı boş mu?
                    print("Değişken adı boş olamaz.")
                    continue
                elif intName[0].isdigit():    #ilk karakter rakam mı?
                    print("Değişken adı rakam ile başlayamaz. Tekrar giriniz.")
                    continue
                elif intName in keywwords:  #değişken adı bir keyword mü?
                    print("Python anahtar kelimeleri değişken adı olarak kullanılamaz. Tekrar giriniz.")
                    continue
                elif "," in intName:    #değişken adı içerisinde "," geçiyor mu?
                    print("Değişken adı özel karakter içeremez. Tekrar giriniz.")
                    continue
                elif any(degiskenAdi not in dogru_isimlendirme for degiskenAdi in intName): #aksi durumlarda özel karakter içerecektir.
                    print("Değişken adı özel karakter içeremez. Tekrar giriniz.")
                    continue
                else:
                    break

            while True:
                intValue = input("Değişkenin değeri:")
                try:    #girilen değer int mı?
                    intValue = int(intValue)
                    break
                except ValueError:
                    print('Lütfen "int" türünde bir değer giriniz.')

            degiskenler[intName] = {intValue}
            print(f"Tebrikler yeni bir int değişkeni oluşturdunuz, {intName} = {intValue}")

