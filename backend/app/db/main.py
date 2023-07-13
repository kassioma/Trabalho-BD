import pymysql

def openConnection():
    dbData = {
        'hostname': 'mysql',
        'port': 3306,
        'username': 'root',
        'password': '123456',
        'database': 'projetoBd'
    }
    conn = pymysql.connect(host=dbData['hostname'], port=dbData['port'], user=dbData['username'], passwd=dbData['password'], database=dbData['database'])
    return conn

def executeInsert(listaValues, listaKeys, tabela):
    conn = openConnection()
    with conn.cursor() as cursor:
        cursor.execute(f'INSERT INTO {tabela} ({",".join(listaKeys)}) VALUES ({",".join(listaValues)})')
    conn.commit()
    conn.close()

def executeInsertPhoto(filepath, tabela, matricula):
    conn = openConnection()
    with conn.cursor() as cursor:
        print(f"UPDATE {tabela} SET imagem = LOAD_FILE('{filepath}') WHERE matricula = {matricula}")
        cursor.execute(f"UPDATE {tabela} SET imagem = LOAD_FILE('{filepath}') WHERE matricula = {matricula}")
    conn.commit()
    conn.close()