from django.db import models

class MainCategory(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class Category(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True, default='MEDICAL EQUIPMENT')
    
    def __str__(self):
        return self.title

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to='product_images/')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_image(self):
        try:
            return f"http://localhost:8000{self.image.url}"
        except:
            return "https://m.media-amazon.com/images/I/21cOE-lrhBL._AC_UF1000,1000_QL80_.jpg"
        

class Contacts(models.Model):
    full_name = models.CharField(max_length=300)
    email = models.CharField(max_length=50)
    message = models.TextField(default="No Comment")
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'Request a Quote'
        verbose_name_plural = 'Request Quotes'


