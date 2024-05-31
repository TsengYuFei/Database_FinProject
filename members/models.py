# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from viewflow.fields import CompositeKey


class Administrator(models.Model):
    a_lname = models.CharField(max_length=5)
    a_fname = models.CharField(max_length=20)
    acc = models.CharField(primary_key=True, max_length=30)
    passwd = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'administrator'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Book(models.Model):
    title = models.CharField(max_length=25)
    isbn = models.CharField(primary_key=True, max_length=13)
    publisher = models.CharField(max_length=20)
    img_id = models.IntegerField(blank=True, null=True)
    b_statu = models.IntegerField()
    aacc = models.ForeignKey(Administrator, models.DO_NOTHING, db_column='Aacc')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book'



class BookAuthor(models.Model):
    ba_lname = models.CharField(primary_key=True, max_length=5)  # The composite primary key (ba_lname, ba_fname, b_isbn) found, that is not supported. The first column is selected.
    ba_fname = models.CharField(max_length=20)
    b_isbn = models.ForeignKey(Book, models.DO_NOTHING, db_column='b_isbn')

    class Meta:
        managed = False
        db_table = 'book_author'
        unique_together = (('ba_lname', 'ba_fname', 'b_isbn'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Mb(models.Model):
    mm = models.OneToOneField('Member', models.DO_NOTHING, db_column='Mm_id', primary_key=True)  # Field name made lowercase. The composite primary key (Mm_id, B_isbn) found, that is not supported. The first column is selected.
    b_isbn = models.ForeignKey(Book, models.DO_NOTHING, db_column='B_isbn')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mb'
        unique_together = (('mm', 'b_isbn'),)


class Member(models.Model):
    phone = models.IntegerField(unique=True)
    m_id = models.CharField(primary_key=True, max_length=10)
    ssn = models.CharField(unique=True, max_length=10)
    m_lname = models.CharField(max_length=5)
    m_fname = models.CharField(max_length=20)
    aacc = models.ForeignKey(Administrator, models.DO_NOTHING, db_column='Aacc')  # Field name made lowercase.
    sex = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member'


class MembersBook(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=25)
    isbn = models.CharField(unique=True, max_length=13)
    author_lname = models.CharField(max_length=5)
    author_fname = models.CharField(max_length=20)
    publisher = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'members_book'


class Ms(models.Model):
    mm = models.OneToOneField(Member, models.DO_NOTHING, db_column='Mm_id', primary_key=True)  # Field name made lowercase. The composite primary key (Mm_id, Ss_id) found, that is not supported. The first column is selected.
    ss = models.ForeignKey('Station', models.DO_NOTHING, db_column='Ss_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ms'
        unique_together = (('mm', 'ss'),)


class Station(models.Model):
    addr = models.CharField(unique=True, max_length=40)
    s_id = models.IntegerField(primary_key=True)
    s_name = models.CharField(max_length=10)
    s_statu = models.IntegerField()
    aacc = models.ForeignKey(Administrator, models.DO_NOTHING, db_column='Aacc')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'station'


class Vb(models.Model):
    vv = models.OneToOneField('Visitor', models.DO_NOTHING, db_column='Vv_id', primary_key=True)  # Field name made lowercase. The composite primary key (Vv_id, B_isbn) found, that is not supported. The first column is selected.
    b_isbn = models.ForeignKey(Book, models.DO_NOTHING, db_column='B_isbn')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vb'
        unique_together = (('vv', 'b_isbn'),)


class Visitor(models.Model):
    v_id = models.IntegerField(primary_key=True)
    aacc = models.ForeignKey(Administrator, models.DO_NOTHING, db_column='Aacc')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'visitor'


class Vs(models.Model):
    vv = models.OneToOneField(Visitor, models.DO_NOTHING, db_column='Vv_id', primary_key=True)  # Field name made lowercase. The composite primary key (Vv_id, Ss_id) found, that is not supported. The first column is selected.
    ss = models.ForeignKey(Station, models.DO_NOTHING, db_column='Ss_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vs'
        unique_together = (('vv', 'ss'),)
# Create your models here.

