from email.mime import image
from django.db import models

class Post(models.Model):
    '''дані про записи'''
    title = models.CharField('Заголовок запису', max_length=100)
    description = models.TextField('Текст запису')
    author = models.CharField('Імя автора', max_length=100)
    date = models.DateField('Дата публікації')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запис'
        verbose_name_plural = 'Записи'

class Comments(models.Model):
    '''Коментарі'''
    email = models.EmailField()
    name = models.CharField('Імя', max_length=50)
    text_comments = models.TextField('Текст коментаря', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Публікація', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
class Likes(models.Model):
    '''вподобайки'''
    ip = models.CharField('IP-адрес', max_length=100)
    pos = models.ForeignKey(Post, verbose_name='Публікація', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Imege(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')

