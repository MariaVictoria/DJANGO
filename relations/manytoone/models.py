from django.db import models
from datetime import date

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.last_name

class Article(models.Model):
    headline = models.CharField(default='none', max_length=100)
    pub_date = models.DateField(default=date(2000, 1, 1))
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE, default=1)  # Example default ID

    def __str__(self):
        return self.headline
