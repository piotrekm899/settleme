from django.urls import path
from settleme_app import views


app_name = "settleme_app"


urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('user_login/', views.user_login, name="user_login"),

]
