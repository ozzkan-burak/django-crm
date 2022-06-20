from django.urls import path
from .views import home_page

urlpatterns = {
  path('all/', home_page, name='home'),
}