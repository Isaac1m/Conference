from django.forms import ModelForm
from .models import Session
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SessionForm(ModelForm):
    class Meta:
        model = Session
        fields = ['title', 'abstract', 'track', 'speaker']

    def __init__(self, *args, **kwargs):
        super(SessionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-offset-1 col-md-2'
        self.helper.field_class = 'col-md-8'
        self.helper.add_input(Submit('submit', 'submit', css_class='btn btn-success'))
        self.helper._form_method = 'POST'
