from django import forms
from .models import Post

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'naamdier', 'image','latijnsenaam', 'kortebeschrijving', 'geslachtsonderscheid', 'huisvesting', 'inrichting', 'voeding', 'voortplanting', 'soort')
        
        
class PostSearchForm(forms.ModelForm):
    search=forms.CharField(required=False, label="Search")
    class Meta:
        model=Post
        fields=['soort', 'search']         
 
   