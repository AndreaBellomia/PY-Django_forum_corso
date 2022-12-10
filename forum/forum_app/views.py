#Djagno app importing
from django.contrib.auth.decorators     import login_required
from django.http                        import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts                   import render, get_object_or_404
from django.urls                        import reverse
from django.views.generic.edit          import CreateView

#Local App importing
from .forms     import DiscussioneModelForm, PostModelForm
from .mixins    import StaffMixins
from .models    import Discussione, Post, Sezione



# ]CLASS[


class CrezioneSezione(StaffMixins, CreateView):
    """
    Funzione Form per la creazione delle sezioni
    """
    model = Sezione
    fields = "__all__"
    template_name = "forum_app/crea_sezione.html"
    success_url = "/"




# ]FUNCTION[

#Function Form

@login_required
def crea_discussione(request, pk):
    """
    Funzione Form per la creazione delle discussioni
    """
    sezione = get_object_or_404(Sezione, pk=pk)
    if request.method == 'POST':
        form = DiscussioneModelForm(request.POST)
        if form.is_valid():
            discussione = form.save(commit=False)
            discussione.sezione_appartenenza = sezione
            discussione.autore = request.user
            discussione.save()
            primo_post = Post.objects.create(
                discussione = discussione, 
                autore_post = request.user, 
                contenuto = form.cleaned_data["contenuto"]
            )
            return HttpResponseRedirect(discussione.get_absolute_url())
    else:
        form = DiscussioneModelForm()
    context = {"form": form, "sezione": sezione}
    return render(request, "forum_app/crea_discussione.html", context)

@login_required
def aggiungi_risposta(request, pk):
    """
    Funzione Form per la creazione delle risposte nelle discussioni
    """
    discussione = get_object_or_404(Discussione, pk=pk)
    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.discussione = discussione
            form.instance.autore_post = request.user
            form.save()
            url_discussione = reverse("visualizza_discussione", kwargs={"pk":pk})
            return HttpResponseRedirect(url_discussione)

    else:
        return HttpResponseBadRequest()
        

#Function View

def visualizza_sezione(reqsuest, pk):
    """
    Funzione View per la visualizzazione della singola sezione
    """
    sezione = get_object_or_404(Sezione, pk=pk)
    
    discussioni_sezione = Discussione.objects.filter(
        sezione_appartenenza = sezione
        ).order_by("-data_creazione")
    context = {"sezione": sezione, "discussioni": discussioni_sezione}
    return render(reqsuest, "forum_app/singola_sezione.html", context)


def visualizza_discussione(request, pk):
    """
    Funzione View per la visualizzazione delle discussioni
    """
    discussione = get_object_or_404(Discussione, pk=pk)
    posts_discussione = Post.objects.filter(discussione=discussione)
    form_risposta = PostModelForm()
    context = {
        "discussione": discussione, 
        "posts_discussione": posts_discussione, 
        "form_risposta": form_risposta
        }
    return render(request, "forum_app/singola_discussione.html", context)


