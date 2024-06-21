from django import forms


class FormularioIniciarConversacion(forms.Form):

    user_chat_2 = forms.ModelChoiceField(
        queryset=None,
        empty_label='',
        widget=forms.Select(attrs={ 'class' : 'form-control' }),
        label='Chatear con',
        to_field_name='username'
    )


class FormularioEnvioMensaje(forms.Form):

    contenido = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={ 'class' : 'form-control' }),
        label=''
    )