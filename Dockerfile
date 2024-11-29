# Base image com Python 3.9
FROM python:3.9-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos necessários para o container
COPY invoke.py .
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Configurar variáveis de ambiente para o LocalStack
ENV AWS_ACCESS_KEY_ID="test"
ENV AWS_SECRET_ACCESS_KEY="test"
ENV AWS_DEFAULT_REGION="us-east-1"

# Comando padrão ao iniciar o container
CMD ["python", "invoke.py"]