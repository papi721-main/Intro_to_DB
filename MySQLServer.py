#!/usr/bin/env python3
import mysql.connector

with mysql.connector.connect(
    host="localhost",
    user="papi721",
    password="",
) as mydb:
    mycursor = mydb.cursor()
    try:
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as e:
        print(e)
