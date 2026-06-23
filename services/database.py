# import sqlite3

# def get_db_connection():

#     conn = sqlite3.connect(
#         "database/virtual_classroom.db"
#     )

#     conn.row_factory = sqlite3.Row

#     return conn

import sqlite3
import os

def get_db_connection():

    db_path = "virtual_classroom.db"

    print("Using DB:", os.path.abspath(db_path))

    conn = sqlite3.connect(db_path)

    conn.row_factory = sqlite3.Row

    return conn