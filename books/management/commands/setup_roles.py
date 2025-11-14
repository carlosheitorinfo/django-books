# books/management/commands/setup_roles.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.apps import apps

class Command(BaseCommand):
    help = "Create groups: Administrator, Editor, Reader and assign permissions"

    def handle(self, *args, **options):
        Book = apps.get_model('books', 'Book')

        # pega todas as permissões do model Book
        perms = Permission.objects.filter(content_type__app_label='books',content_type__model='book')

        perm_map = {p.codename: p for p in perms}

        # Editor
        editor, created = Group.objects.get_or_create(name='Editor')
        editor_perms = ['add_book', 'change_book', 'delete_book', 'view_book', 'publish_book']
        editor.permissions.set([perm_map[c] for c in editor_perms if c in perm_map])

        # Reader
        reader, created = Group.objects.get_or_create(name='Reader')
        if 'view_book' in perm_map:
            reader.permissions.set([perm_map['view_book']])

        # Administrator (grupo com todas perm de books)
        admin_group, created = Group.objects.get_or_create(name='Administrator')
        admin_group.permissions.set(list(perms))

        self.stdout.write(self.style.SUCCESS("Groups created/updated."))
