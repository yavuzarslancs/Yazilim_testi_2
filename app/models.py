from django.db import models
from django.contrib.auth.models import AbstractUser

class NewUser(AbstractUser):
    # username için varsayılan bir değer atayarak yeni bir model tanımlaması yapılıyor.
    # username alanı benzersizdir ve maksimum 150 karakter uzunluğunda olabilir.
    username = models.CharField(max_length=150, unique=True, default='default_username')

    class Meta:
        db_table = 'new_user'  # Veritabanında kullanılacak tablo adı
        swappable = 'AUTH_USER_MODEL'  # Django'nun varsayılan kullanıcı modelini bu model ile değiştir


class Industry(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title