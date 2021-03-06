from django.db import models

# Create your models here.


class Role(models.Model):
    r_name = models.CharField(max_length=10)

    # r = models.ForeignKey(User.u)

    class Meta:
        db_table = 'role'


class User(models.Model):
    u_name = models.CharField(max_length=10)
    u_sex = models.BooleanField()
    u_birth = models.DateField()
    u_create_time = models.DateTimeField(auto_now_add=True)
    u_operate_time = models.DateTimeField(auto_now=True)
    u = models.ForeignKey(Role, null=True)

    class Meta:
        db_table = 'user'


class Permission(models.Model):
    p_name = models.CharField(max_length=10)

    p = models.ManyToManyField(Role)

    class Meta:
        db_table = 'permission'

