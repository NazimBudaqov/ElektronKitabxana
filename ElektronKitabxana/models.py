from django.db import models
from django.utils.text import slugify

# abc.com/category/beyaz-esya (meselen)
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True, blank=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

# abc.com/author/ilyas-efendiyev (meselen)
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    middleName = models.CharField(max_length=150, null=True, blank=True)
    lastName = models.CharField(max_length=150)
    photo = models.ImageField(upload_to="authors",null=True)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True,)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name + "-" +self.lastName)
        super().save(*args, **kwargs)



class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="books")
    description = models.TextField()
    reyting = models.CharField(max_length=30)
    is_active = models.BooleanField()
    pdf = models.CharField(max_length=50)
    slug = models.SlugField(null=True, unique=True, blank=True, db_index=True, editable=False)

    category = models.ForeignKey(Category,default=1, on_delete=models.CASCADE)
    
    author = models.ForeignKey(Author, default=1, on_delete=models.CASCADE)

    #admin sehiofesinde Book object1 deye yox kitabin adi ile gelsin
    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    

    
