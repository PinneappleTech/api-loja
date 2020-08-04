# api-loja

## GERAR SECRET_KEY
1. Comando para gerar secret_key django
```python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'```

## COMO RODAR
1. Para rodar é necessario ter o Docker e o docker-compose instalados
2. Após isso basta executar o comando
    ```docker-compose up```
3. e os containeres serão criados e executados.
4. Assim que a aplicação estiver rodando, para executar comandos no container da aplicação
5. execute comandos assim
6. para criar as tabelas no banco de dados
    ```docker-compose run web python manage.py migrate```
7. assim que as tabelas forem migradas
8. basta criar um superusuario com
    ```docker-compose run web python manage.py createsuperuser```
9. entrar com os dados e pronto.

# Rotas da API

## Rotas de Autenticação
**POST Login - /auth/login/**
>{ "username":"", "password":"" }

**POST Registro - /auth/registration/**
>{ "username":"", "email":"", "password1":"", "password2":"" }

**POST Logout - /auth/logout/**
>{ "token":"" }


## Rotas de Usuarios
**GET Usuarios - /api1/usuarios/**

**GET Usuario - /api1/usuarios/id/**

**POST Usuario - /api1/usuarios/**
Campos Obrigatorios ao enviar POST
>{ "username":"",
>   "password":"",
>   "tipo_usuario":"", #tipos: 1-vendedor, 2-caixa, 3-supervisor, 4-administrador
>   "sexo":"", #opções: M-masculino, F-feminino
>   "cpf":""
>}

**PUT Usuario - /api1/usuarios/id/**

**DELETE Usuario - /api1/usuarios/id/**


## Rotas de Clientes
**GET Clientes - /api1/clientes/**

**GET Cliente - /api1/clientes/id/**

**POST Cliente - /api1/clientes/**
>{  "nome":"",
>   "cpf":"",
>   "sexo":"", #Opções: M-masculino, F-feminino
>   "data_nasc":"", #Formato: aaaa-mm-dd
>   "fone":"",
>   "estado_civil":"", #Opções: 1-casado, 2-divorciado, 3-separado, 4-solteiro, 5-viuvo
>   "credito":"",
>   "endereco": {
>       "logradouro":"",
>       "bairro":"",
>       "cep":"",
>       "uf":"",
>       "cidade":""
>    }
>}

**PUT Cliente - /api1/clientes/id/**

**DELETE Cliente - /api1/clientes/id/**