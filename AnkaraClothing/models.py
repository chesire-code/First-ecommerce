from django.db import models
from PIL import Image
from django.shortcuts import reverse
from django.conf import settings

class offer(models.Model):
    product_names = models.CharField(max_length=100)
    descriptions = models.TextField(default="")
    image = models.ImageField(upload_to='images/')
    image_two = models.ImageField(upload_to='images/', blank = True)
    image_three = models.ImageField(upload_to='images/', blank = True)
    price = models.IntegerField(default=0)
    previous_price = models.IntegerField()
    slug = models.SlugField(max_length=100, default="offer")

    def get_absolute_url(self):
        return reverse("offer", kwargs={
            'slug' : self.slug
        })

    def get_offer_add_to_cart_url(self):
        return reverse("offer-cart", kwargs={
            'slug': self.slug
        })

    def get_offer_remove_from_cart_url(self):
        return reverse("remove-offer-cart", kwargs={
            'slug': self.slug
        })

class bestseller(models.Model):
    product_names = models.CharField(max_length=100)
    descriptions = models.TextField(default="")
    image = models.ImageField(upload_to='images/')
    image_two = models.ImageField(upload_to='images/', blank = True)
    image_three = models.ImageField(upload_to='images/', blank = True)
    price = models.IntegerField(default=0)
    previous_price = models.IntegerField()
    slug = models.SlugField(max_length=100, default="offer")

    def get_absolute_url(self):
        return reverse("bestseller", kwargs={
            'slug' : self.slug
        })

    def get_offer_add_to_cart_url(self):
        return reverse("offer-cart", kwargs={
            'slug': self.slug
        })

    def get_offer_remove_from_cart_url(self):
        return reverse("remove-offer-cart", kwargs={
            'slug': self.slug
        })


class smartphone(models.Model):
    product_names = models.CharField(max_length=100)
    descriptions = models.TextField(default="")
    image = models.ImageField(upload_to='images/')
    image_two = models.ImageField(upload_to='images/', blank = True)
    image_three = models.ImageField(upload_to='images/', blank = True)
    price = models.IntegerField(default=0)
    previous_price = models.IntegerField()
    slug = models.SlugField(max_length=100, default="offer")

    def get_absolute_url(self):
        return reverse("smartphone", kwargs={
            'slug' : self.slug
        })

    def get_offer_add_to_cart_url(self):
        return reverse("offer-cart", kwargs={
            'slug': self.slug
        })

    def get_offer_remove_from_cart_url(self):
        return reverse("remove-offer-cart", kwargs={
            'slug': self.slug
        })

class charger(models.Model):
    product_name = models.CharField(max_length=100)
    descriptions = models.TextField(default="")
    image = models.ImageField(upload_to='images/')
    image_two = models.ImageField(upload_to='images/', blank = True)
    image_three = models.ImageField(upload_to='images/', blank = True)
    price = models.IntegerField()
    previous_price = models.IntegerField()
    slug = models.SlugField(max_length=100, default="product")

    def get_absolute_url(self):
        return reverse("charger", kwargs={
            'slug': self.slug
        })

    def get_product_add_to_cart_url(self):
        return reverse("product-cart", kwargs={
            'slug': self.slug
        })

    def get_trending_remove_from_cart_url(self):
        return reverse("remove-trending-cart", kwargs={
            'slug': self.slug
        })

class cover(models.Model):
    product_name = models.CharField(max_length=100)
    descriptions = models.TextField(default="")
    image = models.ImageField(upload_to='images/')
    image_two = models.ImageField(upload_to='images/', blank = True)
    image_three = models.ImageField(upload_to='images/', blank = True)
    price = models.IntegerField()
    previous_price = models.IntegerField()
    slug = models.SlugField(max_length=100, default="product")

    def get_absolute_url(self):
        return reverse("cover", kwargs={
            'slug': self.slug
        })

    def get_product_add_to_cart_url(self):
        return reverse("product-cart", kwargs={
            'slug': self.slug
        })

    def get_trending_remove_from_cart_url(self):
        return reverse("remove-trending-cart", kwargs={
            'slug': self.slug
        })

class USB_drive(models.Model):
    product_name = models.CharField(max_length=100)
    descriptions = models.TextField(default="")
    image = models.ImageField(upload_to='images/')
    image_two = models.ImageField(upload_to='images/', blank=True)
    image_three = models.ImageField(upload_to='images/', blank=True)
    price = models.IntegerField()
    previous_price = models.IntegerField()
    slug = models.SlugField(max_length=100, default="product")

    def get_absolute_url(self):
        return reverse("protector", kwargs={
            'slug': self.slug
        })

    def get_product_add_to_cart_url(self):
        return reverse("product-cart", kwargs={
            'slug': self.slug
        })

    def get_trending_remove_from_cart_url(self):
        return reverse("remove-trending-cart", kwargs={
            'slug': self.slug
        })

class bt_speaker(models.Model):
    product_name = models.CharField(max_length=100)
    descriptions = models.TextField(default="")
    image = models.ImageField(upload_to='images/')
    image_two = models.ImageField(upload_to='images/', blank=True)
    image_three = models.ImageField(upload_to='images/', blank=True)
    price = models.IntegerField()
    previous_price = models.IntegerField()
    slug = models.SlugField(max_length=100, default="product")

    def get_absolute_url(self):
        return reverse("bt_speaker", kwargs={
            'slug': self.slug
        })

    def get_product_add_to_cart_url(self):
        return reverse("product-cart", kwargs={
            'slug': self.slug
        })

    def get_trending_remove_from_cart_url(self):
        return reverse("remove-trending-cart", kwargs={
            'slug': self.slug
        })

class earphones(models.Model):
    product_name = models.CharField(max_length=100)
    descriptions = models.TextField(default="")
    image = models.ImageField(upload_to='images/')
    image_two = models.ImageField(upload_to='images/', blank=True)
    image_three = models.ImageField(upload_to='images/', blank=True)
    price = models.IntegerField()
    previous_price = models.IntegerField()
    slug = models.SlugField(max_length=100, default="product")

    def get_absolute_url(self):
        return reverse("earphone", kwargs={
            'slug': self.slug
        })

    def get_product_add_to_cart_url(self):
        return reverse("product-cart", kwargs={
            'slug': self.slug
        })

    def get_trending_remove_from_cart_url(self):
        return reverse("remove-trending-cart", kwargs={
            'slug': self.slug
        })

class OrderOffer(models.Model):
    item = models.ForeignKey(charger, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} {self.item.product_name}"

class OrderTrending(models.Model):
    item = models.ForeignKey(charger, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.user.username

class OfferOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    items = models.ManyToManyField(OrderOffer)
    date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class TrendingOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    items = models.ManyToManyField(OrderTrending)
    quantity = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Subscribers(models.Model):
    mail = models.CharField(max_length=100)

class Message(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField(default="")


