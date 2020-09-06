from django.db import models

class User(models.Model):
    name = models.CharField(verbose_name='name', db_index=True, max_length=64)
    email = models.EmailField(max_length=100, blank=False)
    user_id = models.IntegerField(blank=True)
