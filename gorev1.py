# check_adulthood fonksiyonu, kullanıcının yaşını alır ve yetişkin olup olmadığını kontrol eder
def check_adulthood():
    # Kullanıcıdan yaş bilgisini almak için input() fonksiyonu kullanılır
    age_input = input("Yaşınızı girin: ")
    
    # Girilen değerin bir sayı olup olmadığını kontrol ederiz
    if age_input.isdigit():
        # Eğer girilen değer sayısal bir değerse, bunu int() ile tam sayıya çeviririz
        age = int(age_input)
        
        # Eğer yaş 18 veya daha büyükse, yetişkin olduğunu belirten mesaj yazdırılır
        if age >= 18:
            print("Yetişkinsiniz!")
        else:
            # Yaş 18'den küçükse, yetişkin olunmadığı belirtilir
            print("Yetişkin değilsiniz!")
    else:
        # Eğer yaş bir sayı değilse, kullanıcıyı doğru formatta giriş yapması için uyarırız
        print("Lütfen yaşınızı girin. Sadece sayı kullanın!")

# check_adulthood fonksiyonu çağrılır, böylece yaş kontrolü başlar
check_adulthood()
