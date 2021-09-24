from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from interface.models import Mushroom


# Create your views here.


def index(request):
    """Display the home page"""

    return render(request, 'home.html')

def atoz(request):
    """Display A to Z full list mushrooms"""
    mushrooms = Mushroom.objects.filter(image__isnull=False).order_by("espece")
    context = {
        "mushrooms": mushrooms
    }
    return render (request, "atoz.html",context)


class SearchResults(ListView):
    """Will display the 1st products page results with input of user"""

    model = Mushroom
    template_name = "search_list.html"

    def get_queryset(self):
        """
        Get the user input and return each product who contains the input
        in his name
        """

        query = self.request.GET.get("search")
        return Mushroom.objects.filter(image__isnull=False).filter(
            Q(espece__icontains=query) | Q(nom_vernaculaire__icontains=query)
        ).order_by("espece")
