from django.contrib import admin
from .models import UsefullInfo


class UsefullInfoAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)


admin.site.register(UsefullInfo, UsefullInfoAdmin)
