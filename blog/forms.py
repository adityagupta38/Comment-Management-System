from  django import forms
from blog.models import Posts,Comments

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = '__all__'


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'
