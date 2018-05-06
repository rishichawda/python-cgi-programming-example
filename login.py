#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import cgi,cgitb
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
    print("<title>Banking System using CGI</title>")
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
    print("<div class=\"container pt-5\">")
    print("<h2>Login</h2><br><br>")
    # Print signup form
    print("<form class=\"card p-5\" method=\"POST\" action=\"dashboard.py\">")
    print("<div class=\"form-group\">")
    print("<label for=\"exampleInputAccountNum1\">Account Number</label>")
    print("<input type=\"text\" class=\"form-control\" id=\"exampleInputAccountNum1\" aria-describedby=\"accountHelp\" placeholder=\"Enter Account no.\" name=\"ac_n\" required>")
    print("<small id=\"accountHelp\" class=\"form-text text-muted\">Please enter your bank account number.</small>") 
    print("</div>") 
    # print("<div class=\"form-group\">")
    # print("<label for=\"exampleInputEmail1\">Email address</label>")
    # print("<input type=\"email\" class=\"form-control\" id=\"exampleInputEmail1\" aria-describedby=\"emailHelp\" placeholder=\"Enter email\">") 
    # print("<small id=\"emailHelp\" class=\"form-text text-muted\">We'll never share your email with anyone else.</small>") 
    # print("</div>") 
    print("<div class=\"form-group\">") 
    print("<label for=\"exampleInputPassword1\">Password</label>") 
    print("<input type=\"password\" class=\"form-control\" id=\"exampleInputPassword1\" placeholder=\"Password\" name=\"pass\" required>") 
    print("</div>")
    # print("<div class=\"form-group form-check\">") 
    # print("<input type=\"checkbox\" class=\"form-check-input\" id=\"exampleCheck1\">") 
    # print("<label class=\"form-check-label\" for=\"exampleCheck1\">Check me out</label>") 
    # print("</div>") 
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
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        # check_acc = ("SELECT * FROM accountinfo "
        #                 "WHERE account_num = %s")
        # register_user = ("INSERT INTO userinfo "
        #         "(full_name, account_num, email_id, password) "
        #         "VALUES (%s, %s, %s, %s)")
        update_full_name = ("UPDATE userinfo "
                        "SET full_name = %s"
                        "WHERE account_num = %s")
        update_email = ("UPDATE userinfo "
                        "SET email_id = %s"
                        "WHERE account_num = %s")
        update_password = ("UPDATE userinfo "
                        "SET password = %s"
                        "WHERE account_num = %s")
        cursor = db_conn.cursor()
        # cursor.close()
        # rows = cursor.fetchall()
        # if len(rows)==0:
        #     showRegisterationError()
        #     cursor.close()
        #     db_conn.close()
        # else:
        # user_data = (full_name, acc_num, email, password)
        # cursor = db_conn.cursor()
        try:
            # cursor.execute(register_user, user_data)
            cursor.execute(update_full_name,(full_name, acc_num))
            cursor.execute(update_email,(email, acc_num))
            cursor.execute(update_password,(password, acc_num))
        except:
            showRegisterationError('Please check your account details and try again.')
            cursor.close()
            db_conn.close()
        else:
            db_conn.commit()
            cursor.close()
            db_conn.close()
            # Print page
            printHTMLstart()
            printHTMLhead()
            print("<div class=\"alert alert-success text-center lead\" role=\"alert\">Registered Successfully! Please login to continue.</div>")
            printHTMLbody()
            printHTMLend()