from django.db import models

# Create your models here.
class MyUsers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_num = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.first_name