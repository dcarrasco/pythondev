from django.forms import ModelForm


class OrmForm(ModelForm):
    def set_bootstrap_classes(self, fields):
        for field in fields:
            if (field==self._meta.model._meta.pk.name):
                self.fields[field].widget.attrs = {'class': 'form-control', 'readonly': 'readonly'}
            else:
                self.fields[field].widget.attrs = {'class': 'form-control'}
