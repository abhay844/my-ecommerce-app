from django.db import models
import os
import random


def get_file_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_file_name = random.randint(1, 39039012)
    name, ext = get_file_ext(filename)
    final_file_name = '{new_file_name}{ext}'.format(new_file_name=new_file_name, ext=ext)
    return "products/{new_file_name}/{final_file_name}".format(
        new_file_name=new_file_name,
        final_file_name=final_file_name
    )


class ProductManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(pk=id)  # self.get_queryset() == Product.objects
        if qs.count() == 1:
            return qs.first()

        return None


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=15, default=39.99)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    objects = ProductManager()

    def __str__(self):
        return self.title
