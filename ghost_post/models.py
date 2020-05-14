from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    isBoast = models.BooleanField()
    content = models.CharField(max_length=280)
    upVotes = models.IntegerField()
    downVotes = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content



# One model to represent both boasts and roasts
#     Boolean to tell whether it's a boast or a roast
#     CharField to put the content of the post in
#     IntegerField for up votes
#     IntegerField for down votes
#     DateTimeField for submission time
