from django.contrib.auth.models import User
from django.db import models


def user_directory_path(instance, filename):
    return f'user_{instance.owner.id}/{filename}'


class Foto(models.Model):
    title = models.CharField('Название фотографии', max_length=100, blank=True)
    geolocation = models.CharField('Место выполнения фотографии', max_length=50, blank=True)
    date = models.DateField('Дата фото', help_text='формат дд-мм-гггг', null=True, blank=True)
    names = models.CharField('Именна людей на фотографии', max_length=100, blank=True)
    image = models.ImageField('Фотография',upload_to='media')
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE,  verbose_name='владелец')

    def __str__(self):
        return self.title
