#Unit8/Database Handling/Class2

'''
1) Get All the Movies

Search the 'marvel' movie table in the database using sqlite3 and return a list of all the movies in it. The db parameter is the db_connection that is setup in the table setup.

Movie Spreadsheet

Example:

result = get_all_movies(db)
print(result[0]) # (1, 'Iron Man', 'Jon Favreau', 94, 79))
'''

import sqlite3
# Database setup: Please don't change this
db = sqlite3.connect("file::memory:?cache=shared")

db.executescript("""

drop table if exists marvel;
create table marvel (
  id integer primary key autoincrement,
  title text not null,
  director text not null,
  tomatoes integer,
  metacritic integer
);

-- marvel
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (1, 'Iron Man', 'Jon Favreau', 94, 79);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (2, 'The Incredible Hulk', 'Louis Leterrier', 67, 61);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (3, 'Iron Man 2', 'Jon Favreau', 73, 57);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (4, 'Thor', 'Kenneth Branagh', 77, 57);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (5, 'Captain America: The First Avenger', 'Joe Johnston', 80, 66);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (6, 'Marvels The Avengers', 'Joss Whedon', 92, 69);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (7, 'Iron Man 3', 'Shane Black', 80, 62);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (8, 'Thor: The Dark World', 'Alan Taylor', 66, 54);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (9, 'Captain America: The Winter Soldier', 'Anthony and Joe Russo', 89, 70);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (10, 'Guardians of the Galaxy', 'James Gunn', 91, 76);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (11, 'Avengers: Age of Ultron', 'Joss Whedon', 75, 66);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (12, 'Ant-Man', 'Peyton Reed', 82, 64);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (13, 'Captain America: Civil War', 'Anthony and Joe Russo', 91, 75);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (14, 'Doctor Strange', 'Scott Derrickson', 89, 72);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (15, 'Guardians of the Galaxy Vol. 2', 'James Gunn', 83, 67);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (16, 'Spider-Man: Homecoming', 'Jon Watts', 92, 73);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (17, 'Thor: Ragnarok', 'Taika Waititi', 92, 74);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (18, 'Black Panther', 'Ryan Coogler', 97, 88);
""")
# Finish Database Setup

def get_all_movies(db_connection):
    # Your code here
    cursor = db_connection.execute('SELECT * FROM marvel;')
    return cursor.fetchall()

# Test Cases

def test_get_movies():
    assert db is not None
    result = get_all_movies(db)
    assert result[0] == (1, 'Iron Man', 'Jon Favreau', 94, 79)
    assert result[1] == (2, 'The Incredible Hulk', 'Louis Leterrier', 67, 61)
    assert result[17] == (18, 'Black Panther', 'Ryan Coogler', 97, 88)



'''
2) Get Movies and Directors

Search the 'marvel' movie table in the database and return the title and director from each movie. Only get as many movies as the limit parameter.

Movie Spreadsheet

Example:

get_movies_and_directors(db, limit=3)

'''
[('Iron Man', 'Jon Favreau'), ('The Incredible Hulk', 'Louis Leterrier'),
    ('Iron Man 2', 'Jon Favreau')
]
'''
'''

import sqlite3
db = sqlite3.connect("file::memory:?cache=shared")

db.executescript("""

drop table if exists marvel;
create table marvel (
  id integer primary key autoincrement,
  title text not null,
  director text not null,
  tomatoes integer,
  metacritic integer
);

-- marvel
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (1, 'Iron Man', 'Jon Favreau', 94, 79);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (2, 'The Incredible Hulk', 'Louis Leterrier', 67, 61);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (3, 'Iron Man 2', 'Jon Favreau', 73, 57);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (4, 'Thor', 'Kenneth Branagh', 77, 57);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (5, 'Captain America: The First Avenger', 'Joe Johnston', 80, 66);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (6, 'Marvels The Avengers', 'Joss Whedon', 92, 69);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (7, 'Iron Man 3', 'Shane Black', 80, 62);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (8, 'Thor: The Dark World', 'Alan Taylor', 66, 54);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (9, 'Captain America: The Winter Soldier', 'Anthony and Joe Russo', 89, 70);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (10, 'Guardians of the Galaxy', 'James Gunn', 91, 76);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (11, 'Avengers: Age of Ultron', 'Joss Whedon', 75, 66);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (12, 'Ant-Man', 'Peyton Reed', 82, 64);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (13, 'Captain America: Civil War', 'Anthony and Joe Russo', 91, 75);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (14, 'Doctor Strange', 'Scott Derrickson', 89, 72);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (15, 'Guardians of the Galaxy Vol. 2', 'James Gunn', 83, 67);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (16, 'Spider-Man: Homecoming', 'Jon Watts', 92, 73);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (17, 'Thor: Ragnarok', 'Taika Waititi', 92, 74);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (18, 'Black Panther', 'Ryan Coogler', 97, 88);
""")


def get_movies_and_directors(db_connection, limit=5):
    cursor = db_connection.execute('SELECT title, director FROM marvel;')
    cursor_filter = []
    for item in range(limit):
        cursor_filter.append(cursor.fetchone())
    return cursor_filter
    
'''
#alternate solution 
def get_movies_and_directors(db, limit=5):
    query = 'SELECT title, director FROM marvel LIMIT :limit'
    cursor = db.execute(query, {
        'limit': limit
    })
return cursor.fetchall()
'''

# Test Cases

def test_movies_and_directors():
    result = get_movies_and_directors(db, limit=3)
    assert len(result) == 3
    assert result[0] == ('Iron Man', 'Jon Favreau')
    assert result[2] == ('Iron Man 2', 'Jon Favreau')

        
