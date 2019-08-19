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
    birthday = models.DateTimeField(verbose_name='生日', null=True, auto_now_add=True)
    sex = models.IntegerField(choices=[(1, '男'), (2, '女'), (3, '保密')], default=3)

    def __str__(self):
        return self.name
