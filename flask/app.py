from flask import Flask, request, jsonify

app = Flask(__name__)

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
},
{
"id": 17,
"author": "Dinaw Mengestu",
"language": "English",
"title": "The Beautiful Things That Heaven Bears"
},
{
"id": 18,
"author": "Aminata Sow Fall",
"language": "French",
"title": "The Beggars' Strike"
},
{
"id": 19,
"author": "Tayeb Salih",
"language": "Arabic",
"title": "Season of Migration to the North"
}

]

@app.route('/books',method=['GET','POST'])
def books():
  if request.method == 'GET':
    if len(books_list) > 0:
      return jsonify(books_list)
    else:
      'Nothing Found', 404

  if request.method == 'POST':
    new_author = request.form['author']
    new_langauge = request.form['language']
    new_title=request.form['title']
    iD = books_list[-1]['id']+1

    new_obj = {
      'id': iD,
      'author'; new_author,
      'language': new_language,
      'title':new_title
    }
    books_list.append(new_obj)
    return jsonify(books_list)