# data adında bir sözlük oluşturuluyor. Anahtarlar (key) kelimeler, değerler (value) ise açıklamaları içeriyor.
data = {
    "elma": "Ağaçta yetişen bir meyve",
    "python": "Bir programlama dili",
    "dünya": "Güneş'e en yakın üçüncü gezegen", 
    "ay": "Dünya'nın doğal uydusu", 
    "güneş": "Solar sistemin merkezindeki yıldız"
}

# search_dictionary fonksiyonu, kullanıcıdan bir kelime alır ve bu kelimenin açıklamasını sözlükte arar
def search_dictionary():
    # Kullanıcıdan aramak istediği kelimeyi almak için input() fonksiyonu kullanılır
    # Kullanıcı tarafından girilen kelime küçük harfe dönüştürülerek (lower()) sözlükte arama yapılır
    key = input("Açıklamasını öğrenmek istediğiniz kelimeyi girin: ").lower()

    # .get() metodu ile 'key' (anahtar) kullanılarak sözlükte arama yapılır
    # Eğer anahtar sözlükte varsa, karşılık gelen değeri (value) alır
    value = data.get(key)

    # Eğer 'value' (değer) bulunursa, açıklama ekrana yazdırılır
    if value:
        print("Bulduğumuz açıklama:", value)
    else:
        # Eğer anahtar sözlükte yoksa, kullanıcıya kelimenin bulunamadığını belirten mesaj yazdırılır
        print("Girilen kelime sözlükte bulunamadı.") 

# Fonksiyon çağrılır. Kullanıcıdan kelime girişi yapması istenir.
search_dictionary()
