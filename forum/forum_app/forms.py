#Djagno app importing
from django     import forms

#Local App importing
from .models    import Discussione, Post

class DiscussioneModelForm(forms.ModelForm):
    """
    Model Form per la creazione delle discussioni
    #   utilizzata nella view.def crea_discussione()
    """
    contenuto = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Di cosa vuoi parlarci"}),
        max_length=4000, 
        label= "primo messaggio"
    )

    class Meta:
        model = Discussione
        fields = ["titolo", "contenuto"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Titolo della discussione"})
        }


class PostModelForm(forms.ModelForm):

    """
    Model Form per la creazione di risposte alle discussioni
    # utilizzata nella view.def aggiungi_risposta()
    # utilizzata nella view.def visualizza_discussione()
    """

    class Meta:
        model = Post
        fields = ["contenuto"]
        
        widgets = {
            "contenuto" : forms.Textarea(attrs={'rows' : '4'})
        }

        labels = {
            "contenuto" : ""
        }