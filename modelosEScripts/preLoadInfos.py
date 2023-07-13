import pymysql
import pandas

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

def loadFile(path):
    df = pandas.read_csv(path)
    return df

def insertBd(df, conn, table):
    with conn.cursor() as cursor:
        match table:
            case "departamentos":
                for index, frame in df.iterrows():
                    cursor.execute(f'INSERT INTO {table} VALUES ({frame["cod"]}, "{frame["nome"]}")')
                    print(f'Inserido o departamento de {frame["nome"]} com o código {frame["cod"]}')
            case "disciplinas":
                for index, frame in df.iterrows():
                    cursor.execute(f'INSERT INTO {table} VALUES ("{frame["cod"]}", "{frame["nome"]}", {frame["cod_depto"]})')
                    print(f'Inserindo a disciplina {frame["nome"]} com o código {frame["cod"]} do departamento {frame["cod_depto"]}')
            case "turmas":
                for index, frame in df.iterrows():
                    frame["total_vagas"] = 0 if str(frame["total_vagas"]) == "nan" else frame["total_vagas"]
                    cursor.execute(f'INSERT INTO {table} VALUES ({index}, {frame["cod_depto"]}, "{frame["cod_disciplina"]}", "{frame["turma"]}", "{frame["periodo"]}", "{frame["professor"]}", "{frame["horario"]}", {frame["vagas_ocupadas"]}, {frame["total_vagas"]}, "{frame["local"]}")')
                    print(f'Inserindo turma {frame["turma"]} do indice {index} da disciplina {frame["cod_disciplina"]} do professor {frame["professor"]}')
    conn.commit()

if __name__ == '__main__':
    conn = openConnection()
    dfDep = loadFile("../csvs/departamentos_2023-1.csv")
    dfDisc = loadFile("../csvs/disciplinas_2023-1.csv")
    dfTur = loadFile("../csvs/turmas_2023-1.csv")
    insertBd(dfDep, conn, "departamentos")
    insertBd(dfDisc, conn, "disciplinas")
    insertBd(dfTur, conn, "turmas")