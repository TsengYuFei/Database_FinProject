from django.db import models

# Create your models here.

class Administrator(models.Model):
    # 管理員
    # Model: 名、姓、帳號、密碼
    fname = models.CharField(max_length=20, verbose_name='名')
    lname = models.CharField(max_length=5, verbose_name='姓')
    acc = models.CharField(max_length=30, unique=True, verbose_name='帳號')
    passwd = models.CharField(max_length=30, verbose_name='密碼')

    # 顯示管理員: "名 姓"
    def __str__(self):
        return f"{self.fname} {self.lname}"

class Member(models.Model):
    # 會員
    # Model: 電話、身分證、名、姓、性別
    # 性別選擇
    sex_type = [
        ("M", "男性"),
        ("F", "女性"),
    ]
    phone = models.CharField(max_length=10, unique=True, verbose_name='電話')
    ssn = models.CharField(max_length=10, unique=True, verbose_name='身分證')
    fname = models.CharField(max_length=20, verbose_name='名')
    lname = models.CharField(max_length=5, verbose_name='姓')
    sex = models.CharField(max_length=1, choices=sex_type, null=True, verbose_name='性別')

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Station(models.Model):
    # 站點
    # Model: 地址、站名、狀態
    # 狀態選擇
    statu_type = [
        ("0", "維修中"),
        ("1", "營運中"),
    ]
    addr = models.CharField(max_length=40, unique=True, verbose_name='地址')
    name = models.CharField(max_length=10, verbose_name='站名')
    statu = models.CharField(max_length=1, choices=statu_type, verbose_name='狀態')

    def __str__(self):
        return self.name

class Author(models.Model):
    # 作者
    # Model: 名、姓
    fname = models.CharField(max_length=20, verbose_name='名')
    lname = models.CharField(max_length=5, verbose_name='姓')

    def __str__(self):
        # 顯示作者: "名 姓"
        return f"{self.fname} {self.lname}"

class Publisher(models.Model):
    # 出版社
    # Model: 出版社名稱
    name = models.CharField(max_length=20, verbose_name='出版社名稱')

    def __str__(self):
        return self.name

class Book(models.Model):
    # 書籍
    # Model: 書名、ISBN、作者、出版社、書本封面、狀態、目前借閱會員、目前所在站點(後二依狀態判定)
    # 狀態選擇
    statu_type = [
        ("0", "站內"),
        ("1", "借出"),
    ]
    title = models.CharField(max_length=25, verbose_name='書名')
    isbn = models.CharField(max_length=13, unique=True, verbose_name='ISBN')
    # 作者可以用多值
    author = models.ManyToManyField(Author, related_name='books', verbose_name='作者')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books', verbose_name='出版社')
    img = models.ImageField(upload_to='book_images/', null=True, verbose_name='書本封面')
    statu = models.CharField(max_length=1, choices=statu_type, default="0", verbose_name='狀態')
    # 依statu判斷查看/更改會員或站點
    member = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, related_name='books', verbose_name='會員')
    station = models.ForeignKey(Station, on_delete=models.CASCADE, null=True, related_name='books', verbose_name='站點')

    def __str__(self):
        return self.title