from django.db import models

# Create your models here.


class Systemic(models.Model):
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='images/', null=True)
    body = models.TextField(null=True)
    question1 = models.TextField(null=True)
    question2 = models.TextField(null=True)
    question3 = models.TextField(null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
