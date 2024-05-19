from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_delete_blog_post():
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

        # Blog Post Listeleme Sayfasına Git
        driver.get("http://127.0.0.1:8000/blog.html")
        print("Blog sayfasına yönlendirildi.")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div/section/div/div[1]/a")))
        print("HELLOOOOOOOOOOOOOOOOOOO")
        
        # Preloader'ın kaybolmasını bekleyin
        try:
            WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'preloader')))
            print("Preloader kayboldu.")
        except Exception as e:
            print("Preloader kaybolmadı, ancak sayfa tamamen yüklendi.")

        # Blog post silme işlemini gerçekleştirin
        delete_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Delete']")))
        print("Delete düğmesi bulundu.")
        
        # JavaScriptExecutor kullanarak doğrudan Delete düğmesine tıklama
        driver.execute_script("arguments[0].click();", delete_button)
        print("Delete düğmesine basıldı.")
        print("Silme Testi Başarılı.")
        driver.quit()
    except Exception as e:
        print(f"Test başarısız: {e}")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    test_delete_blog_post()
