from django.forms import ModelForm
from.models import Comment
from crispy_forms.helper import FormHelper # type: ignore
from crispy_forms.layout import Submit # type: ignore

class CommentForm(ModelForm):
    class Meta:
        model= Comment
        fields= ('name', 'email', 'content')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Enviar'))