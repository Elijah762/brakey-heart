from datetime import datetime

from django.db import models


class BrakeData(models.Model):
    force = models.DecimalField(decimal_places=2, max_digits=10)
    percent = models.DecimalField(decimal_places=2, max_digits=10)
    ts = models.DateTimeField()


class PiData(models.Model):
    x_acc = models.DecimalField(decimal_places=2, max_digits=5)
    y_acc = models.DecimalField(decimal_places=2, max_digits=5)
    z_acc = models.DecimalField(decimal_places=2, max_digits=5)
    ts = models.DateTimeField(default=datetime.now(), blank=True)




