#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import cgi,cgitb
cgitb.enable()
import mysql.connector as conn
from mysql.connector import errorcode

def printHTMLhead():
    # Print head of the html page
    print("<head>")
    print("<title>requestpage</title>")
    print("</head>")

def printHTMLstart():
    print("Content-Type: text/html\r\n")
    print("\r\n")
    print("<html>")

def printHTMLend():
    # Add script tags
    print("<script>window.onunload=function(){window.opener.location.reload();}</script>")
    # Print closing body tag for html
    print("</body>")
    # End html page
    print("</html>")

printHTMLstart()
printHTMLhead()

form = cgi.FieldStorage()
user_acc_num = form.getvalue('user_accnum')
user_acc_bal = float(form.getvalue('user_accbal'))
deposit_amt = float(form.getvalue('deposit_details'))

config = {
        'user':'root', 
        'password':'', 
        'host':'localhost', 
        'database':'banking system'
    }

try:
    db_conn = conn.connect(**config)
except conn.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor = db_conn.cursor()
    transfer_query = ("UPDATE userinfo "
                        "SET account_bal = %s"
                        "WHERE account_num = %s")
    try:
        cursor.execute(transfer_query,(user_acc_bal+deposit_amt,user_acc_num))
    except:
        cursor.close()
        db_conn.close()
        print('Transfer failed')
    else:
        db_conn.commit()
        cursor.close()
        db_conn.close()
        print('Transfer success')

printHTMLend()