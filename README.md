## Instalação

### Docker

```
sudo  apt-get install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# Substituir focal (Ubuntu 20.04) por xenial se for ubuntu 18.04 (ou equivalente para outras versoes)
sudo  add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
sudo  apt-get update
sudo  apt-get install docker-ce

sudo  curl -L https://github.com/docker/compose/releases/download/1.20.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

sudo groupadd docker
sudo usermod -aG docker $USER
```

### Build de imagens

```
docker-compose build
docker-compose up
```

### Google-bigquery
* Para usar a biblioteca `basedosdados`, é necessário ter um projeto criado no Google Cloud. Documentação original: https://github.com/basedosdados/mais#acesse-uma-tabela

1. Acesso o link https://console.cloud.google.com/projectselector2/home/dashboard
2. Aceite os termos de serviço
3. Clique em Create Project
4. Adicione um nome para seu projeto
5. Clique em Create
6. Clique no nome do seu projeto para abrir o dashboard do mesmo. No canto superior direito, clique nos 3 pontos verticais e selecione a opção "Configurações do projeto"
7. Nessa tela, será possível ver um campo "Número do projeto". Este número que será necessário para adicionar no arquivo .env

TODO - token de autorizacao para docker

### Criar arquivo .env

O repositório contém um arquivo .env.exemplo, copie este arquivo para um arquivo com nome .env e corrija as variáveis para seus dados de projeto. 

### Criar SECRET_KEY

```
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

## Uso

* Ambiente 

```
docker-compose up
```

Acessar em um navegador o endereço 127.0.0.1:8000 para a API e 127.0.0.1:5173 para o mapa

## Debugger

```
mkdir .vscode
cp launch.json .vscode/launch.json
```

## Referências

* https://github.com/basedosdados/mais#usando-em-python
* https://www.data.rio/documents/PCRJ::transporte-rodovi%C3%A1rio-gps-dos-%C3%B4nibus/about
* https://www.data.rio/
* https://github.com/RioBus/
* https://console.cloud.google.com/projectselector2/home/dashboard