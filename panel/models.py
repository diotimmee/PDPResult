from django.db import models


class Homework(models.Model):
    SINCE_CHOICES = [
        ('C++', 'c++'),
        ('JAVA', 'java'),
        ('PYTHON', 'python'),
        ('FRONTEND', 'frontend'),
        ('ROBOTEXNIKA', 'robotexnika'),
        ('FIZIKA', 'fizika'),
        ('MATEMATIKA', 'matemateka'),
        ('INGILIZ TILI', 'ingiliz tili'),
        ('RUS TILI', 'rus tili'),
        ('STA', 'sta'),
        ('ONA TILI', 'ona tili'),
        ('TARBIYA', 'tarbiya'),
        ('JISMONIY', 'jismoniy'),
        ('TARIX', 'tarix'),
        ('BiOLOGIYA', 'biologiya'),
        ('GEOMETRIYA', 'geometriya'),
        ('GEOGRAFIYA', 'geografiya'), ]

    date = models.DateTimeField()
    homework = models.CharField(max_length=255, blank=True, null=True)
    since = models.CharField(max_length=20, choices=SINCE_CHOICES)
    status = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.homework

    class Meta:
        verbose_name = 'Homework'
        verbose_name_plural = 'HomeWork'
        db_table = 'homework'


class Contact(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
