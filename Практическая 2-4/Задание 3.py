import psutil
import sqlite3
from datetime import datetime
class System_monitor:
    def __init__(self, db_name = "monitoring_system.db"):
        self.db_name = db_name
        self.con = sqlite3.connect(self.db_name)
        self.cursor = self.con.cursor()
        self.create_table()
    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS information_system
                            (time DATATIME PRIMARY KEY,
                            cpu REAL NOT NULL,
                            memory REAL NOT NULL,
                            disk REAL NOT NULL
                            )
                        """)
        self.con.commit()
    def information_system(self):
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('C:\\').percent
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return time, cpu, memory, disk
    def insert_bd(self, time, cpu, memory, disk):
        self.cursor.execute("INSERT INTO information_system (time, cpu, memory, disk) VALUES (?, ?, ?, ?)", (time, cpu, memory, disk))
        self.con.commit()
    def information_display(self, time, cpu, memory, disk):
        print(f"Время: {time}")
        print(f"CPU информация: {cpu}%")
        print(f"Оперативная память: {memory}%")
        print(f"Диск {disk}%")
    def run_monitoring(self):
        time, cpu, memory, disk = self.information_system()
        self.insert_bd(time, cpu, memory, disk)
        self.information_display(time, cpu, memory, disk)
    def close(self):
        self.con.close()
monitor = System_monitor()
monitor.run_monitoring()
monitor.close()