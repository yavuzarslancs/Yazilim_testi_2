from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_blog_post():
    driver = webdriver.Chrome()

    try:
        # Giriş yap
        driver.get("http://127.0.0.1:8000/login.html")
        username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
        password = driver.find_element(By.XPATH, "//input[@name='password']")
        username.send_keys("arslanyavuz")
        password.send_keys("Parola123456.")
        password.send_keys(Keys.RETURN)

        # Giriş sonrası belirgin bir öğenin yüklenmesini bekle (örneğin, "Çıkış Yap" bağlantısı)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Çıkış Yap")))
        print("Giriş başarılı.")

        # Blog post ekleme sayfasına git
        driver.get("http://127.0.0.1:8000/blog/add/")
        print("Blog post ekleme sayfasına gidildi.")

        # Form alanlarının görünür olduğundan emin ol
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='title']")))
        
        # Form alanlarını bul ve doldur
        title = driver.find_element(By.XPATH, "//input[@name='title']")
        content = driver.find_element(By.XPATH, "//textarea[@name='content']")
        
        title.send_keys("Yeni Blog Yazısı")
        content.send_keys("Bu bir blog yazısı içeriğidir.")
        driver.find_element(By.XPATH, "//button[text()='Save']").click()

        # Başarılı Ekleme Kontrolü
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div/header/nav/div/div[1]/ul/li[2]/ul/li[2]/a")))
        assert "Yeni Blog Yazısı" in driver.page_source, "Blog yazısı eklenemedi."
        print("Blog Post Ekleme Testi Başarılı")
    
    except Exception as e:
        print(f"Test başarısız: {e}")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    test_add_blog_post()
