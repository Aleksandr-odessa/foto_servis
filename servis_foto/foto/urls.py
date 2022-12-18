from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import SignUp, index, AddFoto, SearchDate, \
    SearchPerson, SearchGeo, StartFoto, SearchID, delete

urlpatterns = [
    path('', index, name="index"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('home/logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('home/', StartFoto.as_view(), name='home'),
    path('<str:var_path>/home', StartFoto.as_view(), name='home'),
    path('<str:var>/add_foto/', AddFoto.as_view(), name='add_foto'),
    path('search_date/', SearchDate.as_view(), name='search_date'),
    path('search_person/', SearchPerson.as_view(), name='search_person'),
    path('search_geo/', SearchGeo.as_view(), name='search_geo'),
    path('search_id/', SearchID.as_view(), name='search_id'),
    path('<str:var_path>/logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('home/delete/<str:id>/', delete, name="delete"),
]
