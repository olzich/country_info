from django.db import models

class Continents(models.Model):
    continent = models.CharField(max_length=40, db_index=True)

    def __str__(self):
        return self.continent
