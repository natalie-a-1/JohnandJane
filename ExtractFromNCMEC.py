import json
import requests


class RetrieveData:
    session = requests.session()
    firstName1 = "Jane"
    firstName2 = "John"
    lastName = "Doe"
    state_abbrev = "CA"
    response = session.get(
        "http://www.missingkids.com/missingkids/servlet/JSONDataServlet?action=publicSearch&searchLang=en_US&search=new&subjToSearch=child&missState=" + state_abbrev + "&missCountry=US")
    print("{} {}").format(response.status_code, response.reason)
    
