from django.db import models

class Technologies(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True,null=True)
    level = models.CharField(max_length=255,blank=True,null=True)
    url_logo = models.CharField(max_length=255)
    def __str__(self):
            return self.name