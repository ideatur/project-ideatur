from django.db import models
from datetime import datetime

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    communication_methods = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class NewTour(models.Model):
    title = models.CharField("Назва туру", max_length=100)
    country = models.CharField("Країна", max_length=50)
    city = models.CharField("Місто", max_length=50)
    CHOICES = (
        ('бориспіль','Київ-Бориспіль'),
        ('жуляни', 'Київ-Жуляни')
        )
    airport_from = models.CharField("Виліт з", choices=CHOICES, max_length=100)
    to_airport = models.CharField("До аеропорту ", max_length=100, default='default')
    hotel = models.CharField("Готель", max_length=100)
    ROOM_CHOICES = (
        ('стандарт','Стандарт'),
        ('все всключено', 'все вклюено'),
        ('королівський люкс', 'Королівський люкс')
        )
    rooms_class =  models.CharField("Тип готельного номеру", choices=ROOM_CHOICES, max_length=100, default='default')
    nights = models.IntegerField("Кількість ночей")
    persons = models.IntegerField("Кількість людей")
    price = models.IntegerField("Ціна")
    tour_photo = models.ImageField("Постер", upload_to="photos/%Y/%m/%d/")
    is_hot_tour = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Нові тури"
        verbose_name_plural = "Нові тури"

