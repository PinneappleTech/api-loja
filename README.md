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
