from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Фото профиля')
    phone_number = models.CharField(max_length=12, blank=True, null=True, verbose_name='Номер телефона')

    class Meta:
        db_table = "user"
        verbose_name = "пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return self.username
