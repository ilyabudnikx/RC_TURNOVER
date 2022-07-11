from django.contrib import admin

from .models import *


# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_country')


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name_products', 'price', 'category_id', 'podcat_id')


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'country_id', 'name_city')


class CatAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PodCatAdmin(admin.ModelAdmin):
    list_display = ('cat_id', 'name',)


admin.site.register(Users)
admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Category, CatAdmin)
admin.site.register(PodCategory, PodCatAdmin)
