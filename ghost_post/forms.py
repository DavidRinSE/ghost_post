from django import forms
from ghost_post.models import Post

class PostForm(forms.Form):
    post_type = forms.ChoiceField(choices=(
        (True, "Boast"),
        (False, "Roast"),
    ))
    post = forms.CharField(widget=forms.Textarea, max_length=280)



# isBoast = models.BooleanField()
# content = models.CharField(max_length=280)
# upVotes = models.IntegerField()
# downVotes = models.IntegerField()
# date = models.DateTimeField(default=timezone.now)