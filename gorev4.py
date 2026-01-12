# Kayıtlı kullanıcılar
users = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3",
    "user4": "password4",
    "user5": "password5",
}

# Kayıtlı kullanıcıları listeleyelim
print("Sistemde kayıtlı olan kullanıcılar:")
for username, password in users.items():
    print(f"Kullanıcı Adı: {username}, Şifre: {password}")

print("\nYeni bir kullanıcı ekleniyor.")
username = input("Yeni kullanıcının kullanıcı adını girin: ")

# Kullanıcı adı kontrolü: Eğer kullanıcı adı zaten varsa, yeni kullanıcı eklenemez
if username in users:
    print("Bu kullanıcı adı zaten mevcut! Lütfen başka bir kullanıcı adı seçin.")
else:
    password = input("Yeni kullanıcının şifresini girin: ")
    users[username] = password  # Yeni kullanıcıyı ekliyoruz
    print(f"Yeni kullanıcı {username} başarıyla eklendi.")

# Yeni kullanıcı eklendikten sonra tüm kullanıcıların listesi
print("\nYeni kullanıcı eklendikten sonra tüm kullanıcıların listesi:")
for username, password in users.items():
    print(f"Kullanıcı Adı: {username}, Şifre: {password}")
