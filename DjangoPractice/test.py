import os

if __name__ == '__main__':

    # 引入django配置文件
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoPractice.settings")
    # 启动django
    import django
    django.setup()
    # 操纵数据库
    from app01.models import *

    # res = Publisher.objects.all()
    # Publisher.objects.create(name="UZI出版社")

    author_obj = Author.objects.get(id=1)
    books = author_obj.book.all()

    print(books)
