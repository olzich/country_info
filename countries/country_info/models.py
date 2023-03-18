from django.db import models
from django.urls import reverse

class Continents(models.Model):
    continent = models.CharField(max_length=40, db_index=True)
    describe = models.CharField(max_length=255, db_index=True, null=True)

    def __str__(self):
        return self.continent

    def get_absolute_url(self):
        return reverse('inform', kwargs={'name': self.continent})