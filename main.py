from fastapi import FastAPI
import mysql.connector
import os

app = FastAPI()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT", 3306))
    )

@app.get("/inventario/primero")
def get_first_item():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM repuestos LIMIT 1")
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result