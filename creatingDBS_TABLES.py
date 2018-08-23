import sqlite3

conn  = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE example(Language VARCHAR, Version REAL, Skill TEXT)")
def enter_data():
    c.execute("INSERT INTO example VALUES('Python', 2.7, 'Beginner')")
    c.execute("INSERT INTO example VALUES('Python', 3.3, 'Intermediate')")
    c.execute("INSERT INTO example VALUES('Python', 3.4, 'Expert')")
    conn.commit()

def enter_dynamic_data():
    lang = input("What language? ")
    version = float(input("What version? "))
    skill = input("What skill level? ")

    c.execute("INSERT INTO example (Language, Versioin, Skill) Values(?,?,?)", (lang, version, skill))
    conn.commit()



def read_from_database():

    what_skill = input("what skill level are we looking for?")

    what_language = input("what language?:  ")
    sql = "SELECT * FROM example WHERE Skill = ? AND Langage = ?"


    for row in c.execute(sql, [(what_skill),(what_language)]):
        print(row)
        #print(row[0])

#update
def read_from_database():

    #sql = "SELECT * FROM example LIMIT 2"
    sql = " UPDATE example SET Skill = 'Beginner' WHERE skill = 'beginner'"


    c.execute(sql):

    sql = "SELECT * FROM example"

    for row in c.execute(sql):
        print(row)

    print(20*"#")
    #delete
    sql= "DELETE FROM example WHERE Skill = 'Beginner'"

    c.execute(sql)


    sql = "SELECT * FROM example"

    for row in c.execute(sql):
        print(row)
    conn.commit()

read_from_database()



#create_table()

#enter_dynamic_data()



conn.close()
