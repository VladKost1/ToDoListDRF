from django.urls import path
from todoapp.views import *
urlpatterns = [
    path('', ListView.as_view()),
    path('create', CreateView.as_view()),
    path('<int:pk>/', DetailView.as_view()),
    path('delete/<int:pk>', DeleteView.as_view())

]