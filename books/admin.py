# books/admin.py
# Importa o módulo admin do Django, usado para registrar modelos no site de administração
from django.contrib import admin
# Importa o modelo Book definido na aplicação
from .models import Book

# Registra o modelo Book no site de administração com uma configuração personalizada
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Define os campos que serão exibidos na lista de objetos no admin
    list_display = ('title','author','published','created_at')
    # Define ações customizadas disponíveis no admin
    actions = ['make_published']

    # Sobrescreve o método para personalizar o queryset exibido no admin
    def get_queryset(self, request):
        # Obtém o queryset padrão
        qs = super().get_queryset(request)
        # Se o usuário for superusuário, retorna todos os objetos
        if request.user.is_superuser:
            return qs
        # Caso contrário, retorna o queryset padrão (editors veem tudo, leitores não acessam o admin)
        return qs

    # Define permissões de alteração para o modelo no admin
    def has_change_permission(self, request, obj=None):
        # Permite alterações se o usuário for superusuário
        if request.user.is_superuser:
            return True
        # Permite alterações se o usuário pertencer ao grupo "Editor"
        if request.user.groups.filter(name='Editor').exists():
            return True
        # Caso contrário, nega a permissão
        return False

    # Define permissões de exclusão reutilizando as permissões de alteração
    def has_delete_permission(self, request, obj=None):
        return self.has_change_permission(request, obj)

    # Define uma ação customizada para publicar livros selecionados
    def make_published(self, request, queryset):
        # Atualiza o campo "published" para True nos objetos selecionados
        updated = queryset.update(published=True)
        # Exibe uma mensagem de sucesso no admin
        self.message_user(request, f"{updated} livro(s) publicados.")
    # Define a descrição da ação customizada exibida no admin
    make_published.short_description = "Publicar livros selecionados"
