import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QWidget

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('cappuccino.ui', self)
        self.connection = sqlite3.connect("coffee.db")
        self.select_data()
        self.pushButton.clicked.connect(self.run)

    def select_data(self):
        query = "SELECT * FROM types_of_coffee"
        res = self.connection.cursor().execute(query).fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def run(self):
        self.secw = SecondWind()
        self.secw.show()
        self.destroy()

class SecondWind(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.BackButton.clicked.connect(self.run2)
        self.appendButton.clicked.connect(self.refresh_data)
        self.editButton.clicked.connect(self.edit)
        self.connection = sqlite3.connect("coffee.db")
        self.showinfo()

    def refresh_data(self):
        data_base_name = 'coffee.db'
        con = sqlite3.connect(data_base_name)
        cur = con.cursor()
        if self.lineEdit_7.text() == '':
            if self.lineEdit.text() != '' and self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '' and self.lineEdit_4.text() != '' and self.lineEdit_5.text() != '' and self.lineEdit_6.text() != '':
                insert_query = f"INSERT INTO types_of_coffee(variety_name,roast_degree,type,flavor_description,price,packing_volume)" \
                               f"VALUES ('{self.lineEdit.text()}', '{self.lineEdit_2.text()}', '{self.lineEdit_3.text()}', '{self.lineEdit_4.text()}', '{self.lineEdit_5.text()}', '{self.lineEdit_6.text()}')"
                cur.execute(insert_query)
                con.commit()
                con.close()
        self.showinfo()

    def showinfo(self):
        query = "SELECT * FROM types_of_coffee"
        res = self.connection.cursor().execute(query).fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def edit(self):
        data_base_name = 'coffee.db'
        con = sqlite3.connect(data_base_name)
        cur = con.cursor()
        if self.lineEdit.text() != '':
            insert_query = f"UPDATE types_of_coffee SET variety_name = '{self.lineEdit.text()}' WHERE id = '{int(self.lineEdit_7.text())}'"
            cur.execute(insert_query)
        if self.lineEdit_2.text() != '':
            insert_query = f"UPDATE types_of_coffee SET roast_degree = '{self.lineEdit_2.text()}' WHERE id = '{int(self.lineEdit_7.text())}'"
            cur.execute(insert_query)
        if self.lineEdit_3.text() != '':
            insert_query = f"UPDATE types_of_coffee SET type = '{self.lineEdit_3.text()}' WHERE id = '{int(self.lineEdit_7.text())}'"
            cur.execute(insert_query)
        if self.lineEdit_4.text() != '':
            insert_query = f"UPDATE types_of_coffee SET flavor_description = '{self.lineEdit_4.text()}' WHERE id = '{int(self.lineEdit_7.text())}'"
            cur.execute(insert_query)
        if self.lineEdit_5.text() != '':
            insert_query = f"UPDATE types_of_coffee SET price = '{self.lineEdit_5.text()}' WHERE id = '{int(self.lineEdit_7.text())}'"
            cur.execute(insert_query)
        if self.lineEdit_6.text() != '':
            insert_query = f"UPDATE types_of_coffee SET packing_volume = '{self.lineEdit_6.text()}' WHERE id = '{int(self.lineEdit_7.text())}'"
            cur.execute(insert_query)
        con.commit()
        con.close()
        self.showinfo()

    def run2(self):
        self.frstw = DBSample()
        self.frstw.show()
        self.destroy()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())