class Calculator:
    def add(self, x, y):
        """iki sayıyı toplama"""
        return x + y
    
    def subtract(self, x, y):
        """x'ten y'yi çıkarma"""
        return x - y
    
    def multiply(self, x, y):
        """İki sayıyı çarpma"""
        return x * y
    
    def divide(self, x, y):
        """x'i y'ye bölme"""
        if y == 0:
            raise ValueError("Sıfıra bölünemiyor")
        return x / y

def get_number_input(prompt):
    """Hata işleme ile kullanıcıdan sayısal girdi alma"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz!")

def main():
    calc = Calculator()
    operations = {
        '1': ('Toplama', calc.add),
        '2': ('Çıkarma', calc.subtract),
        '3': ('Çarpma', calc.multiply),
        '4': ('Bölme', calc.divide)
    }
    
    while True:
        print("\nBasit Hesap Makinesi")
        print("--------------------")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("5. Çıkış")
        
        choice = input("\nİşlem seçiniz (1-5): ")
        if choice == '5':
            print("Hesap makinesi kapatılıyor...")
            break
        
        if choice not in operations:
            print("Geçersiz seçim!")
            continue
        
        num1 = get_number_input("İlk sayıyı giriniz: ")
        num2 = get_number_input("İkinci sayıyı giriniz: ")
        
        try:
            operation_name, operation_func = operations[choice]
            result = operation_func(num1, num2)
            print(f"\nSonuç: {result}")
        except ValueError as e:
            print(f"Hata: {e}")
        except Exception as e:
            print(f"Beklenmeyen bir hata oluştu: {e}")

if __name__ == "__main__":
    main()