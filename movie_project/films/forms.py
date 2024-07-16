from .models import Films
from django.forms import ModelForm


class NewFilmForm(ModelForm):
    class Meta:
        model = Films
        fields = ['name', 'short_description', 'text']