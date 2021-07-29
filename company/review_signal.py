from django.dispatch import Signal


def review_dispatch_add(sender, **kwargs):
    print(f"Отзыв от пользователя {kwargs['review'].name} создан")


review_add = Signal(providing_args=['review'])
review_add.connect(review_dispatch_add)
