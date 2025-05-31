from fastapi import FastAPI
import mysql.connector
import os

app = FastAPI()

DB_HOST = os.getenv("DB_HOST", "yamanote.proxy.rlwy.net")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "IzHqftUcXdEZFbPeYhlEFhCErHxWRZuF")
DB_NAME = os.getenv("DB_NAME", "Sepeyco")
DB_PORT = int(os.getenv("DB_PORT", "51235"))

@app.get("/repuesto")
def get_first_repuesto():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=DB_PORT
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM repuestos LIMIT 1;")
        repuesto = cursor.fetchone()
        cursor.close()
        conn.close()
        return {"repuesto": repuesto}
    except Exception as e:
        return {"error": str(e)}