import mysql.connector

class DatabaseConnection:
    def __init__(self, host, user, password, database, port='3306'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert_data(self, query, data):
        self.cursor.executemany(query, data)
        self.connection.commit()

class DataTransfer:
    def __init__(self, source_db, destination_db):
        self.source_db = source_db
        self.destination_db = destination_db

    def transfer_data(self, select_query, insert_query, batch_size=100):
        self.source_db.connect()
        self.destination_db.connect()

        source_data = self.source_db.execute_query(select_query)

        batch = []
        for i, row in enumerate(source_data, 1):
            batch.append(row)

            if i % batch_size == 0 or i == len(source_data):
                self.destination_db.insert_data(insert_query, batch)
                batch = []

                progress = i / len(source_data) * 100
                print(f"Progresso: {progress:.2f}%")

        self.source_db.disconnect()
        self.destination_db.disconnect()

# Configurações da fonte de dados (origem)
source_db_config = {
    'host': '',
    'user': '',
    'password': '',
    'database': ''
}

# Configurações do destino
destination_db_config = {
    'host': '',
    'port': '',
    'user': '',
    'password': '',
    'database': ''
}

# Crie objetos de conexão de banco de dados
source_db = DatabaseConnection(**source_db_config)
destination_db = DatabaseConnection(**destination_db_config)

# Consulta SQL para selecionar dados da tabela de origem
select_query = "SELECT coluna1, coluna2, coluna3, coluna4, coluna5, coluna6 FROM schema.tabela"

# Instrução SQL para inserir em lote na tabela de destino
insert_query = "INSERT INTO schema.tabela (coluna1, coluna2, coluna3, coluna4, coluna5, coluna6) VALUES (%s, %s, %s, %s, %s, %s)"

data_transfer = DataTransfer(source_db, destination_db)
data_transfer.transfer_data(select_query, insert_query)
