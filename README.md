PT-BR

in English [Data Transfer Script(# Data Transfer Script)

# Script de Transferência de Dados

Este script em Python foi desenvolvido para transferir dados de um banco de dados MySQL de origem para um banco de dados MySQL de destino. Ele é capaz de realizar essa transferência entre servidores MySQL distintos e suporta inserção em lotes para melhorar o desempenho.

## Requisitos

- Python 3.9
- Biblioteca `mysql-connector-python` (instalada com `pip install mysql-connector-python`)

## Utilização

1. Clone o repositório ou copie o conteúdo do script para o seu ambiente.

2. Edite as configurações de conexão no script, especificando os detalhes do banco de dados de origem e de destino.

3. Defina as consultas SQL de seleção e inserção para a sua situação específica. Certifique-se de que as tabelas de origem e de destino tenham a mesma estrutura de colunas.

4. Execute o script com o comando `python data_transfer.py`.

O script realizará a transferência de dados do banco de dados de origem para o banco de dados de destino. O progresso será exibido à medida que as linhas são inseridas.

## Personalização

Você pode personalizar o script de acordo com suas necessidades:

- Ajuste o tamanho do lote (`batch_size`) para otimizar o desempenho, dependendo da quantidade de dados a ser transferida.

- Modifique as consultas SQL de seleção e inserção para corresponder às tabelas e colunas específicas do seu banco de dados.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para melhorar este script e enviar um pedido de pull.

## Autor

Bernardo Nacif

## Licença

Este script é disponibilizado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.

---
# Data Transfer Script

This Python script is designed to transfer data from a source MySQL database to a destination MySQL database. It can transfer data between distinct MySQL servers and supports batch insertion for improved performance.

## Requirements

- Python 3.9
- `mysql-connector-python` library (installed with `pip install mysql-connector-python`)

## Usage

1. Clone the repository or copy the script content to your environment.

2. Edit the connection settings in the script, specifying the details of the source and destination databases.

3. Set the SQL queries for selection and insertion to match your specific situation. Ensure that the source and destination tables have the same column structure.

4. Run the script using the command `python data_transfer.py`.

The script will perform the data transfer from the source database to the destination database. Progress will be displayed as rows are inserted.

## Customization

You can customize the script according to your needs:

- Adjust the batch size (`batch_size`) to optimize performance based on the amount of data to be transferred.

- Modify the SQL queries for selection and insertion to match the specific tables and columns in your database.

## Contributions

Contributions are welcome! Feel free to enhance this script and submit a pull request.

## Author

Bernardo Nacif

## License

This script is provided under the MIT. See the LICENSE file for more information.

---
