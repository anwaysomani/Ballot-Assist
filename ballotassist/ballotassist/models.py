from __future__ import unicode_literals
from django.db import models

class ballot_record(models.Model):
    ballot_id = models.IntegerField(primary_key=True)
    balloters_name = models.CharField(max_length=100)
    ballotees_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Ballot Record"
        verbose_name_plural = "Ballot Records"

