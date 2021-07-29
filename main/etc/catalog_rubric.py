from catalog.models import Category 

def catalog_category(request):
    context = {}
    context['rubric_catalog'] = Category.objects.all()
    return context