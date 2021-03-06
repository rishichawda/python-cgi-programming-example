#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import cgi,cgitb,datetime
cgitb.enable()
import mysql.connector as conn
from mysql.connector import errorcode

def printHTMLstart():
    print("Content-Type: text/html\r\n")
    print("\r\n")
    print("<html>")

def printHTMLhead():
    # Print head of the html page
    print("<head>")
    print("<link rel=\"stylesheet\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css\" integrity=\"sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB\" crossorigin=\"anonymous\">")
    print("<title>User Login</title>")
    print("</head>")

def printHTMLend():
    # Add script tags
    print("<script src=\"https://code.jquery.com/jquery-3.3.1.slim.min.js\" integrity=\"sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo\" crossorigin=\"anonymous\"></script>")
    print("<script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js\" integrity=\"sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49\" crossorigin=\"anonymous\"></script>")
    print("<script src=\"https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js\" integrity=\"sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T\" crossorigin=\"anonymous\"></script>")
    # Print closing body tag for html
    print("</body>")
    # End html page
    print("</html>")

def printHTMLbody():
    # Print body of the html page
    print("<body>")
    if form.getvalue('loginattempt')=='1':
        print("<div class=\"alert alert-danger\" role=\"alert\">Incorrect account number / password details! Please check details and try again</div>")
    print("<div class=\"container pt-5\">")
    print("<h2>Login</h2><br><br>")
    # Print login form
    print("<form class=\"card p-5\" method=\"POST\" action=\"dashboard.py\">")
    print("<div class=\"form-group\">")
    print("<label for=\"exampleInputAccountNum1\">Account Number</label>")
    print("<input type=\"text\" oninput=\"this.value = this.value.replace(/[^0-9]/g, '').replace(/(\..*)\./g, '$1');\" maxlength=\"11\" class=\"form-control\" id=\"exampleInputAccountNum1\" aria-describedby=\"accountHelp\" placeholder=\"Enter Account no.\" name=\"ac_n\" required>")
    print("<small id=\"accountHelp\" class=\"form-text text-muted\">Please enter your bank account number.</small>") 
    print("</div>") 
    print("<div class=\"form-group\">") 
    print("<label for=\"exampleInputPassword1\">Password</label>") 
    print("<input type=\"password\" class=\"form-control\" id=\"exampleInputPassword1\" placeholder=\"Password\" name=\"pass\" required>") 
    print("</div>")
    print("<br><button type=\"submit\" class=\"btn btn-primary\">Login</button>") 
    print("</form>") 
    print("</div>")

def showRegisterationError(err_msg):
    printHTMLstart()
    printHTMLhead()
    print("<div class=\"container bg-danger text-center p-2 mt-5\"><div class=\"card p-auto\"><p class=\"lead\">")
    print(err_msg)
    print("<a href=\"register.py\">Register here</a> with correct account details.</p></div></div>")
    # printHTMLbodywithRegisterForm()
    printHTMLend()

# Get form values
form = cgi.FieldStorage()
acc_num = form.getvalue('ac_n')
full_name = form.getvalue('f_nm')
email = form.getvalue('em_id')
password = form.getvalue('pass')

try:
    logfile = open('my_account_app.log','a')
except:
    print('Error opening log file..')
else:
    logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [User] - '+'GET request at http://localhost/cgi-bin/bankingsystem/login.py\n')

if acc_num==None:
    printHTMLstart()
    printHTMLhead()
    printHTMLbody()
    printHTMLend()
else:
    # Config object for database connection
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
            logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Connection request at http://localhost/cgi-bin/bankingsystem/login.py | Failed to connect to database.\n')
            logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Wrong database user name or password. - login.py\n')
            logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Check admin details provided in `config` at line 80 - login.py.\n')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Connection request at http://localhost/cgi-bin/bankingsystem/login.py | Failed to connect to database.\n')
            logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Database does not exist. - login.py\n')
            logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Check database details provided in `config` at line 80 - login.py.\n')
        else:
            logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Error in conn.connect() at line 88 - login.py.\n')
            logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Error details : '+err)
    else:
        logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Database connection successful! - login.py\n')
        update_full_name = ("UPDATE userinfo "
                        "SET full_name = %s"
                        "WHERE account_num = %s AND full_name IS NULL")
        update_email = ("UPDATE userinfo "
                        "SET email_id = %s"
                        "WHERE account_num = %s AND email_id IS NULL")
        update_password = ("UPDATE userinfo "
                        "SET password = %s"
                        "WHERE account_num = %s AND password IS NULL")
        cursor = db_conn.cursor()
        try:
            logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [User] - '+'Handle user request at http://localhost/cgi-bin/bankingsystem/register.py: Register user.\n')
            cursor.execute(update_full_name,(full_name, acc_num))
            cursor.execute(update_email,(email, acc_num))
            cursor.execute(update_password,(password, acc_num))
        except:
            logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Error at cursor.execute(). - login.py\n')
        else:
            if str(cursor.rowcount)=='0':
                logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [User] - '+'Error handling request: User registeration failed | Error details : Invalid login details::'+'account_num='+acc_num+'.\n')
                showRegisterationError('Please check your account details and try again.')
                cursor.close()
                db_conn.close()
                logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Database connection closed. - login.py\n')
            else:
                logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [User] - '+'Response at http://localhost/cgi-bin/bankingsystem/dashboard.py: User registered successfully | Userdetails:: accountnum='+acc_num+'.\n')
                db_conn.commit()
                logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Commit new changes to database. - login.py - Commit details - account_number='+acc_num+',fullname='+full_name+',email='+email+'\n')
                cursor.close()
                db_conn.close()
                logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Database connection closed. - login.py\n')
                # Print page
                printHTMLstart()
                printHTMLhead()
                print("<div class=\"alert alert-success text-center lead\" role=\"alert\">Registered Successfully! Please login to continue.</div>")
                printHTMLbody()
                printHTMLend()