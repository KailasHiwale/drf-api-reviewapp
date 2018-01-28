from __future__ import unicode_literals

from django.db import models


class InstituteCourse(models.Model):
    """Model to manage courses available for institute"""
    id = models.AutoField(primary_key=True)
    institute = models.ForeignKey('Institute', models.DO_NOTHING)
    course = models.ForeignKey('Course', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'institute_course'

