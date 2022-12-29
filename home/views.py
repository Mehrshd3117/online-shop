# Django packages
from django.shortcuts import render
from django.views import View
# Local apps
from product.models import Category


class HomeView(View):
    def get(self, request):
        categories = Category.objects.filter(child=False)

        context = {'categories': categories}
        return render(request, 'home/index.html', context)
