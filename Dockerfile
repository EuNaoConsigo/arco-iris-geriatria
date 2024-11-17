# Usar uma imagem base com Python 3
FROM python:3.11-slim

# Definir diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema necessárias para compilar algumas bibliotecas Python (se necessário)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Criar um ambiente virtual para evitar o uso de pip como root
RUN python3 -m venv /venv

# Definir o ambiente para usar o venv
ENV PATH="/venv/bin:$PATH"

# Copiar o arquivo de dependências
COPY requirements.txt /app/

# Instalar as dependências no ambiente virtual
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para o contêiner
COPY . /app/

# Definir variáveis de ambiente
ENV PYTHONUNBUFFERED 1

# Coletar arquivos estáticos para produção
RUN python manage.py collectstatic --noinput

RUN python manage.py migrate
# Expor a porta que o servidor vai rodar
EXPOSE 8000

# Comando para rodar o servidor em produção
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]
