import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, port, database):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            port=port,
            database=database,
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def sql_request(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Error as e:
        print(f"The error '{e}' occurred")

connection = create_connection("mysql-rfam-public.ebi.ac.uk", "rfamro", "", "4497", "Rfam")
sql_request_query = """SELECT fr.rfam_acc, fr.rfamseq_acc, fr.seq_start, fr.seq_end
FROM full_region fr, rfamseq rf, taxonomy tx
WHERE rf.ncbi_id = tx.ncbi_id
AND fr.rfamseq_acc = rf.rfamseq_acc
AND tx.ncbi_id = 10116 -- NCBI taxonomy id of Rattus norvegicus
AND is_significant = 1 -- exclude low-scoring matches from the same clan"""
sql_request(connection, sql_request_query)
