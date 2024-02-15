from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    category_name = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self) -> str:
        return self.category_name


class Blog(models.Model):
    blog_name = models.CharField(max_length=250, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    # tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, blank=True)
    tag = models.ManyToManyField(Tag)
    draft = models.BooleanField(default=True)

    
    def __str__(self) -> str:
        return self.blog_name

