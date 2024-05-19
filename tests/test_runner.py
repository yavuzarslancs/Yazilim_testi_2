import login_tests
import register_tests
import blog_post_tests
import industry_tests
import image_tests
import test_blog_views
import blog_post_delete_test
import other_tests
import industry_delete_read_more
def menu():
    print("1- Register Testlerini Çalıştır (1 Adet XPath Testi)")
    print("2- Login Testlerini Çalıştır (2 Adet XPath Testi) ")
    print("3- Blog Listleme ve Read More Testlerini Çalıştırır (2 Adet XPath Testi)")
    print("4- Blog Ekleme Testlerini Çalıştırır (Login Required 2 Adet XPath Testi)")
    print("5- Blog Silme Testini Çalıştırır (Login Required 2 Adet XPath Testi)")
    print("6- Endüstri Ekleme Testini Çalıştırır (Login Required 2 Adet XPath Testi)")
    print("7- Endüstri Silme ve Read More Testleri (Login Required 3 Adet XPath Testi)")
    print("8- Karışık Testleri Çalıştırır.  (15 Adet Test)")
    print("9- Image Testlerini Çalıştır")
    print("q- Çıkış")
    choice = input("Lütfen bir seçenek girin: ")

    if choice == '1':
        register_tests.run_tests()
    elif choice == '2':
        login_tests.run_tests()
    elif choice == '3':
        blog_post_tests.run_tests()
    elif choice == '4':
        test_blog_views.test_add_blog_post()
    elif choice == '5':
        blog_post_delete_test.test_delete_blog_post()
    elif choice == '6':
        industry_tests.test_add_industry()   
    elif choice == '7':
        industry_delete_read_more.run_tests() 
    elif choice == '8':
        other_tests.run_tests()
    elif choice == '9':
        image_tests.run_tests()
    elif choice == 'q':
        exit()
    else:
        print("Geçersiz seçenek. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    while True:
        menu()
