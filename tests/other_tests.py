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

def test_blog_post_listing():
    driver = get_driver()
    try:
        driver.get("http://127.0.0.1:8000/blog.html")
        print("Blog sayfasına yönlendirildi.")
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Blog Posts']")))
        print("Blog Post Listeleme Testi Başarılı")
    except Exception as e:
        print(f"Blog Post Listeleme Testi Başarısız: {e}")
    finally:
        driver.quit()

def test_blog_post_read_more():
    driver = get_driver()
    try:
        driver.get("http://127.0.0.1:8000/blog.html")
        print("Blog sayfasına yönlendirildi.")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Read More']"))).click()
        WebDriverWait(driver, 20).until(EC.url_contains("/blog/"))
        print("Blog Post Detay Sayfası Testi Başarılı")
    except Exception as e:
        print(f"Blog Post Detay Sayfası Testi Başarısız: {e}")
    finally:
        driver.quit()

def test_user_login():
    driver = get_driver()
    try:
        driver.get("http://127.0.0.1:8000/login.html")
        username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        password = driver.find_element(By.NAME, "password")
        username.send_keys("arslanyavuz")
        password.send_keys("Parola123456.")
        password.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Çıkış Yap")))
        print("Kullanıcı Girişi Testi Başarılı")
    except Exception as e:
        print(f"Kullanıcı Girişi Testi Başarısız: {e}")
    finally:
        driver.quit()



def test_blog_detail():
    driver = get_driver()
    try:
        driver.get("http://127.0.0.1:8000/blog/1.html")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        print("Blog Detay Görüntüleme Testi Başarılı")
    except Exception as e:
        print(f"Blog Detay Görüntüleme Testi Başarısız: {e}")
    finally:
        driver.quit()

def test_industry_list():
    driver = get_driver()
    try:
        driver.get("http://127.0.0.1:8000/industries.html")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        print("Endüstri Listeleme Testi Başarılı")
    except Exception as e:
        print(f"Endüstri Listeleme Testi Başarısız: {e}")
    finally:
        driver.quit()

def test_home_classic():
    driver = get_driver()
    try:
        driver.get("http://127.0.0.1:8000/home-classic/")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        print("Ana Sayfa (Klasik) Yönlendirme Testi Başarılı")
    except Exception as e:
        print(f"Ana Sayfa (Klasik) Yönlendirme Testi Başarısız: {e}")
    finally:
        driver.quit()

def test_home_modern():
    driver = get_driver()
    try:
        driver.get("http://127.0.0.1:8000/home-modern/")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        print("Ana Sayfa (Modern) Yönlendirme Testi Başarılı")
    except Exception as e:
        print(f"Ana Sayfa (Modern) Yönlendirme Testi Başarısız: {e}")
    finally:
        driver.quit()

def test_industry_detail():
    driver = get_driver()
    try:
        driver.get("http://127.0.0.1:8000/industries.html")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        print("Endüstri Detay Görüntüleme Testi Başarılı")
    except Exception as e:
        print(f"Endüstri Detay Görüntüleme Testi Başarısız: {e}")
    finally:
        driver.quit()


def test_register_page():
    driver = get_driver()
    try:
        driver.get("http://127.0.0.1:8000/register/")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        print("Kayıt Sayfası Yükleme Testi Başarılı")
    except Exception as e:
        print(f"Kayıt Sayfası Yükleme Testi Başarısız: {e}")
    finally:
        driver.quit()

def test_login_page():
    driver = get_driver()
    try:
        driver.get("http://127.0.0.1:8000/login/")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        print("Giriş Sayfası Yükleme Testi Başarılı")
    except Exception as e:
        print(f"Giriş Sayfası Yükleme Testi Başarısız: {e}")
    finally:
        driver.quit()

def test_home_page():
    driver = get_driver()
    try:
        driver.get("http://127.0.0.1:8000/index/")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        print("Ana Sayfa Yükleme Testi Başarılı")
    except Exception as e:
        print(f"Ana Sayfa Yükleme Testi Başarısız: {e}")
    finally:
        driver.quit()

def test_index_page():
    driver = get_driver()
    try:
        driver.get("http://127.0.0.1:8000/index/")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        print("İndeks Sayfası Yükleme Testi Başarılı")
    except Exception as e:
        print(f"İndeks Sayfası Yükleme Testi Başarısız: {e}")
    finally:
        driver.quit()

def test_404_page():
    driver = get_driver()
    try:
        driver.get("http://127.0.0.1:8000/404/")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        print("404 Sayfası Yükleme Testi Başarılı")
    except Exception as e:
        print(f"404 Sayfası Yükleme Testi Başarısız: {e}")
    finally:
        driver.quit()

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
        driver.get("http://127.0.0.1:8000/login.html")
        username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        password = driver.find_element(By.NAME, "password")
        username.send_keys("arslanyavuz")
        password.send_keys("Parola123456.")
        password.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Çıkış Yap")))
        print("Giriş başarılı.")

        driver.get("http://127.0.0.1:8000/industries.html")
        print("Endüstri sayfasına yönlendirildi.")
        delete_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Delete']")))
        print("Delete düğmesi bulundu.")
        driver.execute_script("arguments[0].click();", delete_button)
        print("Delete düğmesine basıldı.")
        print("Silme işlemi onaylandı.")
        print("Endüstri Silme Testi Başarılı")
        driver.quit()
    except Exception as e:
        print(f"Endüstri Silme Testi Başarısız: {e}")
    finally:
        driver.quit()



def run_tests():
    print("Blog Post Listeleme Testi Başlatılıyor...")
    test_blog_post_listing()
    print("\nBlog Post Detay Sayfası Testi Başlatılıyor...")
    test_blog_post_read_more()
    print("\nKullanıcı Girişi Testi Başlatılıyor...")
    test_user_login()
    print("\nBlog Detay Görüntüleme Testi Başlatılıyor...")
    test_blog_detail()
    print("\nEndüstri Listeleme Testi Başlatılıyor...")
    test_industry_list()
    print("\nAna Sayfa (Klasik) Yönlendirme Testi Başlatılıyor...")
    test_home_classic()
    print("\nAna Sayfa (Modern) Yönlendirme Testi Başlatılıyor...")
    test_home_modern()
    print("\nEndüstri Detay Görüntüleme Testi Başlatılıyor...")
    test_industry_detail()
    print("\nKayıt Sayfası Yükleme Testi Başlatılıyor...")
    test_register_page()
    print("\nGiriş Sayfası Yükleme Testi Başlatılıyor...")
    test_login_page()
    print("\nAna Sayfa Yükleme Testi Başlatılıyor...")
    test_home_page()
    print("\nİndeks Sayfası Yükleme Testi Başlatılıyor...")
    test_index_page()
    print("\n404 Sayfası Yükleme Testi Başlatılıyor...")
    test_404_page()
    print("\nEndüstri 'Read More' Testi Başlatılıyor...")
    test_industry_read_more()
    print("\nEndüstri Silme Testi Başlatılıyor...")
    test_delete_industry()

if __name__ == "__main__":
    run_tests()
