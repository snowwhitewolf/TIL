from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    path('update/', views.update, name='update'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('<username>/', views.profile, name='profile'),
]