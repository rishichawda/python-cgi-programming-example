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
    print("<title>Dashboard</title>")
    print("<style>#add_payee_form,#formError,#payeedetailsshow,#nopayee_error,#remove_payee_form,#nosuchpayee_error{display:none}</style>")
    print("</head>")

def redirectToLogin():
    printHTMLstart()
    print("  <head>")
    print("    <meta http-equiv=\"refresh\" content=\"0;url=login.py\" />") 
    print("  </head>")
    print("</html>")

def printHTMLend():
    # Add script tags
    print("<script>function show_add_payee_form(){document.getElementById(\"add_payee_form\").style.display=\"block\";document.getElementById(\"remove_payee_button\").style.display=\"none\";$('.text-danger').hide();payee_details=document.getElementsByName(\"payee_details\");payee_details[0].value=payee_details[1].value=payee_details[2].value='';document.getElementById(\"add_payee_button\").style.display=\"none\";}function show_remove_payee_form(){if(document.querySelectorAll(\"#payeedetailsshow > div\").length===0){document.getElementById(\"nopayee_error\").style.display=\"block\";}else{document.getElementById(\"remove_payee_form\").style.display=\"block\";document.getElementById(\"add_payee_button\").style.display=\"none\";document.getElementById(\"remove_payee_button\").style.display=\"none\";}}</script>")
    print("<script>function open_transfer_dialogue(){window.open('transfer.py','','toolbar=no,location=no,status=no,menubar=no,scrollbars=yes,resizable=yes,width=470,height=430');}</script>")
    print("<script>function open_deposit_dialogue(){window.open('deposit.py','','toolbar=no,location=no,status=no,menubar=no,scrollbars=yes,resizable=yes,width=470,height=430');}</script>")
    print("<script>function add_payee(){payee_details=document.getElementsByName(\"payee_details\");if(payee_details[0].value==='' || payee_details[1].value==='' || payee_details[2].value===''){document.getElementById(\"formError\").style.display=\"block\";}else{document.getElementById(\"add_payee_form\").style.display=\"none\";document.getElementById(\"add_payee_button\").style.display=\"block\";document.getElementById(\"remove_payee_button\").style.display=\"block\";var new_payee=document.createElement(\"div\");var node=document.createElement(\"p\");var textnode=document.createTextNode(\"Payee name : \"+payee_details[0].value);node=document.createElement(\"p\");node.appendChild(textnode);new_payee.appendChild(node);textnode=document.createTextNode(\"Payee account number : \"+payee_details[1].value);node=document.createElement(\"p\");node.appendChild(textnode);new_payee.appendChild(node);textnode=document.createTextNode(\"Payee bank name : \"+payee_details[2].value);node=document.createElement(\"p\");node.appendChild(textnode);new_payee.appendChild(node);new_payee.classList=\"container bg-light mt-2 p-2\";document.getElementById(\"payeedetailsshow\").appendChild(new_payee);document.getElementById(\"payeedetailsshow\").style.display=\"block\"}}</script>")
    print("<script>function remove_payee(){var rpayee_details=document.getElementsByName(\"rpayee_details\");var rpayee_num=\"Payee account number : \"+rpayee_details[0].value;var rpayee_bank=\"Payee bank name : \"+rpayee_details[1].value;if(rpayee_details[0].value==='' || rpayee_details[1].value===''){document.getElementById(\"formErrorRemovePayee\").style.display=\"block\";}else{document.getElementById(\"formErrorRemovePayee\").style.display=\"none\";var added_payees=document.querySelectorAll(\"#payeedetailsshow > div\");var found_payee=false;for(i=0;i<added_payees.length;i++){var payee_details=added_payees[i];if(rpayee_num===payee_details.firstChild.nextSibling.innerHTML && rpayee_bank===payee_details.lastChild.innerHTML){found_payee=true;$('.text-danger').hide();if(confirm(\"Remove selected payee?\")){document.getElementById(\"payeedetailsshow\").removeChild(payee_details);document.getElementById(\"remove_payee_form\").style.display=\"none\";document.getElementById(\"add_payee_button\").style.display=\"block\";document.getElementById(\"remove_payee_button\").style.display=\"block\";rpayee_details[0].value=rpayee_details[1].value='';}}}if(!found_payee){document.getElementById(\"nosuchpayee_error\").style.display=\"block\";}}}</script>")
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
    print("<p class=\"pt-2\" id=\"user_acc_num\">")
    print(accnum)
    print("</p>")
    print("</div>")
    print("<div class=\"col-md-6 text-center\">Account Balance : ")
    print("<p class=\"pt-2\" id=\"user_acc_bal\">")
    print(accbal)
    print("</p>")
    print("</div>")
    print("</div>")

def printHTMLnavbar():
    print("<nav class=\"navbar navbar-light bg-light\">")
    print("<a class=\"navbar-brand\" href=\"#\">Project</a>")
    print("<div class=\"mr-auto\">")
    print("<button type=\"button\" class=\"btn btn-light\" onclick=\"open_transfer_dialogue()\">Transfer Money</button>")
    print("<button type=\"button\" class=\"btn btn-light\" onclick=\"open_deposit_dialogue()\">Deposit Money</button>")
    print("</div>")
    print("<div class=\"my-2 my-lg-0\">")
    print("<a class=\"nav-link\" href=\"login.py\">Logout</a>")
    print("</div>")
    print("</nav>")

def printAddPayeeForm():
    print("<div class=\"container card bg-light p-2 my-2 mt-4\" id=\"add_payee_form\">")
    print("<h2 id=\"formError\" class=\"text-danger lead\">All fields are required.</h2>")
    print("<div class=\"form-group\">")
    print("<label for=\"exampleInputPayeeAccountNumber\">Payee Account Number</label>")
    print("<input type=\"text\" class=\"form-control\" oninput=\"this.value = this.value.replace(/[^0-9]/g, '').replace(/(\..*)\./g, '$1');\" maxlength=\"11\" id=\"exampleInputPayeeAccountNumber\" aria-describedby=\"PayeeAccountNumberHelp\" placeholder=\"Enter Account number\" name=\"payee_details\" required>")
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
    print("<button type=\"button\" class=\"btn btn-outline-secondary\" onclick=\"$('#add_payee_form').hide();$('.tool-button').show();\">Cancel</button>")
    print("</div>")

def printRemovePayeeForm():
    print("<div class=\"container card bg-light p-2 my-2 mt-4\" id=\"remove_payee_form\">")
    print("<h2 id=\"formErrorRemovePayee\" class=\"text-danger lead\">All fields are required.</h2>")
    print("<h2 id=\"nosuchpayee_error\" class=\"text-danger lead\">Payee not found.</h2>")
    print("<div class=\"form-group\">")
    print("<label for=\"exampleInputPayeeAccountNumber\">Payee Account Number</label>")
    print("<input type=\"text\" oninput=\"this.value = this.value.replace(/[^0-9]/g, '').replace(/(\..*)\./g, '$1');\" maxlength=\"11\" class=\"form-control\" id=\"exampleInputPayeeAccountNumber\" aria-describedby=\"PayeeAccountNumberHelp\" placeholder=\"Enter Account number\" name=\"rpayee_details\" required>")
    print("<small id=\"PayeeAccountNumberHelp\" class=\"form-text text-muted\">Account number of the Payee.</small>")
    print("</div>")
    print("<div class=\"form-group\">")
    print("<label for=\"exampleInputPayeeAccountBank\">Payee Account Bank</label>")
    print("<input type=\"text\" class=\"form-control\" id=\"exampleInputPayeeAccountBank\" aria-describedby=\"PayeeAccountBankHelp\" placeholder=\"Enter Bank name\" name=\"rpayee_details\" required>")
    print("<small id=\"PayeeAccountBankHelp\" class=\"form-text text-muted\">Name of the bank associated with the bank account number.</small>")
    print("</div>")
    print("<button class=\"btn btn-danger\" onclick=\"remove_payee()\">Remove</button>")
    print("<button type=\"button\" class=\"btn btn-outline-secondary\" onclick=\"$('#remove_payee_form').hide();$('.tool-button').show();\">Cancel</button>")
    print("</div>")

# Get form values
show_add_payee_form = False
form = cgi.FieldStorage()
acc_num = form.getvalue('ac_n')
password = form.getvalue('pass')

try:
    logfile = open('my_account_app.log','a')
except:
    print('error opening log file..')
else:
    logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [User] - '+'GET request at http://localhost/cgi-bin/bankingsystem/dashboard.py\n')


if form.getvalue('ac_n')==None:
    logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Redirect request to http://localhost/cgi-bin/bankingsystem/login.py - dashboard.py\n')
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
    except conn.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Connection request at http://localhost/cgi-bin/bankingsystem/dashboard.py | Failed to connect to database.\n')
            logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Wrong database user name or password. - dashboard.py\n')
            logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Check admin details provided in `config` at line 128 - dashboard.py.\n')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Connection request at http://localhost/cgi-bin/bankingsystem/dashboard.py | Failed to connect to database.\n')
            logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Database does not exist. - dashboard.py\n')
            logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Check database details provided in `config` at line 128 - dashboard.py.\n')
        else:
            logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Error in conn.connect() at line 135 - dashboard.py.\n')
            logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Error details : '+err)
    else:
        logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Database connection successful! - dashboard.py\n')
        cursor = db_conn.cursor()
        check_user = ("SELECT * FROM userinfo "
                        "WHERE account_num=%s AND password=%s")
        cursor.execute(check_user,(str(acc_num),password))
        logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [User] - '+'Handle user request at http://localhost/cgi-bin/bankingsystem/dashboard.py: Login user.\n')
        rows = cursor.fetchall()
        if len(rows)==0:
            logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [User] - '+'Error handling request: User login failed | Error details : Invalid login details::'+'account_num='+acc_num+'.\n')
            printHTMLstart()
            print("  <head>")
            print("    <meta http-equiv=\"refresh\" content=\"0;url=login.py?loginattempt=1\" />") 
            print("  </head>")
            print("</html>")
        else:
            logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [User] - '+'Response at http://localhost/cgi-bin/bankingsystem/dashboard.py: User logged in | Userdetails:: accountnum='+acc_num+'.\n')
            printHTMLstart()
            printHTMLhead()
            # Print body of the html page
            print("<body>")
            printHTMLnavbar()
            print("<p class=\"lead my-auto ml-5 p-2\">Hello,")
            print(rows[0][0])
            print("</p>")
            print("<div class=\"container card p-5 mt-5\">")
            showUserDetails(rows[0][1],rows[0][2])
            print("<div id=\"payeedetailsshow\"></div>")
            print("<h2 id=\"nopayee_error\" class=\"text-danger lead mt-5\">Please add a Payee first.</h2>")
            printAddPayeeForm()
            printRemovePayeeForm()
            print("<button class=\"btn btn-info mt-4 tool-button\" id=\"add_payee_button\" onclick=\"show_add_payee_form()\">Add Payee</button>")
            print("<button class=\"btn btn-warning mt-2 tool-button\" id=\"remove_payee_button\" onclick=\"show_remove_payee_form()\">Remove Payee</button>")
            print("</div>")
            printHTMLend()
        cursor.close()
        db_conn.close()
        logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [Admin] - '+'Database connection closed. - dashboard.py\n')