import MySQLdb
host = 'localhost'
user = 'root'
password = '252627'
db = 'escola'
port = 3306

conection = MySQLdb.connect(host, user, password, db, port)

c = conection.cursor()

def select(fields, tables, where=None):

    query = 'SELECT ' + fields + ' FROM ' + tables
    if(where):
        query = query + ' WHERE ' + where
    c.execute(query)
    return c.fetchall()

print(select('nome, cpf', 'alunos', 'id_aluno = 1'))