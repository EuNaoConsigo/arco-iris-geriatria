FROM python:3.9-slim

# Definir o diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema necessárias
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copiar o arquivo de requisitos para o container
COPY requirements.txt /app/

# Atualizar o pip e instalar as dependências do requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar o código do seu projeto para o container
COPY . /app/

# Rodar comandos para aplicar migrações, coletar arquivos estáticos e iniciar o Gunicorn
CMD ["bash", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn core.wsgi:application --bind 0.0.0.0:8000"]
