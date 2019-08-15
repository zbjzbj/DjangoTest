from django.db import models


# Create your models here.
class Userinfo(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    publisher = models.ForeignKey(to='Publisher')

    def __str__(self):
        return self.title


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)  # 作者名称
    age = models.IntegerField()  # 年龄
    book = models.ManyToManyField(to='Book')  # ORM帮我们自动创建的第三张表(用于多对多查询)(但是Author表不会生成book字段)

    def __str__(self):
        return self.name
