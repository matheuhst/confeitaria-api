import psycopg2

def get_conexao():
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='matheus726',
        host='db.yfjtvltaxbxrtzizagkk.supabase.co',
        port='5432'
    )
    return conn
    