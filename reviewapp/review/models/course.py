"""
Use unicode_literals when back-porting new or existing Python 3 code
to Python 2/3 than when porting existing Python 2 code to 2/3
"""
from __future__ import unicode_literals

from django.db import models


class Course(models.Model):
    """Model for course deatils"""
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=150)
    course_detail = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'course'
