from flask import Flask, request, jsonify
import json
import sqlite3  

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('books.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn
                               

"""
books_list = [
{
"id":0,
"author": "Chinua Achebe",
"language": "English",
"title": "Things Fall Apart",
},
{
"id": 1,
"author": "Wole Soyinka",
"language": "English",
"title": "Death and the King's Horseman"
},
{
"id": 2,
"author": "Chimamanda Ngozi Adichie",
"language": "English",
"title": "Half of a Yellow Sun"
},
{
"id": 3,
"author": "Ngũgĩ wa Thiong'o",
"language": "English/Kikuyu",
"title": "Petals of Blood"
},
{
"id": 4,
"author": "Nawal El Saadawi",
"language": "Arabic",
"title": "Woman at Point Zero"
},
{
"id": 5,
"author": "Chigozie Obioma",
"language": "English",
"title": "The Fishermen"
},
{
"id": 6,
"author": "Ayi Kwei Armah",
"language": "English",
"title": "The Beautyful Ones Are Not Yet Born"
},
{
"id": 7,
"author": "Ben Okri",
"language": "English",
"title": "The Famished Road"
},
{
"id": 8,
"author": "Sembene Ousmane",
"language": "French",
"title": "Xala"
},
{
"id": 9,
"author": "Mariama Bâ",
"language": "French",
"title": "So Long a Letter"
},
{
"id": 10,
"author": "Chinua Achebe",
"language": "English",
"title": "Arrow of God"
},
{
"id": 11,
"author": "Nadine Gordimer",
"language": "English",
"title": "Burger's Daughter"
},
{
"id": 12,
"author": "Soyinka Ola Rotimi",
"language": "English",
"title": "The Gods Are Not To Blame"
},
{
"id": 13,
"author": "Leila Aboulela",
"language": "English",
"title": "Minaret"
},
{
"id": 14,
"author": "Mia Couto",
"language": "Portuguese",
"title": "Sleepwalking Land"
},
{
"id": 15,
"author": "Naguib Mahfouz",
"language": "Arabic",
"title": "Children of the Alley"
},
{
"id": 16,
"author": "Buchi Emecheta",
"language": "English",
"title": "The Joys of Motherhood"
}
]
"""
@app.route('/books', methods=['GET', 'POST'])
def books():
    conn =  db_connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor = conn.execute("Select * from book")
        books = [
            dict(id=row[0], author=row[1], language=row[2] , title=row[3])
            for row in cursor.fetchall()
        ]

        if books is not None:
            return jsonify(books)
        else:
            return 'Nothing Found', 404

    if request.method == 'POST':
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']
        sql = """
                INSERT INTO BOOK (author,language,title) VALUES (?, ?, ?)
            """
        cursor = cursor.execute(sql, (new_author,new_lang,new_title))
        conn.commit()

        return f" Book with id: {cursor.lastrowid} successful created"

@app.route('/book/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    conn =  db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM book where id=?",(id,))
        rows = cursor.fetchall()

        for r in rows:
            book = r
        if book is not None:
            return jsonify(book),200
        else:
            return "Something is wrong", 404

    if request.method == 'PUT':
        sql = """ UPDATE book
                SET title=?,
                    author=?,
                    language=?
                WHERE id=? """
        
        author = request.form["author"]
        language = request.form["language"]
        title = request.form["title"]
        
        updated_book = {
                    'id': id,
                    'author': author,
                    'language':language,
                    'title':title
                }
        conn.execute(sql, (author, language, title, id))
        conn.commit()
        return jsonify(updated_book)
    
    if request.method == 'DELETE':
        sql = """DELETE from book WHERE id=?"""
        conn.execute(sql,(id,))
        conn.commit()
        return f"The book with id : {id} has been deleted.",200

if __name__ == '__main__':
    app.run()