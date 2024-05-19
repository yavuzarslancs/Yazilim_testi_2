from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def test_blog_post_listing():
    driver = webdriver.Chrome()
    try:
        # Blog Post Listeleme Testi
        driver.get("http://127.0.0.1:8000/blog.html")
        print("Blog sayfasına yönlendirildi.")
        
        # Preloader'ın kaybolmasını bekleyin
        WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'preloader')))
        
        # Sayfanın yüklenmesini bekleyin
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div/section/div/div[1]/a")))
        
        try:
            assert "Blog Posts" in driver.page_source
            print("Blog Post Listeleme Testi Başarılı")
        except Exception as e:
            print(f"Blog Post Listeleme Testi Başarısız: {e}")
    except Exception as e:
        print(f"Test başarısız: {e}")
    finally:
        driver.quit()

def test_blog_post_read_more():
    driver = webdriver.Chrome()
    try:
        # Blog Post Listeleme Sayfasına Git
        driver.get("http://127.0.0.1:8000/blog.html")
        print("Blog sayfasına yönlendirildi.")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div/section/div/div[1]/a")))

        # Blog Post "Read More" butonuna tıklama testi
        try:
            # Preloader'ın kaybolmasını bekleyin
            WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'preloader')))
            
            read_more_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Read More']")))
            print("Read More düğmesi bulundu.")
            read_more_button.click()
            print("basıldı")
            
            # Yönlendirilmenin başarılı olduğunu kontrol et
            WebDriverWait(driver, 20).until(EC.url_contains("/blog/"))
            print(f"Yönlendirilen URL: {driver.current_url}")
            assert "/blog/" in driver.current_url, "Read More tıklaması sonrası doğru sayfaya yönlendirilmedi."
            print("Blog Post Detay Sayfası Testi Başarılı")
        except Exception as e:
            print(f"Blog Post Detay Sayfası Testi Başarısız: {e}")
    except Exception as e:
        print(f"Test başarısız: {e}")
    finally:
        driver.quit()

def run_tests():
    print("Blog Post Listeleme Testi Başlatılıyor...")
    test_blog_post_listing()
    print("\nBlog Post Detay Sayfası Testi Başlatılıyor...")
    test_blog_post_read_more()

if __name__ == "__main__":
    run_tests()
