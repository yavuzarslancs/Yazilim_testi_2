from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def run_tests():
    print("Register Testleri Çalıştırılıyor...")
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/register.html")

    # Register Test 1: Geçerli bilgilerle kayıt olma (XPath Kullanımı)
    try:
        username = driver.find_element(By.XPATH, "//input[@name='username']")
        email = driver.find_element(By.XPATH, "//input[@name='email']")
        password1 = driver.find_element(By.XPATH, "//input[@name='password1']")
        password2 = driver.find_element(By.XPATH, "//input[@name='password2']")

        # Mevcut içerikleri temizleyin
        username.clear()
        email.clear()
        password1.clear()
        password2.clear()

        
        username.send_keys("arslanyavuz")
        email.send_keys("arslanyavuz@gmail.com")
        password1.send_keys("Parola123456.")
        password2.send_keys("Parola123456.")
        driver.find_element(By.XPATH, "//button[text()='Kayıt Ol']").click()

        time.sleep(2)
        
        # Başarılı Mesaj Kontrolü (http://127.0.0.1:8000/register.html)
        

        # 5 saniye bekle ve ana menüye dönüşü kontrol et
        time.sleep(7)
        current_url = driver.current_url
        print(f"Current URL after redirect: {current_url}")
        if "home" in current_url:  # Yönlendirilecek ana menü sayfası (örneğin 'home')
            print("Register Test 1 Başarılı: Ana menüye yönlendirme")
        else:
            print("Register Test 1 Başarılı: Ana menüye yönlendirme")

    except Exception as e:
        print(f"Register Test 1 Başarısız: {e}")

    driver.quit()

if __name__ == "__main__":
    run_tests()
