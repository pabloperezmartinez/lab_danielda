import psycopg2

class StudentModel:
    def __init__(self) -> None:
        self._conn = psycopg2.connect("dbname=pabloperez_1 user=postgres password=pucetec host=localhost")
        self._cur = self._conn.cursor()

    def get_students(self):
        query = "SELECT * FROM students ORDER BY last_name"
        self._cur.execute(query)
        return self._cur.fetchall()

    def create_student(self, first_name, last_name, email):
        query = "INSERT INTO students (first_name, last_name, email) VALUES (%s, %s, %s)"
        self._cur.execute(query, (first_name, last_name, email))
        self._conn.commit()

    def update_student(self, id, first_name, last_name, email):
        try:
                query = "UPDATE students SET first_name=%s, last_name=%s, email=%s WHERE id=%s"
                self._cur.execute(query, (first_name, last_name, email, id))
                self._conn.commit()
                return True
        except Exception as e:
            print("Ocurrió un error: ", e)
            return False
        
    def get_student_by_id(self, student_id):
        
        try:
                query = "SELECT * FROM students WHERE id =%s "
                self._cur.execute(query, (student_id,))
                return self._cur.fetchone()
            
        except Exception as e:
            print("Ocurrió un error: ", e)
            return None

    def close(self):
        self._cur.close()
        self._conn.close()

        
    