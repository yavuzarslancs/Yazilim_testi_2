from selenium import webdriver

def get_driver():
    # WebDriver örneğini başlat
    driver = webdriver.Chrome()
    return driver