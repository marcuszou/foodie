# sandbox/views.py
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, View

from recipes.models import Recipe
from sandbox.forms import FeedbackForm

# Function based View
## data = ["Pizza", "Pasta", "Salad", "Bread"]
## context = {"foods", data}
data = Recipe.objects.all()
context = {"recipes": data}
# Create your views here.
def index(request):
    return render(request, "sandbox/index.html", context)

# Class-based View
class RecipeListView(ListView):
    model = Recipe
    template_name = "sandbox/index.html"
    context_object_name = "recipes"
    
    def get_queryset(self):
        filtered_recipes = Recipe.objects.filter(category__name_iexact="Salad")
        return filtered_recipes
    
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "sandbox/recipeDetail.html"
    context_object_name = "recipe"

def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # process the form
            print(form.cleaned_data)
            return redirect('thank_you')
        
    else:
        form = FeedbackForm()
        context = {"form": form}
        return render(request, "sandbox/feedbacK_form.html", context)


## Customized View
class SpecificRecipesView(View):
    def get(self, request, *args, **kwargs):
        ## fetch recipes with "refreshing" in the description
        refreshing_recipes = Recipe.objects.filter(description__icontains="refreshing")
        context = {"refreshing": refreshing_recipes}
        return render(request, 'sandbox/refreshing_recipes.html', context)