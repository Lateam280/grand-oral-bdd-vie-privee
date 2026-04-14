import anosql
import psycopg2
import sqlite3

connexion = psycopg2.connect('database.db')
requetes = anosql.from_path('requetes.sql','sqlite3')

requetes.get_all_greetings(connexion)
requetes.get_all_greetings.__doc__
requetes.get_all_greetings.sql
requetes.available_queries

