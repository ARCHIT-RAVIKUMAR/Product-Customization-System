from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ProductView(models.Model):
    VIEW_CHOICES = [
        ('front', 'Front'),
        ('back', 'Back'),
        ('left', 'Left Side'),
        ('right', 'Right Side'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='views')
    view_type = models.CharField(max_length=20, choices=VIEW_CHOICES)
    base_image = models.ImageField(upload_to='products/base/')
    print_area_x = models.PositiveIntegerField()
    print_area_y = models.PositiveIntegerField()
    print_area_width = models.PositiveIntegerField()
    print_area_height = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.view_type}"