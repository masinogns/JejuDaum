from django.db import models

# Create your models here.
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Book(models.Model):
    owner = models.ForeignKey(User, null=True)
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    update_date = models.DateTimeField(null = True, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('jejudaum:book_edit', kwargs={'pk': self.pk})
