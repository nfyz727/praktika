from django.db import models


class TypeProduct(models.Model):
    name = models.CharField(max_length=120)
    kef = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class TypeMaterial(models.Model):
    name = models.CharField(max_length=120)
    waste_percent = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_type = models.ForeignKey(TypeProduct, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    article = models.CharField(max_length=50, unique=True)
    min_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Region (models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class City (models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Street (models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Address (models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    house = models.IntegerField()
    index = models.IntegerField()

    def __str__(self):
        return f"{self.region}, {self.city}, {self.street}, {self.house}, {self.index}"


class Director (models.Model):
    fio = models.CharField(max_length=120)

    def __str__(self):
        return self.fio


class TypePartner (models.Model):
    type = models.CharField(max_length=120)

    def __str__(self):
        return self.type


class Partner (models.Model):
    type = models.ForeignKey(TypePartner, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    inn = models.CharField(max_length=12)
    rate = models.IntegerField()

    def __str__(self):
        return self.name


class Postavki(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    kolvo = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f'{self.product.name} - {self.kolvo} шт. ({self.date})'
