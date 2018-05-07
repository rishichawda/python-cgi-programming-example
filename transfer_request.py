#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import cgi,cgitb
cgitb.enable()
import mysql.connector as conn
from mysql.connector import errorcode

def printHTMLhead():
    # Print head of the html page
    print("<head>")
    print("<link rel=\"stylesheet\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css\" integrity=\"sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB\" crossorigin=\"anonymous\">")
    print("<title>requestpage</title>")
    print("</head>")

def printHTMLstart():
    print("Content-Type: text/html\r\n")
    print("\r\n")
    print("<html>")

def printHTMLend():
    # Add script tags
    print("<script src=\"https://code.jquery.com/jquery-3.3.1.slim.min.js\" integrity=\"sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo\" crossorigin=\"anonymous\"></script>")
    print("<script>window.onunload=function(){window.opener.location.reload();}</script>")
    print("<script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js\" integrity=\"sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49\" crossorigin=\"anonymous\"></script>")
    print("<script src=\"https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js\" integrity=\"sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T\" crossorigin=\"anonymous\"></script>")
    # Print closing body tag for html
    print("</body>")
    # End html page
    print("</html>")

printHTMLstart()
printHTMLhead()

form = cgi.FieldStorage()
details = form.getvalue('transfer_details')
user_acc_num = form.getvalue('user_accnum')
user_acc_bal = float(form.getvalue('user_accbal'))
payee_acc_num = details[0]
payee_acc_bank = details[1]
payee_transfer_amt = float(details[2])

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
        cursor.execute(transfer_query,(user_acc_bal-payee_transfer_amt,user_acc_num))
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