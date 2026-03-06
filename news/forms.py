from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ismingiz',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email manzilingiz',
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Fikringizni yozing...',
                'rows': 4,
            }),
        }


class EmailShareForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Ismingiz',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Sizning emailingiz',
    }))
    to = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Qabul qiluvchi email',
    }))
    comments = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'class': 'form-control', 'placeholder': 'Izoh (ixtiyoriy)', 'rows': 3,
    }))


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Ismingiz',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Email manzilingiz',
    }))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Mavzu',
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control', 'placeholder': 'Xabaringiz', 'rows': 5,
    }))


class SearchForm(forms.Form):
    query = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': "Yangilik qidirish...",
    }))
