from django.db import models


class About(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    images = models.ImageField(upload_to="about")
    dic = models.TextField()

    def __str__(self):
        return self.title
