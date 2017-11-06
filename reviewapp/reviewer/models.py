from __future__ import unicode_literals

from django.db import models
from django.core.validators import validate_email


class Reviewer(models.Model):
    STUDENT = 'ST'
    WORKING = 'WR'
    PROFESSION_STATUS = (
        (STUDENT, 'Student'),
        (WORKING, 'Working'),
    )
    user_id = models.IntegerField()
    reviewer_name = models.CharField(max_length=150)
    email_id = models.EmailField(
        max_length=254,
        unique=True,
        validators=[validate_email]
    )
    profession_status = models.CharField(
        max_length=150,
        choices=PROFESSION_STATUS,
        default=STUDENT,
        blank=True,
        null=True
    )
    state = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviewer'
