from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# mvt
# news model
# like and views 

class NewsTest(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    # like = models.ManyToManyField()
    # images = models.ImageField() # does it require PILLOW library?

    def __str__(self):
        return self.title
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(NewsTest, on_delete=models.CASCADE, related_name="likes")
    # likes = models.BooleanField(default=False) # have to migrate

    def __str__(self):
        return f'{self.user} liked {self.item}'  