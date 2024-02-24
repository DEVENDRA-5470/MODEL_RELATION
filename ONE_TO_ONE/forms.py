from django.forms.widgets import FileInput
from django.forms.models import ModelForm


from .models import *
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        widgets = {
         'profile_img': FileInput(),
         }