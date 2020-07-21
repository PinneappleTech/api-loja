# api-loja

#####COMO RODAR
1 - Para rodar é necessario ter o Docker e o docker-compose instalados
2 - Após isso basta executar o comando
    docker-compose up
3 - e os containeres serão criados e executados.
4 - Assim que a aplicação estiver rodando, para executar comandos no container da aplicação
5 - execute comandos assim
6 - para criar as tabelas no banco de dados
    docker-compose run web python manage.py migrate
7 - assim que as tabelas forem migradas
8 - basta criar um superusuario com
    docker-compose run web python manage.py createsuperuser
9 - entrar com os dados e pronto.

# Rotas da API

##### Rotas de Autenticação
POST Login - /auth/login/
        {
            "username":"",
            "password":""
        }

POST Registro - /auth/registration/
        {
            "username":"",
            "email":"",
            "password1":"",
            "password2":""
        }

POST Logout - /auth/logout/
        {
            "token":""
        }

###### Rotas de Usuarios
GET Usuarios - /api1/usuarios/
GET Usuario - /api1/usuarios/<pk>/
POST Usuario - /api1/usuarios/
PUT Usuario - /api1/usuarios/<pk>/
DELETE Usuario - /api1/usuarios/<pk>/

###### Rotas de Clientes
GET Clientes - /api1/clientes/
GET Cliente - /api1/clientes/<pk>/
POST Cliente - /api1/clientes/
PUT Cliente - /api1/clientes/<pk>/
DELETE Cliente - /api1/clientes/<pk>/