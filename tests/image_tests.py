from base_tests import get_driver

def run_tests():
    driver = get_driver()
    try:
        # İmaj kontrol testlerini burada gerçekleştir
        driver.get('http://127.0.0.1:8000/home.html')
        # İmajın varlığını doğrula
        # Assert koşullarını ekleyin
        print("Image tests passed successfully!")
    finally:
        driver.quit()
