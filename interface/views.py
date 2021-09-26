from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from interface.models import Mushroom
from interface.service import Service

service = Service()  # Load all the necessary methods from service.py

# Create your views here.


def index(request):
    """Display the home page"""

    return render(request, 'home.html')

def atoz(request):
    """Display A to Z full list mushrooms"""
    mushrooms = service.get_all_mushrooms()
    context = service.set_mushrooms_context(mushrooms)
    return render(request, "atoz.html", context)

def mushroom_details(request, mushroom_id):
    """Go to mushroom detail page"""
    mushroom = service.get_mushroom(mushroom_id)
    context = service.set_mushrooms_context(mushroom)
    return render(request, "mushroom_details.html", context)

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
        results = service.search_results_with_name(query)
        return results



