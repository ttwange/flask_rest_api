from flask import Flask, request, jsonify

app =Flask(__name__)

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
}
]