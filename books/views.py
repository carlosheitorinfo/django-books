# books/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import logout
from .models import Book
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    # leitores e acima podem ver; mas para leitores, filtrar published=True
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.has_perm('books.view_book'):
            # leitores veem só publicados; staff/editor/admin podem ver tudo se desejar
            if self.request.user.groups.filter(name='Reader').exists() and not self.request.user.is_staff:
                return qs.filter(published=True)
            return qs
        return qs.none()

class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    fields = ['title','author','published']
    permission_required = 'books.add_book'
    success_url = reverse_lazy('books:list')

class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = ['title','author','published']
    permission_required = 'books.change_book'
    success_url = reverse_lazy('books:list')

class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = Book
    permission_required = 'books.delete_book'
    success_url = reverse_lazy('books:list')

# Exemplo de view para 'publicar' usando perm customizada
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required

@permission_required('books.publish_book', raise_exception=True)
def publish_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.published = True
    book.save()
    return redirect('books:detail', pk=pk)

def add_to_editor(request, user_id):
    u = User.objects.get(id=user_id)
    group = Group.objects.get(name='Editor')
    u.groups.add(group)
    
def logout_view(request):
    # Realiza o logout do usuário, encerrando a sessão.
    logout(request)    
    return redirect('/')