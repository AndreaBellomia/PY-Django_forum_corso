#Djagno app importing
from django.contrib.auth.models import User
from django.db                  import models
from django.urls                import reverse

#External library
import datetime


# Database Model File

class Sezione(models.Model):
    """ 
    Modello Sezione Forum 
    Divisione del sito 
    Ogni sezione contiene più discussioni create dagli amministratori del sito
    
    """

    nome_sezione = models.CharField(max_length=80)
    descrizione = models.CharField(max_length=150, blank=True, null=True)
    logo_sezione = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nome_sezione

    def get_absolute_url(self):
        return reverse("visualizza_sezione", kwargs={'pk': self.pk})
    
    class Meta:
        verbose_name = "Sezione"
        verbose_name_plural = "Sezioni"


class Discussione(models.Model):
    """ 
    Modello Discussione Forum 
    Divisione delle sezioni in discussioni
    Ogni discussioni contiene i commenti degli utenti presenti in User

    """

    titolo = models.CharField(max_length=120)
    data_creazione = models.DateTimeField(auto_now_add=True)
    autore = models.ForeignKey(User, on_delete=models.CASCADE, related_name='discussioni')
    sezione_appartenenza = models.ForeignKey(Sezione, on_delete=models.CASCADE)

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        return reverse("visualizza_discussione", kwargs={'pk': self.pk})
    
    def get_day_ago(self):
        django_date = str(self.data_creazione)
        date = datetime.datetime.now() - datetime.datetime.strptime(django_date[:len(django_date) -6], '%Y-%m-%d %H:%M:%S.%f') - datetime.timedelta(hours=1)
        if date.days >= 1:
            return f'{date.days} giorno' if date.days == 1 else f'{date.days} giorni'
        else:
            hours = float(date.seconds/3600)
            if hours <= 1:
                return '< 1 hr'
            else:
                return f'{str(round(hours))} hr'
    
        
    class Meta:
        verbose_name = "Discussione"
        verbose_name_plural = "Discussioni"


class Post(models.Model):
    """ 
    Modello Post Forum 
    Ogni post contine il commento che un utente aggiunge ad una sezione

    """

    autore_post = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    contenuto = models.TextField()
    data_creazione = models.DateTimeField(auto_now_add=True)
    discussione = models.ForeignKey(Discussione, on_delete=models.CASCADE, related_name='posts_discussione')

    def __str__(self):
        return self.autore_post.username
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
