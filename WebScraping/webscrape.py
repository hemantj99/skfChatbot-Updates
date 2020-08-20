import sys
import urllib.request
import urllib.parse
import re
from urllib.request import urlopen as ureqs
from bs4 import BeautifulSoup as soup
from googleapiclient.discovery import build
def remove_duplicates(string):
    final_list=[]
    for q in string:
        if q not in final_list:
            final_list.append(q)
    return final_list 
query = input("enter the query\n")
print("1) Google Search Results\n")
print("2) Youtube Links\n")
choice=input("Enter The choice\n")
if choice=='1':
    my_api_key = "AIzaSyDP1iLdfgvct3BQKLAKQaD3UG6LVgiJSLs"
    my_cse_id = "007944217764671561800:ve3xx693pke"
    def google_search(search_term, api_key, cse_id, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        return res
    results = google_search(query, my_api_key, my_cse_id)
    print("\n*********Google Search Results*********\n")
    print("Title == " +results['items'][0]['title'])
    print("Link ==" +results['items'][0]['link'])
    snippet=results['items'][0]['snippet'].replace('\n',"")
    html_snippet=results['items'][0]['htmlSnippet'].replace('\n',"")
    html_snippet= html_snippet.replace("<b>","")
    html_snippet= html_snippet.replace("</b>","")
    html_snippet= html_snippet.replace("<br>","")
    html_snippet= html_snippet.replace("&nbsp;...",".")
    print("Description == " + snippet+html_snippet)
    print("\n\n")
    #print(type(results))

    print("Title == " +results['items'][1]['title'])
    print("Link ==" +results['items'][1]['link'])
    snippet=results['items'][1]['snippet'].replace('\n',"")
    html_snippet=results['items'][1]['htmlSnippet'].replace('\n',"")
    html_snippet= html_snippet.replace("<b>","")
    html_snippet= html_snippet.replace("</b>","")
    html_snippet= html_snippet.replace("<br>","")
    html_snippet= html_snippet.replace("&nbsp;...",".")
    print("Description == " + snippet+html_snippet)


elif choice=='2':
    query_string = urllib.parse.urlencode({"search_query" : query})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())

    final_search=remove_duplicates(search_results)
    print("\n********YouTube Links*********\n")
    print("http://www.youtube.com/watch?v=" + final_search[0])
    print("\nhttp://www.youtube.com/watch?v=" + final_search[1])
    print("\nhttp://www.youtube.com/watch?v=" + final_search[2])
    print("\nhttp://www.youtube.com/watch?v=" + final_search[3])
else:
    print("Enter correct choice")
