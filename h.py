from googleapiclient.discovery import build
my_api_key = "AIzaSyDP1iLdfgvct3BQKLAKQaD3UG6LVgiJSLs"
my_cse_id = "007944217764671561800:ve3xx693pke"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res
result = google_search("xss", my_api_key, my_cse_id)
print(result)    
