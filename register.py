#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import cgi,cgitb,datetime
cgitb.enable()

def printHTMLbody():
    # Print body of the html page
    print("<body>")
    print("<div class=\"container pt-5\">")
    print("<h2>Register</h2><br><br>")
    # Print signup form
    print("<form class=\"card p-5\" action=\"login.py\" method=\"POST\">")
    print("<div class=\"form-group\">")
    print("<label for=\"exampleInputAccountNum1\">Account Number</label>")
    print("<input type=\"text\" oninput=\"this.value = this.value.replace(/[^0-9]/g, '').replace(/(\..*)\./g, '$1');\" maxlength=\"11\" class=\"form-control\" id=\"exampleInputAccountNum1\" aria-describedby=\"accountHelp\" placeholder=\"Enter Account no.\" name=\"ac_n\" required>")
    print("<small id=\"accountHelp\" class=\"form-text text-muted\">Please enter your bank account number.</small>") 
    print("</div>") 
    print("<div class=\"form-group\">")
    print("<label for=\"exampleInputFullName1\">Full Name</label>")
    print("<input type=\"text\" class=\"form-control\" id=\"exampleInputFullName1\" aria-describedby=\"nameHelp\" placeholder=\"Enter your full name associated with account\" name=\"f_nm\" required>")
    print("<small id=\"nameHelp\" class=\"form-text text-muted\">Please enter your bank account number.</small>") 
    print("</div>") 
    print("<div class=\"form-group\">")
    print("<label for=\"exampleInputEmail1\">Email address</label>")
    print("<input type=\"email\" class=\"form-control\" id=\"exampleInputEmail1\" aria-describedby=\"emailHelp\" placeholder=\"Enter email\" name=\"em_id\" required>") 
    print("<small id=\"emailHelp\" class=\"form-text text-muted\">We'll never share your email with anyone else.</small>") 
    print("</div>") 
    print("<div class=\"form-group\">") 
    print("<label for=\"exampleInputPassword1\">Password</label>") 
    print("<input type=\"password\" class=\"form-control\" id=\"exampleInputPassword1\" placeholder=\"Password\" name=\"pass\" required>") 
    print("</div>")
    print("<br><button type=\"submit\" class=\"btn btn-primary\">Register now!</button>") 
    print("</form>") 
    print("</div>") 

def printHTMLhead():
    # Print head of the html page
    print("<head>")
    print("<link rel=\"stylesheet\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css\" integrity=\"sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB\" crossorigin=\"anonymous\">")
    print("<title>Registeration Page</title>")
    print("</head>")

def printHTMLstart():
    print("Content-Type: text/html\r\n")
    print("\r\n")
    print("<html>")

def printHTMLend():
    # Add script tags
    print("<script src=\"https://code.jquery.com/jquery-3.3.1.slim.min.js\" integrity=\"sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo\" crossorigin=\"anonymous\"></script>")
    print("<script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js\" integrity=\"sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49\" crossorigin=\"anonymous\"></script>")
    print("<script src=\"https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js\" integrity=\"sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T\" crossorigin=\"anonymous\"></script>")
    # Print closing body tag for html
    print("</body>")
    # End html page
    print("</html>")


printHTMLstart()
printHTMLhead()
printHTMLbody()
printHTMLend()


try:
    logfile = open('my_account_app.log','a')
except:
    print('Error opening log file..')
else:
    logfile.write('['+ str(datetime.datetime.now().isoformat()) +'] - [User] - '+'GET request at http://localhost/cgi-bin/bankingsystem/register.py\n')
