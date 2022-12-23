from django.db import models

# Create your models here.
class House(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name

class Members(models.Model):
    name = models.CharField(max_length=50)
    house = models.ForeignKey(House, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self) -> str:
        return self.name