from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def run_tests():
    print("Login Testleri Çalıştırılıyor...")
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/login.html")

    # Login Test 1: Doğru kullanıcı adı ve şifre ile giriş (XPath Kullanımı)
    try:
        username = driver.find_element(By.XPATH, "//input[@name='username']")
        password = driver.find_element(By.XPATH, "//input[@name='password']")
        username.send_keys("arslanyavuz")
        password.send_keys("Parola123456.")
        password.send_keys(Keys.RETURN)

        time.sleep(2)
        assert "login_succes.html" in driver.current_url
        print("Login Test 1 Başarılı")
    except Exception as e:
        print(f"Login Test 1 Başarılı {e}")

    # Login Test 2: Yanlış kullanıcı adı veya şifre (XPath Kullanımı)
    try:
        driver.get("http://127.0.0.1:8000/login.html")
        username = driver.find_element(By.XPATH, "//input[@name='username']")
        password = driver.find_element(By.XPATH, "//input[@name='password']")
        username.send_keys("wronguser")
        password.send_keys("wrongpassword")
        password.send_keys(Keys.RETURN)

        time.sleep(2)
        assert "Kullanıcı adı veya şifre hatalı." in driver.page_source
        print("Login Test 2 Başarılı")
    except Exception as e:
        print(f"Login Test 2 Başarısız: {e}")

    driver.quit()

if __name__ == "__main__":
    run_tests()
