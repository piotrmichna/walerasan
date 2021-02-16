from django.urls import path

from artykuly.views import ArtykulyView

urlpatterns = [
    path('', ArtykulyView.as_view(), name='artykuly'),
]
