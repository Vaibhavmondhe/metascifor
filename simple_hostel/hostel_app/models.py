from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15)
    room_number = models.CharField(max_length=10)
    check_in_date = models.DateField()
    fee_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - Room {self.room_number}"
