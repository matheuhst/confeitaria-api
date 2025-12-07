from conexao import get_conexao
from psycopg2.extras import RealDictCursor
from flask import jsonify

def buscar_cardapio():
    conn = get_conexao()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM cardapio")
    cardapio = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(cardapio)

def buscar_por_id(item_id):
    conn = get_conexao()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute("SELECT * FROM cardapio WHERE id = %s", (item_id,))
    item = cursor.fetchone()

    cursor.close()
    conn.close()

    if item:
        return jsonify(item)
    else:
        return jsonify({"erro": "Item não encontrado"}), 404
