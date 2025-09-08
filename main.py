from colorama import Fore, Back, Style
import sqlite3 as sq

conn = sq.connect("database.db")
cursor = conn.cursor()

