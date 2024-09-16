print("Birinci sayıyı girin: ")
num1 = float(input())
print("İkinci sayıyı girin: ")
num2 = float(input())

print("Yapmak istediğiniz işlemi seçin:")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

operation = input()

if operation == '1':
    result = num1 + num2
    print(f"Sonuç: {num1} + {num2} = {result}")

elif operation == '2':
    result = num1 - num2
    print(f"Sonuç: {num1} - {num2} = {result}")

elif operation == '3':
    result = num1 * num2
    print(f"Sonuç: {num1} * {num2} = {result}")

elif operation == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"Sonuç: {num1} / {num2} = {result}")
    else:
        print("Hata: Bir sayıyı sıfıra bölemezsiniz.")

else:
    print("Geçersiz seçim! Lütfen 1, 2, 3 veya 4'ü girin.")
