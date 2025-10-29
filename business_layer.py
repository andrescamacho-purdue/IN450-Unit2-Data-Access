import psycopg2

class BusinessLayer:
    """Business layer for IN450 Unit 2. All DB I/O stays here."""

    def __init__(self, conn_string: str):
        self.conn_string = conn_string

    def _connect(self):
        return psycopg2.connect(self.conn_string)

    def get_row_count_in450a(self) -> int:
        """Return total rows from in450a."""
        with self._connect() as conn, conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM in450a;")
            return cur.fetchone()[0]

    def get_names_in450b(self):
        """Return list of (first_name, last_name) tuples from in450b."""
        with self._connect() as conn, conn.cursor() as cur:
            cur.execute("SELECT first_name, last_name FROM in450b;")
            return cur.fetchall()
