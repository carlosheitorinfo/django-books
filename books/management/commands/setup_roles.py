# books/management/commands/setup_roles.py
# Importa a classe base para criar comandos customizados no Django
from django.core.management.base import BaseCommand
# Importa os modelos Group e Permission para manipular grupos e permissões
from django.contrib.auth.models import Group, Permission
# Importa a função para acessar modelos dinamicamente
from django.apps import apps

# Define a classe do comando customizado
class Command(BaseCommand):
    # Define uma mensagem de ajuda que descreve o propósito do comando
    help = "Create groups: Administrator, Editor, Reader and assign permissions"

    # Método principal que será executado quando o comando for chamado
    def handle(self, *args, **options):
        # Obtém o modelo Book dinamicamente
        Book = apps.get_model('books', 'Book')

        # Obtém todas as permissões associadas ao modelo Book
        perms = Permission.objects.filter(content_type__app_label='books',content_type__model='book')

        # Cria um dicionário para mapear os codenames das permissões aos objetos Permission
        perm_map = {p.codename: p for p in perms}

        # Cria ou obtém o grupo "Editor"
        editor, created = Group.objects.get_or_create(name='Editor')
        # Define as permissões específicas para o grupo "Editor"
        editor_perms = ['add_book', 'change_book', 'delete_book', 'view_book', 'publish_book']
        # Associa as permissões ao grupo "Editor" se elas existirem no dicionário
        editor.permissions.set([perm_map[c] for c in editor_perms if c in perm_map])

        # Cria ou obtém o grupo "Reader"
        reader, created = Group.objects.get_or_create(name='Reader')
        # Associa apenas a permissão de visualização ao grupo "Reader"
        if 'view_book' in perm_map:
            reader.permissions.set([perm_map['view_book']])

        # Cria ou obtém o grupo "Administrator"
        admin_group, created = Group.objects.get_or_create(name='Administrator')
        # Associa todas as permissões do modelo Book ao grupo "Administrator"
        admin_group.permissions.set(list(perms))

        # Exibe uma mensagem de sucesso no terminal após a execução do comando
        self.stdout.write(self.style.SUCCESS("Groups created/updated."))
