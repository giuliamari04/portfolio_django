from django.db import models
from django.utils.text import slugify
from .technologies import Technologies

class Posts(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True,null=True)
    technologies = models.ManyToManyField(Technologies, related_name='posts')
    collaborations = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # Genera lo slug dal nome del post
        super(Posts, self).save(*args, **kwargs)


    def __str__(self):
        return self.name


