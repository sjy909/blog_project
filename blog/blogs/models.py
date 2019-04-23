from django.db import models

# Create your models here.


class KIND(models.Model):
    k_content = models.CharField(max_length=255)


class ARTICLE(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    read_count = models.IntegerField()
    author = models.CharField(max_length=255)
    content = models.TextField()
    a_k = models.ForeignKey(KIND, on_delete=models.CASCADE)


class COMMENT(models.Model):
    c_author = models.CharField(max_length=255)
    c_content = models.TextField()
    c_datetime = models.DateField(auto_now_add=True)
    c_a = models.ForeignKey(ARTICLE, on_delete=models.CASCADE)


class TALLY(models.Model):
    t_content = models.CharField(max_length=255)
    t_a = models.ManyToManyField(ARTICLE)

