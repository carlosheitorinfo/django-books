# Django Livros Permission

Este projeto é uma aplicação Django para gerenciar livros com permissões específicas para diferentes grupos de usuários.

## Requisitos

- Python 3.8 ou superior
- Django 5.2
- Um ambiente virtual configurado

## Instruções de Instalação

Siga os passos abaixo para configurar e executar o projeto:

### 1. Clone o repositório

```bash
git clone https://github.com/ricardoazeredo/django-livros-permission.git
cd django-livros-permission
```

### 2. Crie e ative um ambiente virtual

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

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados

Crie as migrações e aplique-as:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crie um superusuário

```bash
python manage.py createsuperuser
```

Siga as instruções no terminal para definir o nome de usuário, e-mail e senha.

### 6. Configure os grupos e permissões

Para configurar os grupos e permissões, siga os passos abaixo:

1. Certifique-se de que o ambiente virtual está ativado. Caso não esteja, ative-o:
   - **Windows**: `source .venv/Scripts/activate`
   - **Linux/Mac**: `source .venv/bin/activate`

2. Verifique se o banco de dados está configurado corretamente e as migrações foram aplicadas:
   ```bash
   python manage.py migrate
   ```
   Este comando garante que todas as tabelas necessárias, incluindo as de permissões, estejam criadas no banco de dados.

3. Execute o comando customizado para criar os grupos e permissões:
   ```bash
   python manage.py setup_roles
   ```
   Este comando irá:
   - Criar os grupos `Administrator`, `Editor` e `Reader`.
   - Associar as permissões adequadas a cada grupo, como definido no arquivo `setup_roles.py`.

4. Após a execução, você verá uma mensagem de sucesso no terminal confirmando que os grupos foram criados ou atualizados:
   ```
   Groups created/updated.
   ```

### 7. Inicie o servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse o projeto no navegador em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Explicação Detalhada

### Passo 1: Clonar o repositório

Este comando baixa o código do repositório GitHub e navega até o diretório do projeto.

### Passo 2: Criar e ativar o ambiente virtual

O ambiente virtual isola as dependências do projeto, garantindo que pacotes instalados não interfiram em outros projetos.

- **Windows**: Use `source .venv/Scripts/activate` para ativar o ambiente.
- **Linux/Mac**: Use `source .venv/bin/activate`.

### Passo 3: Instalar dependências

O comando `pip install -r requirements.txt` instala todas as bibliotecas necessárias listadas no arquivo `requirements.txt`.

### Passo 4: Configurar o banco de dados

- `python manage.py makemigrations`: Cria os arquivos de migração com base nos modelos definidos.
- `python manage.py migrate`: Aplica as migrações ao banco de dados, criando as tabelas necessárias.

### Passo 5: Criar um superusuário

O comando `createsuperuser` cria um administrador para acessar o painel de administração do Django.

### Passo 6: Configurar grupos e permissões

O comando customizado `setup_roles` cria os grupos `Administrator`, `Editor` e `Reader`, e associa as permissões adequadas a cada grupo.

### Passo 7: Iniciar o servidor de desenvolvimento

O comando `runserver` inicia o servidor local para testar a aplicação. Acesse o endereço [http://127.0.0.1:8000](http://127.0.0.1:8000) no navegador para visualizar o projeto.

---

Siga os passos acima para configurar e executar o projeto corretamente. Se encontrar problemas, verifique os requisitos e as configurações do ambiente.