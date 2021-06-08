
from django.forms import ModelForm
from posts.models import Posts

class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['title','photo','user','profile']