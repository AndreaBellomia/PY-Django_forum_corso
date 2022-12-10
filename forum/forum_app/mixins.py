#Djagno app importing
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts           import redirect



# mixin per la classe views.CrezioneSezione
class StaffMixins(UserPassesTestMixin):
    """
    Classse che limita la creazione di nuove sezioni solo allo staff
    """
    
    def test_func(self):
        return self.request.user.is_staff
