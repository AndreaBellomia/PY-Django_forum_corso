#Djagno app importing
from django.urls import path

#Local App importing
from .           import views


urlpatterns = [
    path('discussione/<int:pk>/', views.visualizza_discussione, name='visualizza_discussione'),
    path('discussione/<int:pk>/rispondi/', views.aggiungi_risposta, name='rispondi_discussione'),
    path('sezione/<int:pk>/', views.visualizza_sezione, name='visualizza_sezione'),
    path('nuova-sezione/', views.CrezioneSezione.as_view(), name='creazione_sezione'),
    path('sezione/<int:pk>/crea-discussione/', views.crea_discussione, name='crea_discussione'),
]