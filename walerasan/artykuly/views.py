from django.shortcuts import render
from django.views import View

from artykuly.models import Artykuly


class ArtykulyView(View):
    """WIDOK WYŚWIETLA SZCZEGÓŁOWE INFORMACJE O ROŚLINIE"""

    def get(self, request):
        artykuly = Artykuly.objects.order_by('-title')

        return render(request, 'main.html', {'art': artykuly})
