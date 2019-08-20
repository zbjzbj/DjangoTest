import os

if __name__ == '__main__':
    # 引入django配置文件
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoPractice.settings")
    # 启动django
    import django

    django.setup()
    # 操纵数据库
    from app01.models import *

    # ret1 = Userinfo.objects.all()
    # print(ret1)
    #
    # ret2 = Userinfo.objects.filter(name="小明")
    # print(ret2)
    #
    # ret3 = Userinfo.objects.exclude(name="小明")
    # print(ret3)
    #
    # ret4 = Userinfo.objects.all().values('name', 'sex')
    # print(ret4)
    #
    # ret5 = Userinfo.objects.all().values_list('name', 'sex')
    # print(ret5)
    #
    # ret6 = Userinfo.objects.all().order_by('id')
    # print(ret6)
    #
    # ret7 = Userinfo.objects.all().order_by('-id')
    # print(ret7)
    #
    # ret8 = Userinfo.objects.all().order_by('id').reverse()
    # print(ret8)
    #
    # ret9 = Userinfo.objects.all().first()
    # ret10 = Userinfo.objects.all().last()
    # print(ret9)
    # print(ret10)
    #
    # ret11 = Userinfo.objects.all().exists()
    # print(ret11)
    #
    # ret12 = Userinfo.objects.all().count()
    # print(ret12)
    #
    # ret13 = Userinfo.objects.all().distinct()
    # print(ret13)
    #
    # ret14 = Userinfo.objects.filter(id__lt=3)
    # print(ret14)
    #
    # ret15 = Userinfo.objects.filter(id__lte=3)
    # print(ret15)
    #
    # ret16 = Userinfo.objects.filter(id__in=[4, 5])
    # print(ret16)
    #
    # ret17 = Userinfo.objects.filter(id__range=[2, 3])
    # print(ret17)
    #
    # ret18 = Userinfo.objects.filter(name__startswith="小")
    # print(ret18)
    #
    # ret19 = Userinfo.objects.filter(name__endswith="仔")
    # print(ret19)
    #
    # ret20 = Userinfo.objects.filter(name__contains="明")
    # print(ret20)
    #
    # ret21 = Userinfo.objects.filter(birthday__year=2019)  # Date时间类型特有的年月日判断
    # print(ret21)
    #
    # ret22 = Userinfo.objects.filter(name__isnull=True)
    # print(ret22)



    ##################  基于对象的查询  ####################
    """
    1. 正向查
    对象.关联字段.属性
            # 查询第一本书关联的出版社名称
            book_obj = Book.objects.first()
            ret = book_obj.publisher.name
            print(ret)

    2. 反向查
        1. 默认不设置related_name属性
            1. 查找的对象是多个的时候（一对多或多对多时）
                publisher_obj.book_set.all()  # 一对多(ForeignKey)和多对多(ManyToManyField)的反向查询：类名_set
                publisher_obj.book_set.filter(price__lt=34)

            2. 查找的对象时一个的时候（一对一）
                author_info_obj.author.name  # 一对一(OneToOneField)的反向查询：类名
                
        2.设置related_name='books'属性(publisher = models.ForeignKey(to='Publisher', related_name='books'))
            # 查询明哥出版社出版的所有书
            publisher_obj = Publisher.objects.get(name='明哥出版社')
            publisher_obj.books.all()
    """

    # book_obj = Book.objects.first()
    # ret1 = book_obj.publisher.name
    # print(ret1)
    #
    # ret1 = book_obj.author_set.all()    # 没有设置related_name的反向查询：类名_set
    # print(ret1)
    #
    #
    # publisher_obj = Publisher.objects.first()
    # ret2 = publisher_obj.books.all()  # 设置了related_name的反向查询：使用related_name定义的关键字即可
    # print(ret2)
    #
    # ret3 = publisher_obj.books.filter(price__lt=34)
    # print(ret3)


    ###############  基于QuerySet的查询(__表示跨表查询)  ##########
    """
    1. 正向查
        Book.objects.filter(id=1).values_list('publisher__name')

    2. 反向查
        1. 默认不设置related_name属性,默认就用类名的小写
            Publisher.objects.filter(id=1).values_list('book__price')
        2. 设置related_name='books'属性
            Publisher.objects.filter(id=1).values_list('books__price')
    3. related_query_name = 'hello'
        在关联的字段参数设置了related_query_name = 'hello'后，反向查找就不需要使用表名，而是直接使用"hello"
    """

    # 热身：普通的values的使用
    # 查询第一本书的名称
    ret = Book.objects.filter(id=2).values('title')
    print(ret)

    # 使用：外键基于QuerySet跨表查询
    # 查询第一本书关联的出版社名称(__表示跨表查询)(正向查找)
    # valuse('publisher')表示通过外键找到了publisher表，__表示跨表取到publisher表的字段的值
    ret = Book.objects.filter(id=2).values('publisher__name')
    print(ret)

    # 反向查找
    # 查询id=2的出版社的所有书的名称和价格
    ret = Publisher.objects.filter(id=2).values_list('books__title', 'books__price')
    print(ret)

    # 一对一基于QuerySet跨表查询
    # 查询id=2的作者婚否(正向查找)
    ret = Author.objects.filter(id=2).values('info__is_marry')
    print(ret)

    # 查找住在深圳的作者的姓名(反向查找)
    ret = AuthorInfo.objects.filter(city='惠州').values('author__name')
    print(ret)

    # 多对多基于QuerySet跨表查询
    # 查询id=2的作者关联的所有数据的名称和价格(正向查找)
    ret = Author.objects.filter(id=2).values('books__title', 'books__price')
    print(ret)

    # 查找id=2的作者的名字(反向查找)
    ret = Book.objects.filter(id=2).values('author__name')
    print(ret)

    # 链式查询
    # 查找id=2的书的作者的城市
    ret = Book.objects.filter(id=2).values('author__info__city')
    print(ret)