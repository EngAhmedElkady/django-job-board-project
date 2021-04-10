from django.db import models

# Create your models here.
JOP_TYPE=(
        ("full time","full time"),
        ("part time","part time"),
    )
class job(models.Model):
    
    title = models.CharField(max_length=20)
    # location=models.CharField(max_length=30)
    jop_type=models.CharField(max_length=30,choices=JOP_TYPE)
    description=models.TextField(max_length=400)
    published=models.DateField(auto_now=True)
    Vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=5000)
    experience=models.IntegerField(default=5)


    def __str__(self):
        return self.title