from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import NewUser


from django import forms
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Kullanıcı Adı', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Şifre', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = NewUser
        fields = UserCreationForm.Meta.fields + ('email',)  # Eğer ekstra alanlarınız varsa buraya ekleyin

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = NewUser
        fields = UserChangeForm.Meta.fields


from .models import Industry, BlogPost

class IndustryForm(forms.ModelForm):
    class Meta:
        model = Industry
        fields = ['name', 'description']

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']