from django import forms
from django.forms import DateInput
from django_ckeditor_5.widgets import CKEditor5Widget
from admin_app.models import *

class LatestReleaseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].required = False

    class Meta:
        model = LatestRelease
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'title': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'slug_name' : forms.TextInput(attrs={'class': 'form-control'}),
        }
        


class LocationReportForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].required = False

    class Meta:
        model = LocationReport
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'title': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'slug_name' : forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class MeetThePersonForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].required = False

    class Meta:
        model = MeetThePerson
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'title': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'slug_name' : forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        
        
class TeaserAndPromoseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].required = False

    class Meta:
        model = TeaserAndPromose
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'title': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'slug_name' : forms.TextInput(attrs={'class': 'form-control'}),
        }