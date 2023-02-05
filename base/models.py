from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from datetime import datetime

# Create your models here.


class Event(models.Model):

    category = (
        ("Technical","Technical"),
        ("Non-Technical","Non-Technical")
    )

    banner_image = models.ImageField(null=True,blank=True,upload_to='banner')
    title = models.CharField(max_length=150)
    slug = models.SlugField(default="", editable=False, max_length=200, null = False)
    category = models.CharField(max_length=50,choices=category,null=True,blank=True)
    preview = models.CharField(max_length=300,null=True,blank=True)
    description = models.TextField(blank=True,null=True)
    start_date = models.DateTimeField(null=True,blank=True)
    end_date = models.DateTimeField(null=True,blank=True)
    registration_deadline = models.DateTimeField(null=True)
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("event_detail", args=[int(self.id),str(self.category),str(self.slug)])

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    @property
    def event_status(self):
        status = None
        
        present = datetime.now().timestamp()
        deadline = self.registration_deadline.timestamp()
        past_deadline = (present > deadline)

        if past_deadline:
            status = 'Finished'
        else:
            status = 'Ongoing'

        return status

    def __str__(self):
        return self.title



class Extra(models.Model):

    category = (
        ("Workshop","Workshop"),
        ("Webinar","Webinar")
    )

    banner_image = models.ImageField(null=True,blank=True,upload_to='banner')
    title = models.CharField(max_length=150)
    slug = models.SlugField(default="", editable=False, max_length=200, null = False)
    category = models.CharField(max_length=50,choices=category,null=True,blank=True)
    preview_image = models.ImageField(null=True,blank=True,upload_to='preview_images')
    preview = models.TextField(null=True,blank=True)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField(null=True,blank=True)
    end_date = models.DateTimeField(null=True,blank=True)
    registration_deadline = models.DateTimeField(null=True)
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("extra_detail", args=[str(self.category),int(self.id),str(self.slug)])

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name