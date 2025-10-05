from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .models import Comment
from .models import Post,Tag
from django.forms import widgets  # <- import widgets

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']
class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'})
    )

    class Meta:
        model = Comment
        fields = ['content']
class TagWidget(widgets.CheckboxSelectMultiple):
    pass  # can customize if needed

# -----------------------------
# Post form with tags
# -----------------------------
class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=TagWidget()  # use the custom widget
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']