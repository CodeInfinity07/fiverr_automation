#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 08:06:52 2021

@author: root
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="zain0980",
  database="coinhunt"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT `token_address` FROM token")

myresult = mycursor.fetchall()

for x in myresult:
  print(x[0])