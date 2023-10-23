from django import forms
from .models import İmage,Pano,Pin,Comment

#choices = [('coding','coding'),('sports','sports'),('eğlence','eğlence'),]
choices = Pano.objects.all().values_list('name','name')

choice_list=[]

for item in choices:
    choice_list.append(item)

class İmageForm(forms.ModelForm):
    class Meta:
        model=İmage
        fields=('title','body','user','category','snippet','likes')

        widgets={
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'body':forms.Textarea(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list,attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'likes': forms.Select(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model=Pin
        fields=('pin_title','pin_body','url','pin_image')

        widgets={
            'pin_title':forms.TextInput(attrs={'class':'form-control'}),
            'pin_body': forms.Textarea(attrs={'class':'form-control'}),
            'url': forms.TextInput(attrs={'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),  
        }        
