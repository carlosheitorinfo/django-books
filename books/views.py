# Importa as classes genéricas de views baseadas em classe do Django
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
# Importa o mixin para controle de permissões nas views
from django.contrib.auth.mixins import PermissionRequiredMixin
# Importa a função de logout para encerrar a sessão do usuário
from django.contrib.auth import logout
# Importa o modelo Book definido na aplicação
from .models import Book
# Importa a função para gerar URLs reversas com base nos nomes das rotas
from django.urls import reverse_lazy
# Importa os modelos User e Group para manipulação de usuários e grupos
from django.contrib.auth.models import User, Group
# Importa funções adicionais para manipulação de objetos e redirecionamento
from django.shortcuts import get_object_or_404, redirect
# Importa o decorador para verificar permissões em views baseadas em função
from django.contrib.auth.decorators import permission_required

# Define uma view para listar os livros
class BookListView(ListView):
    # Define o modelo associado à view
    model = Book
    # Define o template que será usado para renderizar a lista de livros
    template_name = 'books/book_list.html'

    # Sobrescreve o método para filtrar os livros com base nas permissões do usuário
    def get_queryset(self):
        # Obtém o queryset padrão
        qs = super().get_queryset()
        # Verifica se o usuário tem permissão para visualizar livros
        if self.request.user.has_perm('books.view_book'):
            # Se o usuário pertence ao grupo "Reader" e não é staff, filtra apenas os livros publicados
            if self.request.user.groups.filter(name='Reader').exists() and not self.request.user.is_staff:
                return qs.filter(published=True)
            # Caso contrário, retorna todos os livros
            return qs
        # Se o usuário não tem permissão, retorna um queryset vazio
        return qs

# Define uma view para criar novos livros, exigindo permissão específica
class BookCreateView(PermissionRequiredMixin, CreateView):
    # Define o modelo associado à view
    model = Book
    # Define os campos do modelo que serão exibidos no formulário
    fields = ['title','author','published']
    # Define a permissão necessária para acessar esta view
    permission_required = 'books.add_book'
    # Define a URL de sucesso após a criação do livro
    success_url = reverse_lazy('books:list')

# Define uma view para atualizar livros existentes, exigindo permissão específica
class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = ['title','author','published']
    permission_required = 'books.change_book'
    success_url = reverse_lazy('books:list')

# Define uma view para deletar livros, exigindo permissão específica
class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = Book
    permission_required = 'books.delete_book'
    success_url = reverse_lazy('books:list')

# Define uma view baseada em função para publicar um livro, exigindo permissão específica
@permission_required('books.publish_book', raise_exception=True)
def publish_book(request, pk):
    # Obtém o livro pelo ID ou retorna 404 se não encontrado
    book = get_object_or_404(Book, pk=pk)
    # Marca o livro como publicado
    book.published = True
    # Salva as alterações no banco de dados
    book.save()
    # Redireciona para a página de detalhes do livro
    return redirect('books:detail', pk=pk)

# Define uma função para adicionar um usuário ao grupo "Editor"
def add_to_editor(request, user_id):
    # Obtém o usuário pelo ID
    u = User.objects.get(id=user_id)
    # Obtém o grupo "Editor"
    group = Group.objects.get(name='Editor')
    # Adiciona o usuário ao grupo
    u.groups.add(group)

# Define uma view para realizar o logout do usuário
def logout_view(request):
    # Realiza o logout do usuário, encerrando a sessão
    logout(request)    
    # Redireciona para a página inicial
    return redirect('/')