#Djagno app importing
from django.contrib.auth.decorators     import login_required
from django.contrib.auth.models         import User
from django.contrib.auth.mixins         import LoginRequiredMixin
from django.shortcuts                   import get_object_or_404, render 
from django.views.generic.list          import ListView

#Local App importing
from forum_app.models import Discussione, Sezione




# ]CLASS[


class HomeView(ListView):
    """
    View della homepage 
    """
    queryset = Sezione.objects.all()
    template_name = 'core/homepage.html'
    context_object_name = "lista_sezioni"


class UserList(LoginRequiredMixin, ListView):
    """
    View della lista utenti del forum 
    """
    model = User
    template_name = 'core/user_list.html'


# ]FUNCTION[

@login_required
def user_profile_view(request, username):
    ''' 
    View della UserPorfile page del sito 
    '''

    user = get_object_or_404(User, username=username)
    discussioni_utente = Discussione.objects.filter(autore=user).order_by("-pk")
    context = {"user": user, "discussioni_utente": discussioni_utente}
    
    return render(request, "core/user_profile.html", context)




