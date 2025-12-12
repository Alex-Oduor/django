from django.db import models

# Create your models here.
class blogContent(models.Model):
    date_created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length = 100)
    contents = models.TextField()
    

    def __str__(self):
        return self.title


