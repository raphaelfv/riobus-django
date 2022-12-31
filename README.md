## Instalação

* Criar virtual env

```
python3 -m venv myvenv
```

* Instalar dependências 

```
. myvenv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py migrate --run-syncdb
```

* Para usar a biblioteca `basedosdados`, é necessário ter um projeto criado no Google Cloud. Documentação original: https://github.com/basedosdados/mais#acesse-uma-tabela

1. Acesso o link https://console.cloud.google.com/projectselector2/home/dashboard
2. Aceite os termos de serviço
3. Clique em Create Project
4. Adicione um nome para seu projeto
5. Clique em Create
6. Clique no nome do seu projeto para abrir o dashboard do mesmo. No canto superior direito, clique nos 3 pontos verticais e selecione a opção "Configurações do projeto"
7. Nessa tela, será possível ver um campo "Número do projeto". Este número que será necessário para adicionar no arquivo .env

* Criar arquivo .env

O repositório contém um arquivo .env.exemplo, copie este arquivo para um arquivo com nome .env e corrija as variáveis para seus dados de projeto. 

## Uso

* Ambiente 

```
. myvenv/bin/activate
python manage.py runserver
```

Acessar em um navegador o endereço 127.0.0.1:8000

## Referências

* https://github.com/basedosdados/mais#usando-em-python
* https://www.data.rio/documents/PCRJ::transporte-rodovi%C3%A1rio-gps-dos-%C3%B4nibus/about
* https://www.data.rio/
* https://github.com/RioBus/
* https://console.cloud.google.com/projectselector2/home/dashboard