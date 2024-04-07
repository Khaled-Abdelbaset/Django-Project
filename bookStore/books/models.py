from django.db import models
from categories.models import Category

# Create your models here.
class book(models.Model):
    title = models.CharField(max_length=100)
    no_pages = models.IntegerField(null=True, blank=True)
    author = models.CharField(max_length=100)
    price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='books/images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)


    @property
    def image_url(self):
        return f"/media/{self.image}"
