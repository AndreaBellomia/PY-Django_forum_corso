#Djagno app importing
from django.urls    import path
from core.views     import user_profile_view, UserList, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('users/', UserList.as_view(), name='user_list'),
    path('profile/<str:username>/', user_profile_view, name='user_profile_view')
    
] 
