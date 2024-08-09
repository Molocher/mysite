from django.db import models
from datetime import date


# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)
    data = models.JSONField(default=[{}])

    def __str__(self):
        return (f"blog:{self.blog},headline:{self.headline},"
                f"body_text:{self.body_text},pub_date:{self.pub_date},"
                f"mod_date:{self.mod_date},authors:{self.authors},"
                f"number_of_comments:{self.number_of_comments},"
                f"number_of_pingbacks:{self.number_of_pingbacks}")


class Dog(models.Model):
    name = models.CharField(max_length=200)
    data = models.JSONField(null=True)

    def __str__(self):
        return self.name
