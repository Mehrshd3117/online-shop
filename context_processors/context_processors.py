from product.models import Category


def category(request):
    categories = Category.objects.filter(child=False)

    return {'categories': categories}
