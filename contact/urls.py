from django.urls import path
from . import views
from .views import addContact, deleteContact


urlpatterns = [
    # path('', views.index, name='index'),
    path('add-contact/', views.addContact, name='add-contact'),
    path('edit-contact/<str:pk>', views.editContact, name='edit-contact'),
    path('delete-contact/<str:pk>', deleteContact, name='delete-contact'),
    path('viewAll/', views.indexView.as_view(template_name="index.html")),
    # path('delete/(\d+)/$', views.deleteContact, name='deleter')

]

