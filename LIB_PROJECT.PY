############################ DATABASE ###########################
import mysql.connector
lib_project = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "Chandu@123",
    database = "lib_project"

)

# print(lib_project) 

lib_data = lib_project.cursor()
# lib_data.execute("CREATE DATABASE lib_project")

# lib_data.execute("CREATE TABLE BOOKS_TABLE (BOOK_NAME VARCHAR(50), BAR_CODE VARCHAR(50), TOTAL INT, SUBJECT VARCHAR (50))")
# lib_data.execute("CREATE TABLE ISSUE_TABLE (NAME VARCHAR(50), REGISTER_NO VARCHAR(50), BAR_CODE INT, ISSUE VARCHAR(50))")
# lib_data.execute("CREATE TABLE SUBMIT_TABLE (NAME VARCHAR(50), REGISTER_NO VARCHAR(50), BAR_CODE INT, SUBMIT VARCHAR(50))")



##########################################Programming###############################################

def addbook():
    bookname = input("Enter Book Name: ")
    code = input("Enter Book Code: ") 
    total = input("Total Books: ")
    subject = input("Enter Subject: ")
    data=(bookname,code,total,subject)
    sql = "INSERT INTO books_table values(%s,%s,%s,%s)"
    lib_data = lib_project.cursor()
    lib_data.execute(sql,data)
    lib_project.commit()
    print(">------------------------------------------------------<")
    print("Data Entered Sucessfully")
    main()

def issuebook():
    name = input("Enter Name: ")
    reg = input("Enter Reg No: ")
    cb = input("Enter Book code: ")
    d= input("Enter Date: ")
    sql = "INSERT INTO issue_table values(%s,%s,%s,%s)"
    data = (name,reg,cb,d)
    lib_data = lib_project.cursor()
    lib_data.execute(sql,data)
    lib_project.commit()
    print(">--------------------------------------------------<")
    print("Book issued to:",name)
    bookup(cb,-1)

def submitbook():
    name = input("Enter Name: ")
    reg = input("Enter Reg No: ")
    cb = input("Enter Book code: ")
    date = input("Enter date: ")
    sql = "INSERT INTO submit_table values(%s,%s,%s,%s)"
    data = (name,reg,cb,date)
    lib_data = lib_project.cursor()
    lib_data.execute(sql,data)
    lib_project.commit()
    print(">---------------------------------------------------------------<")
    print("Book Submitted from :",name)
    bookup(cb,1)

def bookup(cb,u):
    sql = "SELECT TOTAL from books_table WHERE BAR_CODE = %s"
    data = (cb,)
    lib_data = lib_project.cursor()
    lib_data.execute(sql,data)
    myresult = lib_data.fetchone()
    t = myresult[0] + u
    sql = "UPDATE books_table set TOTAL =%s where BAR_CODE = %s"
    d = (t,cb)
    lib_data.execute(sql,d)
    lib_project.commit()
    main()

def deletebook():
    bc = input("Enter Book Code: ")
    sql = "DELETE FROM books_table WHERE BAR_CODE = %s"
    data = (bc,)
    lib_data = lib_project.cursor()
    lib_data.execute(sql,data)
    lib_project.commit()
    print("Books Deleted")
    main()

def displaybook():
    sql = "SELECT * FROM books_table"
    lib_data = lib_project.cursor()
    lib_data.execute(sql)
    myresult = lib_data.fetchall()
    for i in myresult:
        print("Book Name :",i[0])
        print("Book Code :",i[1])
        print("Total: ",i[2])
        print(">-------------------------------------<")
    main()




def main():
    print("""

    1. ADD BOOK
    2. ISSUE BOOK
    3. SUBMIT BOOK
    4. DELETE BOOK
    5. DISPLAY BOOKS
      
    """)
    choice = input("Enter Task No: ")
    print(">-----------------------------------------<")
    if(choice == '1'):
        addbook()
    elif(choice == '2'):
        issuebook()
    elif(choice == '3'):
        submitbook()
    elif(choice == '4'):
        deletebook()
    elif(choice == '5'):
        displaybook()
    else:
        print("Wrong choice..........")
        main()
    
def pswd():
        id = input("Enter your id: ")
        ps = input("Enter password: ")
        if id == "chandu":
            main()
        elif ps == "123":
            main()
        else:
            print("Invalid....")
            pswd()
pswd()



