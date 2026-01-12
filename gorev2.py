# count_vowels fonksiyonu, kullanıcıdan alınan kelimede sesli harflerin sayısını hesaplar
def count_vowels():
    # Kullanıcıdan bir kelime alınır ve tüm harfler küçük harfe dönüştürülür (Türkçe karakterlere duyarlı)
    user_input = input("Bir kelime girin: ").lower()  # Kullanıcı girişini küçük harfe dönüştürme
    
    # Türkçe alfabesinde bulunan sesli harfler 'aeıioöuü' stringi olarak tanımlanır
    vowels = 'aeıioöuü'
    
    # Kelimedeki sesli harflerin sayısını hesaplamak için sum() fonksiyonu kullanılır
    # Her bir harf için, harfin sesli harfler listesinde olup olmadığı kontrol edilir
    count = sum(1 for char in user_input if char in vowels)  # Sesli harflerin sayısını toplama
    
    # Sonuç olarak, kelimedeki sesli harf sayısı ekrana yazdırılır
    print(f"Kelimedeki sesli harf sayısı: {count}")

# count_vowels fonksiyonu çağrılır ve kullanıcıdan kelime girmesi istenir
count_vowels()
