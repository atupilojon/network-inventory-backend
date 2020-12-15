import sys
import mariadb


class DaoService:
    try:
        session = mariadb.connect(
            user="root",
            password="@gusdana",
            host="172.17.0.2",
            port=3306,
            database="inventory"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    def getCursor(self):
        return self.session.cursor()

    def getDevices(self):
        return self.getCursor().execute("SELECT device_name FROM device")
