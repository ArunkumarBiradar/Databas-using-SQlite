import sqlite3
con = sqlite3.connect('MFM.db')
print("Database connected....")
cur=con.cursor()
cur.execute("INSERT INTO My_Favourite_Movies(movie_name,dor,actor_name,actress_name,director_name) VALUES('3idiots',2009,'Amirkhan','Kareena Kapoor','Rajkumar Hirani')")
cur.execute("INSERT INTO My_Favourite_Movies(movie_name,dor,actor_name,actress_name,director_name) VALUES('Munna bhai MBBS',2003,'Sanja Dutt','Gracy Singh','Rajkumar Hirani')")
cur.execute("INSERT INTO My_Favourite_Movies(movie_name,dor,actor_name,actress_name,director_name) VALUES('pk',2014,'Amirkhan','Anushka Sharma','Rajkumar Hirani')")
cur.execute("INSERT INTO My_Favourite_Movies(movie_name,dor,actor_name,actress_name,director_name) VALUES('Shershaah',2021,'Sidharth Malhotra','Kiara Advani','Vishnuvardhan')")
cur.execute("INSERT INTO My_Favourite_Movies(movie_name,dor,actor_name,actress_name,director_name) VALUES('Commando 3',2019,'Vidyut Jammwal','Adah Sharma','Aditya datt')")
print("data inserted....")
print("movie_name\t ,dor\t ,actor_name\t ,actress_name\t ,director_name\n")
cursor=cur.execute("SELECT * FROM My_Favourite_Movies");
for row in cursor:
    print(row[0], "\t",row[1], "\t",row[2], "\t",row[3],"\t",row[4], "\n")
con.close()