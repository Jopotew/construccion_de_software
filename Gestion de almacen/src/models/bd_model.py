import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    """
    Clase para gestionar la conexión y ejecución de consultas relacionadas al stock en la base de datos MySQL.
    """

    def __init__(self, host: str, user: str, password: str, database: str):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor(dictionary=True)
            print("✅ Conexión exitosa a la base de datos")
        except Error as e:
            print(f"❌ Error al conectar a la base de datos: {e}")

    def execute_query(self, query: str, params: tuple = None):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            print("✅ Consulta ejecutada correctamente")
        except Error as e:
            print(f"❌ Error al ejecutar la consulta: {e}")

    def fetch_query(self, query: str, params: tuple = None):
        try:
            self.cursor.execute(query, params)
            result = self.cursor.fetchall()
            return result
        except Error as e:
            print(f"❌ Error al ejecutar la consulta: {e}")
            return None

    def increase_stock(self, id_item: int, quantity: int):
        """
        Aumenta la cantidad de un item en stock.
        """
        query = """
            UPDATE Stock
            SET quantity = quantity + %s
            WHERE id_item = %s
        """
        self.execute_query(query, (quantity, id_item))

    def decrease_stock(self, id_item: int, quantity: int):
        """
        Disminuye la cantidad de un item en stock si hay suficiente.
        """
        stock = self.fetch_query(
            "SELECT quantity FROM Stock WHERE id_item = %s LIMIT 1", (id_item,)
        )

        if stock and stock[0]['quantity'] >= quantity:
            query = """
                UPDATE Stock
                SET quantity = quantity - %s
                WHERE id_item = %s
            """
            self.execute_query(query, (quantity, id_item))
        else:
            print("❌ No hay suficiente stock disponible.")

    def process_stock_order(self, order_id: int):
        """
        Procesa una orden de stock, actualiza el stock y cambia el estado de la orden.
        """
        order = self.fetch_query(
            "SELECT id_item, quantity, status FROM StockOrder WHERE id = %s", (order_id,)
        )

        if not order:
            print("❌ Orden no encontrada.")
            return

        if order[0]['status']:
            print("⚠️ La orden ya fue procesada.")
            return

        # Aumenta el stock
        self.increase_stock(order[0]['id_item'], order[0]['quantity'])

        # Marca la orden como completada
        update_query = "UPDATE StockOrder SET status = TRUE WHERE id = %s"
        self.execute_query(update_query, (order_id,))
        print("✅ Orden procesada y stock actualizado.")

    def close(self):
        """
        Cierra la conexión y el cursor de la base de datos.
        """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("✅ Conexión cerrada")
