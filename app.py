import sqlite3
from flask import Flask, render_template, g


app = Flask(__name__)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('database.db')
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route('/')
def acceuil():
    return render_template('index.html')

@app.route('/utilisateurs')
def utilisateurs():
    db = get_db()
    user = db.execute('SELECT * FROM utilisateurs').fetchall()
    print(len(user))
    return render_template('utilisateurs.html', user=user)

@app.route('/profil/int:id>')
def profil(id):
    db = get_db()
    user = db.execute('SELECT * FROM utilisateurs WHERE id = ?', (id,)).fetchall()
    return render_template('profil.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
