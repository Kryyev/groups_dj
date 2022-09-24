import datetime

from django.core.validators import MinLengthValidator # noqa
from django.db import models

class Group (models.Model):

    name = models.CharField(str('lorem ipsum dolor'))

    date = models.DateField(default=datetime.date.today(), null=False, blank=True)

    description = models.CharField(verbose_name='Lorem ipsum dolor')

    def __str__(self):
        return f'{self.name} {self.date} {self.description}'
