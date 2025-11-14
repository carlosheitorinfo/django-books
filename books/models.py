# books/models.py
# Importa o módulo models do Django, que contém classes base para definir modelos
from django.db import models

# Define o modelo Book, que representa um livro no sistema
class Book(models.Model):
    # Campo para armazenar o título do livro, com um limite máximo de 200 caracteres
    title = models.CharField(max_length=200)
    # Campo para armazenar o nome do autor do livro, também com um limite de 200 caracteres
    author = models.CharField(max_length=200)
    # Campo booleano para indicar se o livro foi publicado ou não, com valor padrão False
    published = models.BooleanField(default=False)
    # Campo para armazenar a data e hora de criação do registro, preenchido automaticamente
    created_at = models.DateTimeField(auto_now_add=True)

    # Classe interna para definir metadados do modelo
    class Meta:
        # Define uma permissão customizada chamada "publish_book" com uma descrição
        permissions = [
            ("publish_book", "Can publish book"),
        ]

    # Método especial para retornar uma representação em string do objeto
    def __str__(self):
        # Retorna o título do livro como representação do objeto
        return self.title
