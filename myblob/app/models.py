from __future__ import unicode_literals

from django.db import models
from django.contrib import admin


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=80)
    sex = models.CharField(max_length=2)
    reg_time = models.DateTimeField()


class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    create_time = models.DateTimeField()
    author = models.CharField(max_length=20)
    add_zan = models.IntegerField(default='1')


class Visitor(models.Model):
    ip = models.CharField(max_length=20)
    visit_time = models.DateTimeField()


class Liuyan(models.Model):
    text = models.TextField()


class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'create_time', 'author')     # list


admin.site.register(Article, ContactAdmin)
# admin.site.register(Visitor)


# class Publisher(models.Model):
#     name = models.CharField(max_length=30)
#     address = models.CharField(max_length=50)
#     city = models.CharField(max_length=60)
#     state_province = models.CharField(max_length=30)
#     country = models.CharField(max_length=50)
#     website = models.URLField()
#
#
# class Author(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=40)
#     email = models.EmailField()
#
#
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     authors = models.ManyToManyField(Author)
#     publisher = models.ForeignKey(Publisher)
#     publication_date = models.DateField()
