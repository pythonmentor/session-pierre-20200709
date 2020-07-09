from django.shortcuts import render

from .models import Product

# Create your views here.
def search_results(request):
    name = request.GET.get("query")
    # récupérer la recherche effectuée oar l'utilisateur
    product, substitutes = Product.objects.search_substitutes(name)

    # ...
    return render(
        request,
        "results.html",
        {"product": product, "substitutes": substitutes},
    )

