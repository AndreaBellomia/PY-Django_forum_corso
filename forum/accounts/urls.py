
#Djagno app importing
from accounts.views     import registrazione_view
from django.urls        import path


urlpatterns = [
    path('registrazione/', registrazione_view, name='registration_view')
]
