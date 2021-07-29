from company.models import ReviewsCompany


def show_random_review(request):
    reviews = ReviewsCompany.objects.all().order_by('?')[:2]
    return {'random_reviews': reviews}