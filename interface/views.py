from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateResponse
from interface.models import Mushroom
from interface.service import Service

service = Service()  # Load all the necessary methods from service.py

# Create your views here.


def index(request):
    """Display the home page"""

    return render(request, 'home.html')


def info(request):
    """Display the home page"""

    return render(request, 'info.html')

def atoz(request):
    """Display A to Z full list mushrooms"""

    user = request.user
    mushrooms = service.get_all_mushrooms()
    mushrooms = service.sort_out_user_favorite_mushrooms(mushrooms, user)
    context = service.set_mushrooms_context(mushrooms)
    return render(request, "atoz.html", context)

def mushroom_details(request, mushroom_id):
    """Go to mushroom detail page"""
    user = request.user
    mushroom = service.get_mushroom(mushroom_id)
    mushroom = service.sort_out_if_mushroom_is_favorite(mushroom, user)
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
        results = service.sort_out_user_favorite_mushrooms(
            results, user=self.request.user)
        return results

def sort_by_edible_very_good(request):

    user = request.user
    mushrooms = service.sort_by_edible_very_good()
    mushrooms = service.sort_out_user_favorite_mushrooms(mushrooms, user)
    context = service.set_mushrooms_context(mushrooms)
    return render(request, "sort_by_edible_very_good.html", context)


def sort_by_edible_good(request):

    user = request.user
    mushrooms = service.sort_by_edible_good()
    mushrooms = service.sort_out_user_favorite_mushrooms(mushrooms, user)
    context = service.set_mushrooms_context(mushrooms)
    return render(request, "sort_by_edible_good.html", context)


def sort_by_edible_bad_good(request):

    user = request.user
    mushrooms = service.sort_by_edible_bad_good()
    mushrooms = service.sort_out_user_favorite_mushrooms(mushrooms, user)
    context = service.set_mushrooms_context(mushrooms)
    return render(request, "sort_by_edible_bad_good.html", context)


def sort_by_edible_bad(request):

    user = request.user
    mushrooms = service.sort_by_edible_bad()
    mushrooms = service.sort_out_user_favorite_mushrooms(mushrooms, user)
    context = service.set_mushrooms_context(mushrooms)
    return render(request, "sort_by_edible_bad.html", context)


def sort_by_edible_toxic(request):

    user = request.user
    mushrooms = service.sort_by_edible_toxic()
    mushrooms = service.sort_out_user_favorite_mushrooms(mushrooms, user)
    context = service.set_mushrooms_context(mushrooms)
    return render(request, "sort_by_edible_toxic.html", context)


def sort_by_edible_deadly(request):

    user = request.user
    mushrooms = service.sort_by_edible_deadly()
    mushrooms = service.sort_out_user_favorite_mushrooms(mushrooms, user)
    context = service.set_mushrooms_context(mushrooms)
    return render(request, "sort_by_edible_deadly.html", context)

def engine2(request, color_top):
    
    args = {}
    color_top = color_top
    args['color_top'] = color_top
    
    return TemplateResponse(request, "engine2.html", args)

def engine3(request, color_top, form):
    
    args = {}
    color_top = color_top
    form = form
    args['color_top'] = color_top
    args['form'] = form

    return TemplateResponse(request, "engine3.html", args)


def engine4(request, color_top, form, color_under):

    args = {}
    color_top = color_top
    form = form
    color_under = color_under
    args['color_top'] = color_top
    args['form'] = form
    args['color_under'] = color_under

    return TemplateResponse(request, "engine4.html", args)

def engine_results(request, color_top, form, color_under, ring):

    user = request.user

    args = {}
    color_top = color_top
    form = form
    color_under = color_under
    args['color_top'] = color_top
    args['form'] = form
    args['color_under'] = color_under
    args['ring'] = ring

    if color_top == "blanc":
        first_sort_color_top = service.sort_by_color_top_white()
    elif color_top == "brun":
        first_sort_color_top = service.sort_by_color_top_brown()
    elif color_top == "rouge":
        first_sort_color_top = service.sort_by_color_top_red()
    elif color_top == "jaune":
        first_sort_color_top = service.sort_by_color_top_yellow()
    else:
        first_sort_color_top = service.sort_by_color_top_other()

    if form == "lamelles":
       second_sort_form = service.sort_by_lamelles(first_sort_color_top)
    elif form == "tubes":
       second_sort_form = service.sort_by_tubes(first_sort_color_top)
    elif form == "plis fourchus":
       second_sort_form = service.sort_by_plis(first_sort_color_top)
    elif form == "aiguillons":
       second_sort_form = service.sort_by_aiguillons(first_sort_color_top)
    else:
       second_sort_form = service.sort_by_no_lamelles_and_tubes(
           first_sort_color_top)

    if color_under == "blanc":
        third_sort_color_under = service.sort_by_color_under_white(second_sort_form)
    elif color_under == "jaune":
        third_sort_color_under = service.sort_by_color_under_yellow(second_sort_form)
    elif color_under == "brun":
        third_sort_color_under = service.sort_by_color_under_brown(second_sort_form)
    elif color_under == "rouge":
        third_sort_color_under = service.sort_by_color_under_red(second_sort_form)
    else:
        third_sort_color_under = service.sort_by_color_under_other(
            second_sort_form)

    if ring == "oui":
        final_results = service.sort_by_ring(third_sort_color_under)
    else:
        final_results = service.sort_by_not_ring(third_sort_color_under)

    mushrooms = service.sort_out_user_favorite_mushrooms(final_results, user)
    context = service.set_final_engine_context(
        color_top, form, color_under, ring, final_results)
    return TemplateResponse(request, "engine_results.html", context)

@login_required()
def add_or_remove_favorite(request, mushroom_id):
    """Add or remove a product in favorites list by clicking on heart"""

    user = request.user
    mushroom = service.get_mushroom(mushroom_id)
    service.add_or_remove_favorite(mushroom, user)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required()
def favorites_list(request):
    """Display the favorites product list page of the user"""

    user = request.user
    favorites = user.favorites.all()
    favorites = service.sort_out_user_favorite_mushrooms(favorites, user)
    context = service.set_mushrooms_context(favorites)
    return render(request, "favorites.html", context)
