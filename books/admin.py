# books/admin.py
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','published','created_at')
    actions = ['make_published']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # editors (membros do grupo) veem tudo no admin; leitores não devem acessar admin
        return qs

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if request.user.groups.filter(name='Editor').exists():
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return self.has_change_permission(request, obj)

    def make_published(self, request, queryset):
        updated = queryset.update(published=True)
        self.message_user(request, f"{updated} livro(s) publicados.")
    make_published.short_description = "Publicar livros selecionados"
