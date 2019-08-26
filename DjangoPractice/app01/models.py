from django.db import models


# Create your models here.

class Test(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=20)
    # 有choices参数的字段，在views中可以使用：get_字段名_display()  --> 获取choice字段的显示值
    # 例如：get_sex_display() --> 保密
    sex = models.IntegerField(choices=[(1, '男'), (2, '女'), (3, '保密')], default=3)
    bool_field = models.BooleanField()
    text_field = models.TextField()
    email_field = models.EmailField()
    ip_field = models.GenericIPAddressField()
    uuid_field = models.UUIDField()
    image_field = models.ImageField(upload_to="image/%Y-%m")
    datetime_field = models.DateTimeField(auto_now_add=True)  # 当前数据的创建时间
    date_field = models.DateField(auto_now=True)  # 当前数据的最后修改时间
    time_field = models.TimeField()
    float_field = models.FloatField()
    decimal_Field = models.DecimalField(max_digits=2, decimal_places=2)

    class Meta:
        db_table = "test"  # 定义表名，若无定义，默认使用：app名_类名(小写)
        unique_together = (('tag', 'sex'),)  # 联合唯一索引
        index_together = (("ip_field", "uuid_field"),)  # # 联合索引


class Userinfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=12)
    password = models.CharField(max_length=18)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    publisher = models.ForeignKey(to='Publisher', related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=12)  # 姓名
    gender = models.SmallIntegerField(choices=((1, '男'), (2, '女'), (3, '保密')), default=3)  # 性别
    books = models.ManyToManyField(to='Book')  # 作品
    info = models.OneToOneField(to='AuthorInfo')  # 详细信息

    def __str__(self):
        return self.name


# 作者详细信息表
class AuthorInfo(models.Model):
    city = models.CharField(max_length=12)  # 住址
    is_marry = models.BooleanField()  # 婚否
    income = models.BigIntegerField()  # 收入


class Employee(models.Model):
    name = models.CharField(max_length=12)
    age = models.IntegerField()
    salary = models.IntegerField()
    province = models.CharField(max_length=12)
    dept = models.CharField(max_length=12)
