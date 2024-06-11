import sqlite3

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS users (
                            discord_id INTEGER PRIMARY KEY,
                            balance INTEGER DEFAULT 0
                            )''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS images (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            filename TEXT
                            )''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS purchases (
                            discord_id TEXT,
                            image_id INTEGER,
                            FOREIGN KEY (discord_id) REFERENCES users (discord_id),
                            FOREIGN KEY (image_id) REFERENCES images (id),
                            PRIMARY KEY (discord_id, image_id)
                            )''')
        self.conn.commit()

    def add_user(self, discord_id):
        self.cur.execute("INSERT OR IGNORE INTO users (discord_id, balance) VALUES (?, ?)", (discord_id, 200))
        self.conn.commit()

    def add_image(self, filename):
        self.cur.execute("INSERT INTO images (filename) VALUES (?)", (filename,))
        self.conn.commit()

    def add_purchase(self, discord_id, image_id):
        self.cur.execute("INSERT INTO purchases (discord_id, image_id) VALUES (?, ?)", (discord_id, image_id))
        self.conn.commit()

    def get_random_image(self):
        self.cur.execute("SELECT id, filename FROM images ORDER BY RANDOM() LIMIT 1")
        image = self.cur.fetchone()
        return image

    def get_user_purchases(self, discord_id):
        self.cur.execute("SELECT images.filename FROM images "
                         "JOIN purchases ON images.id = purchases.image_id "
                         "WHERE purchases.discord_id = ?", (discord_id,))
        purchases = self.cur.fetchall()
        return purchases

    def get_all_images(self):
        self.cur.execute("SELECT filename FROM images")
        images = self.cur.fetchall()
        return images

    def get_all_users(self):
        self.cur.execute("SELECT discord_id FROM users")
        users = self.cur.fetchall()
        return users

    def change_balance(self, discord_id, amount):
        self.cur.execute("SELECT balance FROM users WHERE discord_id = ?", (discord_id,))
        user = self.cur.fetchone()
        new_balance = user[0] + amount
        self.cur.execute("UPDATE users SET balance = ? WHERE discord_id = ?", (new_balance, discord_id))
        return new_balance

    def get_balance(self, discord_id):
        self.cur.execute("SELECT balance FROM users WHERE discord_id = ?", (discord_id,))
        return self.cur.fetchone()[0]

    def close(self):
        self.conn.close()


# Пример использования
# db = Database('discord.db')
# db.add_user('1234567890')  # Добавление пользователя
# db.add_user('0987654321')  # Добавление пользователя
# db.add_image('image1.jpg')  # Добавление картинки
# db.add_image('image2.jpg')  # Добавление картинки
# db.add_purchase('1234567890', 1)  # Покупка картинки пользователем
# db.add_purchase('0987654321', 2)  # Покупка картинки пользователем
#
# print(db.get_random_image())  # Получение случайной картинки
# print(db.get_user_purchases('1234567890'))  # Получение списка картинок, купленных пользователем
# print(db.get_all_images())  # Получение списка всех картинок
#
# db.close()
