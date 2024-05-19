from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    return driver

def login(driver):
    driver.get("http://127.0.0.1:8000/login.html")
    username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    username.send_keys("arslanyavuz")
    password.send_keys("Parola123456.")
    password.send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Çıkış Yap")))
    print("Giriş başarılı.")

def test_industry_read_more():
    driver = get_driver()
    try:
        driver.get("http://127.0.0.1:8000/industries.html")
        print("Endüstri sayfasına yönlendirildi.")
        read_more_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Read More']")))
        read_more_button.click()
        WebDriverWait(driver, 20).until(EC.url_contains("/industries/"))
        print(f"Yönlendirilen URL: {driver.current_url}")
        assert "/industries/" in driver.current_url, "Read More tıklaması sonrası doğru sayfaya yönlendirilmedi."
        print("Endüstri Detay Sayfası Testi Başarılı")
    except Exception as e:
        print(f"Endüstri Detay Sayfası Testi Başarısız: {e}")
    finally:
        driver.quit()

def test_delete_industry():
    driver = get_driver()
    try:
        login(driver)
        driver.get("http://127.0.0.1:8000/industries.html")
        print("Endüstri sayfasına yönlendirildi.")
        
        delete_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Delete']")))
        print("Delete düğmesi bulundu.")
        
        driver.execute_script("arguments[0].click();", delete_button)
        print("Delete düğmesine basıldı.")
        print("Endüstri Silme Testi Başarılı")
        driver.quit()
        
    except Exception as e:
        print(f"Endüstri Silme Testi Başarısız: {e}")
    finally:
        driver.quit()

def run_tests():
    print("Endüstri 'Read More' Testi Başlatılıyor...")
    test_industry_read_more()
    print("\nEndüstri Silme Testi Başlatılıyor...")
    test_delete_industry()

if __name__ == "__main__":
    run_tests()
