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
    print("<style>#add_payee_form,#formError,#payeedetailsshow{display:none}</style>")
    print("</head>")

def redirectToLogin():
    printHTMLstart()
    print("  <head>")
    print("    <meta http-equiv=\"refresh\" content=\"0;url=login.py\" />") 
    print("  </head>")
    print("</html>")

def printHTMLend():
    # Add script tags
    print("<script>function show_add_payee_form(){document.getElementById(\"add_payee_form\").style.display=\"block\";payee_details=document.getElementsByName(\"payee_details\");payee_details[0].value=payee_details[1].value=payee_details[2].value='';document.getElementById(\"add_payee_button\").style.display=\"none\";}</script>")
    print("<script>function add_payee(){payee_details=document.getElementsByName(\"payee_details\");if(payee_details[0].value==='' || payee_details[1].value==='' || payee_details[2].value===''){document.getElementById(\"formError\").style.display=\"block\";}else{document.getElementById(\"add_payee_form\").style.display=\"none\";document.getElementById(\"add_payee_button\").style.display=\"block\";var new_payee=document.createElement(\"div\");var node=document.createElement(\"p\");var textnode=document.createTextNode(\"Payee name :\"+payee_details[0].value);node=document.createElement(\"p\");node.appendChild(textnode);new_payee.appendChild(node);textnode=document.createTextNode(\"Payee account number :\"+payee_details[1].value);node=document.createElement(\"p\");node.appendChild(textnode);new_payee.appendChild(node);textnode=document.createTextNode(\"Payee bank name :\"+payee_details[2].value);node=document.createElement(\"p\");node.appendChild(textnode);new_payee.appendChild(node);new_payee.classList=\"container bg-light mt-2 p-2\";document.getElementById(\"payeedetailsshow\").appendChild(new_payee);document.getElementById(\"payeedetailsshow\").style.display=\"block\"}}</script>")
    print("<script src=\"https://code.jquery.com/jquery-3.3.1.slim.min.js\" integrity=\"sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo\" crossorigin=\"anonymous\"></script>")
    print("<script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js\" integrity=\"sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49\" crossorigin=\"anonymous\"></script>")
    print("<script src=\"https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js\" integrity=\"sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T\" crossorigin=\"anonymous\"></script>")
    # Print closing body tag for html
    print("</body>")
    # End html page
    print("</html>")

def showUserDetails(accnum,accbal):
    print("<div class=\"row\">")
    print("<div class=\"col-md-6 text-center\">Account Number : ")
    print(accnum)
    print("</div>")
    print("<div class=\"col-md-6 text-center\">Account Balance : Rs. ")
    print(accbal)
    print("</div>")
    print("</div>")

def printHTMLnavbar(username):
    print("<nav class=\"navbar navbar-light bg-light\">")
    print("<a class=\"navbar-brand\" href=\"#\">Bank</a>")
    print("<p class=\"lead my-auto\">Hello,")
    print(username)
    print("</p>")
    print("<div class=\"my-2 my-lg-0\">")
    print("<a class=\"nav-link\" href=\"login.py\">Logout</a>")
    print("</div>")
    print("</nav>")

def printAddPayeeForm():
    print("<div class=\"container card bg-light p-2 my-2 mt-4\" id=\"add_payee_form\">")
    print("<h2 id=\"formError\" class=\"text-danger lead\">All fields are required.</h2>")
    print("<div class=\"form-group\">")
    print("<label for=\"exampleInputPayeeAccountNumber\">Payee Account Number</label>")
    print("<input type=\"text\" class=\"form-control\" id=\"exampleInputPayeeAccountNumber\" aria-describedby=\"PayeeAccountNumberHelp\" placeholder=\"Enter Account number\" name=\"payee_details\" required>")
    print("<small id=\"PayeeAccountNumberHelp\" class=\"form-text text-muted\">Account number of the Payee.</small>")
    print("</div>")
    print("<div class=\"form-group\">")
    print("<label for=\"exampleInputPayeeAccountName\">Payee Account Name</label>")
    print("<input type=\"text\" class=\"form-control\" id=\"exampleInputPayeeAccountName\" aria-describedby=\"PayeeAccountNameHelp\" placeholder=\"Enter Account name\" name=\"payee_details\" required>")
    print("<small id=\"PayeeAccountNameHelp\" class=\"form-text text-muted\">Full name associated with the bank account number.</small>")
    print("</div>")
    print("<div class=\"form-group\">")
    print("<label for=\"exampleInputPayeeAccountBank\">Payee Account Bank</label>")
    print("<input type=\"text\" class=\"form-control\" id=\"exampleInputPayeeAccountBank\" aria-describedby=\"PayeeAccountBankHelp\" placeholder=\"Enter Bank name\" name=\"payee_details\" required>")
    print("<small id=\"PayeeAccountBankHelp\" class=\"form-text text-muted\">Name of the bank associated with the bank account number.</small>")
    print("</div>")
    print("<button class=\"btn btn-success\" onclick=\"add_payee()\">Add</button>")
    print("</div>")

def printRemovePayeeForm():
    print("<div class=\"container card bg-light p-2 my-2 mt-4\" id=\"add_payee_form\">")
    print("<h2 id=\"formError\" class=\"text-danger lead\">All fields are required.</h2>")
    print("<div class=\"form-group\">")
    print("<label for=\"exampleInputPayeeAccountNumber\">Payee Account Number</label>")
    print("<input type=\"text\" class=\"form-control\" id=\"exampleInputPayeeAccountNumber\" aria-describedby=\"PayeeAccountNumberHelp\" placeholder=\"Enter Account number\" name=\"payee_details\" required>")
    print("<small id=\"PayeeAccountNumberHelp\" class=\"form-text text-muted\">Account number of the Payee.</small>")
    print("</div>")
    print("<div class=\"form-group\">")
    print("<label for=\"exampleInputPayeeAccountBank\">Payee Account Bank</label>")
    print("<input type=\"text\" class=\"form-control\" id=\"exampleInputPayeeAccountBank\" aria-describedby=\"PayeeAccountBankHelp\" placeholder=\"Enter Bank name\" name=\"payee_details\" required>")
    print("<small id=\"PayeeAccountBankHelp\" class=\"form-text text-muted\">Name of the bank associated with the bank account number.</small>")
    print("</div>")
    print("<button class=\"btn btn-success\" onclick=\"remove_payee()\">Remove</button>")
    print("</div>")

# Get form values
show_add_payee_form = False
form = cgi.FieldStorage()
acc_num = form.getvalue('ac_n')
password = form.getvalue('pass')

if form.getvalue('ac_n')==None:
    redirectToLogin()
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
        cursor = db_conn.cursor()
        check_user = ("SELECT * FROM userinfo "
                        "WHERE account_num=%s AND password=%s")
        cursor.execute(check_user,(str(acc_num),password))
        rows = cursor.fetchall()
        if len(rows)==0:
            redirectToLogin()
        else:
            printHTMLstart()
            printHTMLhead()
            # Print body of the html page
            print("<body>")
            printHTMLnavbar(rows[0][0])
            print("<div class=\"container card p-5 mt-5\">")
            showUserDetails(rows[0][1],rows[0][2])
            print("<div id=\"payeedetailsshow\"></div>")
            printAddPayeeForm()
            printRemovePayeeForm()
            print("<button class=\"btn btn-info mt-4\" id=\"add_payee_button\" onclick=\"show_add_payee_form()\">Add Payee</button>")
            print("<button class=\"btn btn-warning mt-2\" id=\"remove_payee_button\" onclick=\"show_remove_payee_form()\">Remove Payee</button>")
            print("</div>")
            printHTMLend()