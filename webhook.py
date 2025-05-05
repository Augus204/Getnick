import sqlite3
import pandas as pd
import requests


wa_db_path = '/sdcard/wa.db'  # Ruta original
wa_db_backup_path = '/storage/emulated/0/WhatsApp/Databases/wa.db'  # Nueva ruta

try:
    with sqlite3.connect(wa_db_path) as con1:
        contacts = pd.read_sql_query("SELECT jid, wa_name from wa_contacts", con1)
        contacts['jid'] = contacts['jid'].str.split('@').str[0]
        contacts.dropna(inplace=True)

except sqlite3.Error as e:
    print(f"Error conectando a la base de datos en la ruta {wa_db_path}: {e}")
    print("Intentando con la nueva ruta...")
    try:
        with sqlite3.connect(wa_db_backup_path) as con1:
            contacts = pd.read_sql_query("SELECT jid, wa_name from wa_contacts", con1)
            contacts['jid'] = contacts['jid'].str.split('@').str[0]
            contacts.dropna(inplace=True)

    except sqlite3.Error as e:
        print(f"Error conectando a la base de datos en la nueva ruta {wa_db_backup_path}: {e}")
        exit(1)

json_data = contacts.to_dict(orient='records')

url = 'https://5mkwzjlv-5000.use.devtunnels.ms/webhook2'
response = requests.post(url, json=json_data)

print("Código de estado:", response.status_code)
print("Respuesta:", response.text)