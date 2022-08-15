import json
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class RetrieveData:


<< << << < HEAD
 johnRequests = requests.get(
      'https://api.missingkids.org/missingkids/servlet/JSONDataServlet', timeout=1)

  janeRequests = requests.get(
       'https://www.missingkids.org/gethelpnow/search/poster-results')

   if (johnRequests.status_code != 200 or janeRequests.status_code != 200):
        print("Error occured while connecting to HTTP, status code is: " +
              str(johnRequests.status_code))

    johnRequests.encoding = 'utf-8'
    # johnRequests.text
    data = johnRequests.text

    print(data)

# test
    # print(data)

    #each individual person is known as a screen and has a corresponding id#
    #posterData.caseNumber // posterData.seqNumber
    # ng-attr-data-url
    # data-json
    # http://www.missingkids.org/missingkids/servlet/JSONDataServlet?action=longTermMissing&term=year&start=15&end=10&LanguageId=en_US
    # /missingkids/servlet/PublicHomeServlet
    # /content\/ dam\/ missingkids\/ pdfs | content\/ dam\/ netsmartz\/ pdfs | content\/ dam\/ netsmartz\/ downloadable | content\/ dam\/ kidsmartz\/ pdfs/
== == == =
 session = requests.session()
  firstName1 = "Jane"
   firstName2 = "John"
    lastName = "Doe"
    state_abbrev = "CA"
    response = session.get(
        "http://www.missingkids.com/missingkids/servlet/JSONDataServlet?action=publicSearch&searchLang=en_US&search=new&subjToSearch=child&missState=" + state_abbrev + "&missCountry=US")
    print("{} {}").format(response.status_code, response.reason)
>>>>>> > 4a82f2bc753f40202feac8b2960c23a1a4ac3a82
