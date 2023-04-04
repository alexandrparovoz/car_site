from django.db import models


class WorldCars(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
   # gallery = models.ImageField(upload_to='photos/%Y/%m/%d')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    is_pablic = models.BooleanField(default=True)
    country = models.ForeignKey('Countries', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class Countries(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name


