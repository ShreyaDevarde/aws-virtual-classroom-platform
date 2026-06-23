from services.database import get_db_connection
class User:

    @staticmethod
    def create_user(username, password):

        conn = get_db_connection()
        cursor = conn.cursor()

        try:

            cursor.execute(
                """
                INSERT INTO users
                (username, password)
                VALUES (?, ?)
                """,
                (username, password)
            )

            conn.commit()

        finally:

            cursor.close()
            conn.close()

    @staticmethod
    def get_user_by_username(username):

        conn = get_db_connection()
        cursor = conn.cursor()

        try:

            cursor.execute(
                """
                SELECT *
                FROM users
                WHERE username = ?
                """,
                (username,)
            )

            return cursor.fetchone()

        finally:

            cursor.close()
            conn.close()