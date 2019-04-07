from django.db import models

# Create your models here.

class WICS(models.Model):

    # phone = models.CharField(max_length=255,default='',blank=True)
    phone = models.IntegerField(default='',blank=True)
    email = models.CharField(max_length=255,default='',blank=True)
    zip_code = models.IntegerField(default='',blank=True)
    # zip_code = models.CharField(max_length=5,default="",blank=True)

    def __str__(self):
        return '%s' % self.phone # %s return as string
