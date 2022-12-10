#Djagno app importing
from django.contrib.auth.models     import User
from django.shortcuts               import get_object_or_404, render 
from django.views.generic.list      import ListView

#Local App importing
from forum_app.models import Sezione




# ]CLASS[


class HomeView(ListView):
    """
    View della homepage 
    """
    queryset = Sezione.objects.all()
    template_name = 'core/homepage.html'
    context_object_name = "lista_sezioni"


class UserList(ListView):
    """
    View della lista utenti del forum 
    """
    model = User
    template_name = 'core/user_list.html'


# ]FUNCTION[


def user_profile_view(request, username):
    ''' 
    View della UserPorfile page del sito 
    '''

    user = get_object_or_404(User, username=username)
    context = {"user": user}
    
    return render(request, "core/user_profile.html", context)




