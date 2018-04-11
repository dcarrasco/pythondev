from django.forms import ModelForm
from django.forms.widgets import CheckboxInput


class OrmForm(ModelForm):
    def set_bootstrap_classes(self):
        for field in self.fields:
            if self._meta.model._meta.get_field(field).__class__.__name__ == 'BooleanField':
                self.fields[field].widget.template_name = 'acl/boolean_widget.html'
            else:
                if (field==self._meta.model._meta.pk.name):
                    self.fields[field].widget.attrs = {'class': 'form-control', 'readonly': 'readonly'}
                else:
                    self.fields[field].widget.attrs = {'class': 'form-control'}

