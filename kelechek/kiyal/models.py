from django.db import models


class TagGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    group = models.ForeignKey(TagGroup, on_delete=models.CASCADE, related_name='tags')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(upload_to='icons/', blank=True, null=True)

    def __str__(self):
        return self.name


class Premises(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability_start_date = models.DateField()
    availability_end_date = models.DateField()
    tags = models.ManyToManyField(Tag, related_name='premises', blank=True)  # Connect Premises to Tag

    def __str__(self):
        return self.name
