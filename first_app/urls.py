from django.urls import path
from . import views

# template tagging
app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('form', views.form_page, name='form_page'),
    path('users', views.users_page, name='users_page'),
    path('help', views.help_page, name='help_page'),
    path('other', views.other_page, name='other_page'),
    path('relative', views.relative_page, name='relative_page'),
    path('register', views.register_page, name='register_page'),
    path('user_login', views.user_login_page, name='user_login_page'),
    path('user_logout', views.user_logout_page, name='user_logout_page'),
    path('special', views.special_page, name='special_page'),
]

