from django.db import models

class Cake(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField()
    weight = models.PositiveSmallIntegerField(default=0, help_text="gramla")
    ingredients = models.TextField(max_length=3000, null=True, blank=True)
    baked_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    image_url = models.URLField(max_length=256, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name} -- {self.price}"