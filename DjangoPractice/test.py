import os

if __name__ == '__main__':
    # 引入django配置文件
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoPractice.settings")
    # 启动django
    import django

    django.setup()
    # 操纵数据库
    from app01.models import *

    ret1 = Userinfo.objects.all()
    print(ret1)

    ret2 = Userinfo.objects.filter(name="小明")
    print(ret2)

    ret3 = Userinfo.objects.exclude(name="小明")
    print(ret3)

    ret4 = Userinfo.objects.all().values('name', 'sex')
    print(ret4)

    ret5 = Userinfo.objects.all().values_list('name', 'sex')
    print(ret5)

    ret6 = Userinfo.objects.all().order_by('id')
    print(ret6)

    ret7 = Userinfo.objects.all().order_by('-id')
    print(ret7)

    ret8 = Userinfo.objects.all().order_by('id').reverse()
    print(ret8)

    ret9 = Userinfo.objects.all().first()
    ret10 = Userinfo.objects.all().last()
    print(ret9)
    print(ret10)

    ret11 = Userinfo.objects.all().exists()
    print(ret11)

    ret12 = Userinfo.objects.all().count()
    print(ret12)

    ret13 = Userinfo.objects.all().distinct()
    print(ret13)
