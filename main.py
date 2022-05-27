import sqlite3 as connector
import datetime
from Pessoa import Pessoa

pessoa = Pessoa('08277083351', 'Gustavo', '2002-03-19', True)

conexao = connector.connect('./conexao_banco_dados_python.db')
cursor = conexao.cursor();

comando1 = '''
                CREATE TABLE Pessoa(
                    id INTEGER NOT NULL,
                    cpf VARCHAR(11) NOT NULL,
                    nome TEXT NOT NULL,
                    data_nascimento DATE NOT NULL,
                    usa_oculos BOOLEAN NOT NULL,

                    PRIMARY KEY(id)
                );
            '''

cursor.execute(comando1)
conexao.commit()
conexao.close()


comando2 =  '''
                INSERT INTO Pessoa(cpf, nome, data_nascimento, usa_oculos)
                VALUES (:cpf, :nome, :data_nascimento, :usa_oculos);
            '''

cursor.execute(comando2, ('08277083351', 'Gustavo', '2002-03-19', True))
conexao.commit()
conexao.close()