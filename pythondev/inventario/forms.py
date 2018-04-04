from django import forms
from .models import Auditor

class AuditorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AuditorForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs = {'class': 'form-control'}

    class Meta:
        model = Auditor
        fields = ['nombre', 'activo']
