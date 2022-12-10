#Djagno app importing
from django                         import forms
from django.contrib.auth.forms      import UserCreationForm
from django.contrib.auth.models     import User




class FormRegistrazione(UserCreationForm):
    """ Form per la registrazione degli User """
    email = forms.CharField(max_length=30, required=True, widget=forms.EmailInput())

    #Funzione per il customing degli elementi
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['username'].widget.attrs.update({'class': 'special'})


    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
