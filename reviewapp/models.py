# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Course(models.Model):
    course_name = models.CharField(max_length=150)
    course_detail = models.CharField(max_length=500, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class Employee(models.Model):
    user_id = models.IntegerField()
    employee_name = models.CharField(max_length=150)
    address = models.CharField(max_length=254)
    pin_code = models.IntegerField(blank=True, null=True)
    email_id = models.CharField(max_length=254)
    mobile_number = models.CharField(max_length=14)
    birth_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Institute(models.Model):
    institute_name = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    pin_code = models.IntegerField(blank=True, null=True)
    office_mail = models.CharField(max_length=254, blank=True, null=True)
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    website = models.CharField(max_length=150, blank=True, null=True)
    institute_type = models.CharField(max_length=150, blank=True, null=True)
    founded_in = models.IntegerField(blank=True, null=True)
    affiliated_to = models.CharField(max_length=150, blank=True, null=True)
    approved_by = models.CharField(max_length=254, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'institute'


class InstituteCourse(models.Model):
    institute = models.ForeignKey(Institute, models.DO_NOTHING)
    course = models.ForeignKey(Course, models.DO_NOTHING)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'institute_course'


class Review(models.Model):
    institute = models.ForeignKey(Institute, models.DO_NOTHING)
    reviewer = models.ForeignKey('Reviewer', models.DO_NOTHING)
    overall_rating = models.IntegerField()
    review_title = models.CharField(max_length=254, blank=True, null=True)
    merits = models.CharField(max_length=500, blank=True, null=True)
    demerits = models.CharField(max_length=500, blank=True, null=True)
    advice = models.CharField(max_length=500, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'


class Reviewer(models.Model):
    user_id = models.IntegerField()
    reviewer_name = models.CharField(max_length=150)
    email_id = models.CharField(max_length=254)
    profession_status = models.CharField(max_length=150, blank=True, null=True)
    state = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviewer'
