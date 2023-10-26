import mysql.connector

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

# Conecta ao banco de dados de origem
source_conn = mysql.connector.connect(**source_db_config)
source_cursor = source_conn.cursor()

# Conecta ao banco de dados de destino
destination_conn = mysql.connector.connect(**destination_db_config)
destination_cursor = destination_conn.cursor()

# Consulta SQL para selecionar dados da tabela de origem
select_query = "SELECT coluna1, coluna2, coluna3, coluna4, coluna5, coluna6 FROM schema.tabela"

# Execute a consulta na base de dados de origem
source_cursor.execute(select_query)

# Recupere os resultados da consulta
result_set = source_cursor.fetchall()

# Inserir em lotes
batch_size = 100  # Número de linhas por lote
batch = []

for i, row in enumerate(result_set, 1):
    batch.append(row)

    if i % batch_size == 0 or i == len(result_set):
        # Instrução SQL para inserir em lote
        insert_query = "INSERT INTO schema.tabela (coluna1, coluna2, coluna3, coluna4, coluna5, coluna6) VALUES (%s, %s, %s, %s, %s, %s)"

        # Execute a instrução de inserção em lote
        destination_cursor.executemany(insert_query, batch)
        batch = []  # Limpe o lote para a próxima iteração

        # Exibir progresso
        progress = i / len(result_set) * 100
        print(f"Progresso: {progress:.2f}%")

# Commit das alterações na base de dados de destino
destination_conn.commit()

# Feche as conexões
source_cursor.close()
source_conn.close()
destination_cursor.close()
destination_conn.close()
