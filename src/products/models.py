from django.db import models
import os
import random
from ecommerce.utils import unique_slug_generator
from django.db.models.signals import pre_save


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


class ProductQuerySet(models.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def featured(self):
        return self.get_queryset().filter(featured=True)

    def active(self):
        return self.get_queryset().active()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(pk=id)  # self.get_queryset() == Product.objects
        if qs.count() == 1:
            return qs.first()

        return None


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=15, default=39.99)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    objects = ProductManager()

    def get_absolute_url(self):
        return "/products/{slug}/".format(slug=self.slug)
        pass

    def __str__(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


# Receiver function
pre_save.connect(product_pre_save_receiver, sender=Product)
