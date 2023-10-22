from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class GenderChoices(models.TextChoices):
    Male = 'M'
    Female = 'F'
    Other = 'O'


class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MaxValueValidator(50), MinValueValidator(5)])
    gender = models.CharField(choices=GenderChoices.choices, max_length=10)
    register_number = models.IntegerField(unique=True)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
