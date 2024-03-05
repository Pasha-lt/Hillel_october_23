import sqlite3

class Vendor:
    def __init__(self, name, item, deal, price):
        self.name = name
        self.item = item
        self.deal = deal
        self.price = price


    def __repr__(self):
        return f"Vendor(name={self.name}, item={self.item}, deal={self.deal}, price={self.price})"

    def  get_vendor_attributes(self):
        return self.name, self.item, self.deal, self.price

class AbstractRepository:
    def __init__(self, db_path):
        self._connection = sqlite3.connect(db_path, isolation_level=None)
        self._cursor = self._connection.cursor()

    def __del__(self):
        if self._cursor:
            self._cursor.close()
        if self._connection:
            self._connection.close()

class VendorsRepository(AbstractRepository):
    def __init__(self, db_path):
        super().__init__(db_path)
        self._cursor.execute(
            "CREATE TABLE IF NOT EXISTS Vendors(vendor_id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, item TEXT, deal INTEGER, price REAL);")

    def add_vendor(self, vendor: Vendor):
        self._cursor.execute("INSERT INTO Vendors(name, item, deal, price) VALUES ((?), (?), (?), (?));",
                             vendor.get_vendor_attributes())
    def add_vendors(self, vendors):
        self._cursor.executemany("INSERT INTO Vendors(name, item, deal, price) VALUES ((?), (?), (?), (?));",
                                 [vendor.get_vendor_attributes() for vendor in vendors])
    def get_all_vendors(self):
        data = self._cursor.execute('SELECT * from Vendors;')
        return self.rows2objects(data)

    def get_vendors_by_deal(self, deal):
        data = self._cursor.execute('SELECT * from Vendors WHERE deal=(?)', (deal,))
        return self.rows2objects(data)

    def row2object(self, row):
        return Vendor(*row[1:])

    def rows2objects(self, rows):
        return [self.row2object(row) for row in rows]


vendor_repo = VendorsRepository('orders_new2.db')
print(vendor_repo.get_all_vendors())
vendor = Vendor('Anna', 'Train', 3, 343434.5)
vendor_repo.add_vendor(vendor)
print(vendor_repo.get_all_vendors())

vendors = [Vendor('John', 'Tram', 5, 34.5), Vendor('James', 'Avion', 2, 10900000)]
vendor_repo.add_vendors(vendors)
print(vendor_repo.get_all_vendors())
print(vendor_repo.get_vendors_by_deal(2))