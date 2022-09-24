from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):  #defines our model, it is an object, Post is the name of the our model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #properties of the object, this is for a link to another model
    title = models.CharField(max_length=200) #limited numbers of characters text is defined like this
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title