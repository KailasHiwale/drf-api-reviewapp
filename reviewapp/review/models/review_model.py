from __future__ import unicode_literals

from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator)


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    institute = models.ForeignKey('Institute')
    reviewer = models.ForeignKey('reviewer.Reviewer')
    overall_rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        blank=True,
        null=True)
    review_title = models.CharField(max_length=254, blank=True, null=True)
    merits = models.CharField(max_length=500, blank=True, null=True)
    demerits = models.CharField(max_length=500, blank=True, null=True)
    advice = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'
