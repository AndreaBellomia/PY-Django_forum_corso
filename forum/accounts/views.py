#Djagno app importing
from django.contrib.auth            import authenticate, login
from django.contrib.auth.models     import User
from django.shortcuts               import render, HttpResponseRedirect

#Local App importing
from accounts.forms import FormRegistrazione





def registrazione_view(request):
    """ Fuznione di Registrazione degli Utenti e Auto Login """
    if request.method == 'POST': # Ricezione del form
        form = FormRegistrazione(request.POST) # Crezione dell'instaza form
        
        if form.is_valid(): # Validazione Post
            print(form.cleaned_data)
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            # Querry a database per il salvataggio dell'utente
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user) # Auto login dopo la registrazione 
            return HttpResponseRedirect('/')

    else: # Primo rendering dell'form
        form = FormRegistrazione()

    return render(request, "accounts/registrazione.html", {'form':form})

