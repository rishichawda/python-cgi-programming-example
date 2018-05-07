#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import cgi,cgitb
cgitb.enable()

def printHTMLstart():
    print("Content-Type: text/html\r\n")
    print("\r\n")
    print("<html>")

def printHTMLhead():
    # Print head of the html page
    print("<head>")
    print("<link rel=\"stylesheet\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css\" integrity=\"sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB\" crossorigin=\"anonymous\">")
    print("<title>Transfer Money</title>")
    print("<style>#formError{display:none}</style>")
    print("</head>")

def printHTMLbody():
    print("<div class=\"container p-2\">")
    print("<h2 class=\"lead my-4\">Transfer details : </h2>")
    print("<div class=\"container card bg-light p-3\">")
    print("<h2 id=\"formError\" class=\"text-danger lead\">All fields are required.</h2>")
    print("<form  onsubmit=\"return transfer_money()\" action=\"transfer_request.py\" method=\"POST\">")
    print("<input id=\"user_acc\" name=\"user_accnum\" style=\"display:none;\">")
    print("<input id=\"user_bal\" name=\"user_accbal\" style=\"display:none;\">")
    print("<div class=\"form-group\">")
    print("<label for=\"exampleInputPayeeAccountNumber\">Payee Account Number</label>")
    print("<input type=\"text\" class=\"form-control\" id=\"exampleInputPayeeAccountNumber\" aria-describedby=\"PayeeAccountNumberHelp\" placeholder=\"Enter Account Number\" name=\"transfer_details\">")
    print("<small id=\"PayeeAccountNumberHelp\" class=\"form-text text-muted\">Please enter Payee account number.</small>")
    print("</div>")
    print("<div class=\"form-group\">")
    print("<label for=\"exampleInputPayeeAccountBank\">Payee Account Bank</label>")
    print("<input type=\"text\" class=\"form-control\" id=\"exampleInputPayeeAccountBank\" aria-describedby=\"PayeeAccountBankHelp\" placeholder=\"Enter Account Bank\" name=\"transfer_details\">")
    print("<small id=\"PayeeAccountBankHelp\" class=\"form-text text-muted\">Please enter Payee account bank name.</small>")
    print("</div>")
    print("<div class=\"form-group\">")
    print("<label for=\"exampleInputTransferAmount\">Amount</label>")
    print("<input type=\"text\" class=\"form-control\" id=\"exampleInputTransferAmount\" aria-describedby=\"TransferAmountHelp\" placeholder=\"Amount in Rupees\" name=\"transfer_details\">")
    print("<small id=\"TransferAmountHelp\" class=\"form-text text-muted\">Enter transfer amount in Rupees.</small>")
    print("</div>")
    print("<button type=\"submit\" class=\"btn btn-success\">Transfer</button>")
    print("</form>")
    print("</div>")
    print("</div>")


def printHTMLend():
    # Add script tags
    print("<script src=\"https://code.jquery.com/jquery-3.3.1.min.js\"></script>")
    print("<script>$(document).ready(function(){document.getElementById(\"user_acc\").value=window.opener.document.getElementById(\"user_acc_num\").innerHTML;document.getElementById(\"user_bal\").value=window.opener.document.getElementById(\"user_acc_bal\").innerHTML;});function transfer_money(){var transfer_details=document.getElementsByName(\"transfer_details\");if(transfer_details[0].value==='' || transfer_details[1].value==='' || transfer_details[2].value===''){document.getElementById(\"formError\").style.display=\"block\";return false;}else{document.getElementById(\"formError\").style.display=\"none\";if(confirm(\"Proceed with transaction?\")){return true;}else{return false}}}</script>")
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