# 1. Use uma base de imagem completa (Ubuntu 22.04 LTS)
FROM ubuntu:22.04

# 2. Adicionar metadados
LABEL maintainer="Weder Sousa <weder96@gmail.com>"
LABEL version="2.0"

# 3. Configurar variáveis de ambiente e fuso horário sem interação
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    TZ=America/Sao_Paulo

# 4. Instalar todas as dependências em uma única camada (RUN) para otimizar
#    - Instala Java 17, Python 3, Pip e Git.
#    - Limpa o cache do apt no final para reduzir o tamanho da imagem.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    openjdk-17-jre-headless \
    python3 \
    python3-pip \
    git && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    rm -rf /var/lib/apt/lists/*

# 5. Instalar todas as bibliotecas Python em uma única camada
RUN pip3 install --no-cache-dir jupyterlab jupyterlab-git jupyterthemes scipy \
    SQLAlchemy missingno json_tricks gensim elasticsearch psycopg2-binary pymc3 apyori msgpack

# 6. Configurar o tema do Jupyter
RUN jt -t grade3

# 7. Configurar ambiente de trabalho e expor a porta
ENV SHARED_WORKSPACE=/opt/workspace
RUN mkdir -p ${SHARED_WORKSPACE} && mkdir -p /root/GitProjects
WORKDIR /root/GitProjectsdocker push
EXPOSE 8888

# 8. Comando para iniciar o Jupyter Lab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]