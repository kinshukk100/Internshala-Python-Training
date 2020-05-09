import sqlite3
db=sqlite3.connect("m5assignment.db")
cur=db.cursor()

total=0
while True:
    
    ttl=input("enter book's title: ")

    sql="SELECT * FROM books WHERE title='"+ttl+"'"
    cur=db.cursor()
    cur.execute(sql)
    rec=cur.fetchone()
    if rec!=None:
        print (rec)
        pr=rec[3]
        qty=int(input("enter number of books purchased"))
        cost=pr*qty
        total=total+cost
    else:
        print ("Title Not Found")
    choice=input("add more books[Y/N]?")
    if choice=='N': break
print ("Total cost of Purchased Books",total)
db.close()

