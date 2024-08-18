from django.db import models


class Lesson(models.Model):
    numbers = models.IntegerField()
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=225, blank=True, null=True)
    images = models.ImageField(upload_to="edu")
    link = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lesson'
        db_table = 'lesson'


