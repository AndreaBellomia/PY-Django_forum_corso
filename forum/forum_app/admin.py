#Djagno app importing
from django.contrib import admin

#Local App importing
from .models        import Discussione, Post, Sezione



class DiscussioneModelAdmin(admin.ModelAdmin):
    """
    Custom del pannello /admin inerente alle discussioni
    """
    model = Discussione
    list_display = ["titolo", "sezione_appartenenza", "autore"]
    search_fields = ["titolo", "autore"]
    list_filter = ["sezione_appartenenza", "data_creazione"]


class PostModelAdmin(admin.ModelAdmin):
    """
    Custom del pannello /admin inerente ai Post
    """
    model = Post
    list_display = ["autore_post", "discussione"]
    search_fields = ["contenuto"]
    list_filter = ["data_creazione", "autore_post"]


class SezioneModelAdmin(admin.ModelAdmin):
    """
    Custom del pannello /admin inerente Sezioni
    """
    model = Sezione
    list_display = ["nome_sezione", "descrizione"]



#Model Registration to /admin pannel
admin.site.register(Discussione, DiscussioneModelAdmin)
admin.site.register(Post, PostModelAdmin)
admin.site.register(Sezione, SezioneModelAdmin)