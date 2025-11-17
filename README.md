# Django Livros Permission

Este projeto é uma aplicação Django para gerenciar livros com permissões específicas para diferentes grupos de usuários.

## Requisitos

- Python 3.8 ou superior
- Django 5.2
- Um ambiente virtual configurado

## Instruções de Instalação

Siga os passos abaixo para configurar e executar o projeto:

### 1. Crie e ative um ambiente virtual

No Windows:
```bash
python -m venv .venv
source .venv/Scripts/activate
```

No Linux/Mac:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure o banco de dados

Crie as migrações e aplique-as:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Crie um superusuário

```bash
python manage.py createsuperuser
```

Siga as instruções no terminal para definir o nome de usuário, e-mail e senha.

### 5. Configure os grupos e permissões

Para configurar os grupos e permissões, siga os passos detalhados abaixo:

1. **Ative o ambiente virtual**:
   Certifique-se de que o ambiente virtual está ativado para garantir que os pacotes e configurações do projeto sejam usados corretamente.
   - No **Windows**:
     ```bash
     source .venv/Scripts/activate
     ```
   - No **Linux/Mac**:
     ```bash
     source .venv/bin/activate
     ```

2. **Verifique as migrações do banco de dados**:
   Antes de configurar os grupos e permissões, é necessário garantir que o banco de dados esteja atualizado com as tabelas necessárias. Execute o comando abaixo:
   ```bash
   python manage.py migrate
   ```
   Este comando aplica todas as migrações pendentes, criando as tabelas necessárias para o funcionamento do sistema, incluindo as relacionadas a permissões.

3. **Entenda o comando `setup_roles`**:
   O comando `setup_roles` é um comando customizado definido no arquivo `books/management/commands/setup_roles.py`. Ele realiza as seguintes ações:
   - Cria três grupos de usuários: `Administrator`, `Editor` e `Reader`.
   - Associa permissões específicas a cada grupo:
     - **Administrator**: Todas as permissões relacionadas ao modelo `Book`.
     - **Editor**: Permissões para adicionar, alterar, excluir, visualizar e publicar livros.
     - **Reader**: Permissão apenas para visualizar livros.

4. **Execute o comando `setup_roles`**:
   Após garantir que o banco de dados está configurado, execute o comando abaixo para criar os grupos e associar as permissões:
   ```bash
   python manage.py setup_roles
   ```
   Este comando utiliza o modelo `Permission` do Django para configurar as permissões e associações de forma programática.

5. **Verifique a saída do comando**:
   Após a execução, você verá uma mensagem no terminal confirmando que os grupos foram criados ou atualizados com sucesso:
   ```
   Groups created/updated.
   ```
6. **Inicie o servidor de desenvolvimento**:

```bash
python manage.py runserver
```

Acesse o projeto no navegador em: [http://127.0.0.1:8000](http://127.0.0.1:8000)
7. **Confirme as configurações no admin**:
   Acesse o painel de administração do Django em [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) com o superusuário criado anteriormente. Navegue até a seção de grupos para verificar se os grupos `Administrator`, `Editor` e `Reader` foram criados e se as permissões estão associadas corretamente.

---

Siga os passos acima para configurar e executar o projeto corretamente. Se encontrar problemas, verifique os requisitos e as configurações do ambiente.