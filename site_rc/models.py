from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class Users(models.Model):
    login = models.CharField(max_length=21)
    password = models.CharField(max_length=128)
    number_phone = PhoneNumberField(unique=True)
    real_name = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to='avatar')
    rating = models.IntegerField()
    country_id = models.IntegerField()
    city_id = models.IntegerField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    online = models.BooleanField()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.login


class Country(models.Model):
    name_country = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name_country


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    name_city = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name_city


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return  self.name


class PodCategory(models.Model):
    cat_id = models.ForeignKey(Category, blank=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name


class Products(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.PROTECT)
    name_products = models.CharField(max_length=300)
    condition_products = models.CharField(max_length=50)
    status_products = models.CharField(max_length=30)
    pictures_products = models.ImageField(upload_to='products_pic')
    price = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Цена')
    description_products = models.TextField(max_length=1000)
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT)
    podcat_id = models.ForeignKey(PodCategory, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name_products

class Messages(models.Model):
    from_user = models.CharField(max_length=200)
    to_user = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    text_message = models.CharField(max_length=500)