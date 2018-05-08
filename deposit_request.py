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
    logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [User] - '+'GET request at http://localhost/cgi-bin/bankingsystem/deposit_request.py\n')

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
        logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Connection request at http://localhost/cgi-bin/bankingsystem/deposit_request.py | Failed to connect to database.\n')
        logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Wrong database user name or password.\n')
        logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Check admin details provided in `config` at line 128 - deposit_request.py.\n')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Connection request at http://localhost/cgi-bin/bankingsystem/deposit_request.py | Failed to connect to database.\n')
        logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Database does not exist.\n')
        logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Check database details provided in `config` at line 128 - deposit_request.py.\n')
    else:
        logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Error in conn.connect() at line 135 - deposit_request.py.\n')
        logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Error details : '+err)
else:
    logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Database connection successful! - deposit_request.py. - @user:'+user_acc_num+'\n')
    cursor = db_conn.cursor()
    transfer_query = ("UPDATE userinfo "
                        "SET account_bal = %s"
                        "WHERE account_num = %s")
    try:
        cursor.execute(transfer_query,(user_acc_bal+deposit_amt,user_acc_num))
    except:
        logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [User] - '+'Transfer money transaction failed. - deposit_request.py. - @user:'+user_acc_num+'\n')
        cursor.close()
        db_conn.close()
        logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Database connection closed. - deposit_request.py. - @user:'+user_acc_num+'\n')
        print('Transfer failed')
    else:
        db_conn.commit()
        logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Commit new changes to database. - deposit_request.py. - @user:'+user_acc_num+'\n')
        cursor.close()
        db_conn.close()
        logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Database connection closed. - deposit_request.py. - @user:'+user_acc_num+'\n')
        print('Transfer success')

printHTMLend()