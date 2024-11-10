# Usar uma imagem base com Python 3
FROM python:3.11-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos de dependências
COPY requirements.txt /app/

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para o contêiner
COPY . /app/

# Definir variáveis de ambiente
ENV PYTHONUNBUFFERED 1

# Coletar arquivos estáticos para produção
RUN python manage.py collectstatic --noinput

# Expor a porta que o servidor vai rodar
EXPOSE 8000

# Comando para rodar o servidor em produção
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "your_project_name.wsgi:application"]
