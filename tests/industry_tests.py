from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_industry():
    driver = webdriver.Chrome()
    
    # Giriş yap
    driver.get("http://127.0.0.1:8000/login.html")
    username = driver.find_element(By.XPATH, "//input[@name='username']")
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    username.send_keys("arslanyavuz")
    password.send_keys("Parola123456.")
    password.send_keys(Keys.RETURN)
    
    # Giriş sonrası belirgin bir öğenin yüklenmesini bekle (örneğin, kullanıcı adı)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div/header/nav/div/ul/li[2]/a")))  # Giriş sonrası görünür olacak bir öğeyi bekleyin
    
    # Endüstri ekleme sayfasına git
    driver.get("http://127.0.0.1:8000/industries/add/")
    
    # Form alanlarının görünür olduğundan emin ol
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='name']")))
    
    # Form alanlarını bul ve doldur
    name = driver.find_element(By.XPATH, "//input[@name='name']")
    description = driver.find_element(By.XPATH, "//textarea[@name='description']")
    
    name.send_keys("Yeni Industry")
    description.send_keys("Bu bir industry açıklamasıdır.")
    driver.find_element(By.XPATH, "//button[text()='Kaydet']").click()

    # Başarılı Ekleme Kontrolü
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div[1]/header/nav/div/div[1]/ul/li[2]/ul/li[2]/a")))
    assert "Yeni Industry" in driver.page_source, "Endüstri eklenemedi."
    print("Industry Testleri Başarılı")
    driver.quit()



if __name__ == "__main__":
    test_add_industry()
    
    
