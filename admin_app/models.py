from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify

# Create your models here.

class LatestRelease(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    text = CKEditor5Field('Text', config_name='extends')
    slug_name = models.CharField(max_length=200, default='slug')
    slug = models.SlugField(unique=True, blank=True)

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.slug_name)
            # Check if the generated slug already exists
            if LatestRelease.objects.filter(slug=self.slug).exists():
                # Append a number to the slug to make it unique
                count = 1
                while LatestRelease.objects.filter(slug=self.slug).exists():
                    self.slug = f"{slugify(self.slug_name)}-{count}"
                    count += 1
        super().save(*args, **kwargs)
    
class LocationReport(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    text = CKEditor5Field('Text', config_name='extends')
    slug_name = models.CharField(max_length=200, default='slug')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.slug_name)
            # Check if the generated slug already exists
            if LocationReport.objects.filter(slug=self.slug).exists():
                # Append a number to the slug to make it unique
                count = 1
                while LocationReport.objects.filter(slug=self.slug).exists():
                    self.slug = f"{slugify(self.slug_name)}-{count}"
                    count += 1
        super().save(*args, **kwargs)

   
    
class MeetThePerson(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    text = CKEditor5Field('Text', config_name='extends')
    slug_name = models.CharField(max_length=200, default='slug')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.slug_name)
            # Check if the generated slug already exists
            if MeetThePerson.objects.filter(slug=self.slug).exists():
                # Append a number to the slug to make it unique
                count = 1
                while MeetThePerson.objects.filter(slug=self.slug).exists():
                    self.slug = f"{slugify(self.slug_name)}-{count}"
                    count += 1
        super().save(*args, **kwargs)

class TeaserAndPromose(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    text = CKEditor5Field('Text', config_name='extends')
    slug_name = models.CharField(max_length=200, default='slug')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.slug_name)
            # Check if the generated slug already exists
            if TeaserAndPromose.objects.filter(slug=self.slug).exists():
                # Append a number to the slug to make it unique
                count = 1
                while TeaserAndPromose.objects.filter(slug=self.slug).exists():
                    self.slug = f"{slugify(self.slug_name)}-{count}"
                    count += 1
        super().save(*args, **kwargs)
        
        
class FlashNews(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True, null=True, blank=True)