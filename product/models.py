from django.db import models
from autoslug import AutoSlugField
from accounts.models import Account


# Global function
def upload_path_handler(instance, filename):
    return "uploads/product_{id}/{file}".format(id=instance.product_id.id, file=filename)


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = AutoSlugField(max_length=225, unique=True, populate_from='category_name', null=True, default=None)
    description = models.TextField(max_length=225, blank=True)
    image = models.ImageField(upload_to='photos/categories')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'{self.category_name}'

    @property
    def get_counts(self):
        return Product.objects.filter(category=self).__len__()

    @property
    def avg_price(self):
        products = Product.objects.filter(category=self)
        if products.__len__():
            return f'{sum([product.price for product in products]) / products.__len__()}'

        return '0'


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, null=True)
    stock = models.PositiveIntegerField(default=0, blank=False)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    price = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, models.RESTRICT)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    vendor_id = models.ForeignKey(Account, models.RESTRICT)
    product_code = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return f'{self.id} - {self.product_name} - {self.price}'

    def get_stock(self):
        return self.stock

    @property
    def get_first_image(self):
        return ProductImage.objects.filter(product_id=self).first()

    @property
    def get_all_images(self):
        return ProductImage.objects.filter(product_id=self)


class ProductImage(models.Model):
    product_id = models.ForeignKey(Product, models.CASCADE)
    image = models.ImageField(upload_to=upload_path_handler)

    class Meta:
        verbose_name = 'product image'
        verbose_name_plural = 'product images'

    def __str__(self):
        return self.image.url
