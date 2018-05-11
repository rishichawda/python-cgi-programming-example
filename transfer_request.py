#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import cgi,cgitb,datetime
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

try:
    logfile = open('my_account_app.log','a')
except:
    print('error opening log file..')
else:
    logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [User] - '+'GET request at http://localhost/cgi-bin/bankingsystem/transfer_request.py\n')

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
        logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Connection request at http://localhost/cgi-bin/bankingsystem/transfer_request.py | Failed to connect to database.\n')
        logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Wrong database user name or password.\n')
        logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Check admin details provided in `config` at line 128 - transfer_request.py.\n')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Connection request at http://localhost/cgi-bin/bankingsystem/transfer_request.py | Failed to connect to database.\n')
        logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Database does not exist.\n')
        logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Check database details provided in `config` at line 128 - transfer_request.py.\n')
    else:
        logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Error in conn.connect() at line 135 - transfer_request.py.\n')
        logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Error details : '+err)
else:
    logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Database connection successful!\n')
    cursor = db_conn.cursor()
    transfer_query = ("UPDATE userinfo "
                        "SET account_bal = %s"
                        "WHERE account_num = %s")
    if user_acc_bal >= payee_transfer_amt:
        try:
            cursor.execute(transfer_query,(user_acc_bal-payee_transfer_amt,user_acc_num))
        except:
            logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [User] - '+'Transfer money transaction failed. - transfer_request.py. - @user:'+user_acc_num+'\n')
            cursor.close()
            db_conn.close()
            logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Database connection closed. - transfer_request.py. - @user:'+user_acc_num+'\n')
            print('Transfer failed.')
        else:
            logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [User] - '+'Transfer money transaction successful. - transfer_request.py. - @user:'+user_acc_num+'\n')
            db_conn.commit()
            logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Commit new changes to database. - transfer_request.py. - @user:'+user_acc_num+'\n')
            cursor.close()
            db_conn.close()
            logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Database connection closed. - transfer_request.py. - @user:'+user_acc_num+'\n')
            print('Transfer success.')
    else:
        print('Transfer unsuccessful. Please enter a valid amount.')

printHTMLend()