from django.urls import path , include
from . import views

app_name = 'contacts'

urlpatterns = [
    path('',views.view_contact,name='contact'),
    path('done',views.sent,name='sent'),
]


