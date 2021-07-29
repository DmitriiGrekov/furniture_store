from unidecode import unidecode
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from .forms import ReviewFormAdd
from .models import ReviewsFiles, RubricCompany, ReviewsCompany

# Для обработки сигналов
from .review_signal import review_add


def company_view(request, slug):
    context = {"rubrics": RubricCompany.objects.all().order_by('-name')}
    context['title_link'] = 'about'
    return render(request, f"company/company_{slug}.html", context)


class ReviewsList(ListView):
    template_name = 'company/otzyvy.html'
    queryset = ReviewsCompany.objects.all()
    context_object_name = 'reviews'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = RubricCompany.objects.all().order_by('-name')
        return context


class ReviewsDetail(DetailView):
    template_name = 'company/reviews_detail.html'
    model = ReviewsCompany
    context_object_name = 'review'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = RubricCompany.objects.all().order_by('-name')
        return context


# def create_review_view(requets):
#     if requets.method == 'POST':
#         form = ReviewFormAdd(requets.POST, requets.FILES )
#         if form.is_valid():
#     else:
#         form = ReviewFormAdd()
#         return render(requets, 'company/create_review.html', {'form': form})


@login_required
def create_review_view(request):
    if request.method == "POST":
        form = ReviewFormAdd(request.POST, request.FILES)
        if form.is_valid:
            form = form.save(commit=False)
            form.slug = slugify(unidecode(form.name), unidecode(form.company))
            form.save()
            review_add.send(form, review=form)
            files = request.FILES.getlist('files')
            print(form)
            for f in files:
                new_file = ReviewsFiles(files=f)
                new_file.save()
                form.files.add(new_file)
            form.save()
            return redirect('company:otzyvy')
    else:
        form = ReviewFormAdd()
        return render(request, 'company/create_review.html', {'form': form})
