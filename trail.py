from googleapiclient.discovery import build
service = build("customsearch", "v1", developerKey="AIzaSyA7k7eZAzVdsm1cWDGDlk2IQFINiTXMAf8")
res = service.cse().list(q="Tiger", cx="b1fd71c797e6043d5", num=3).execute()
for item in res.get("items", []):
    print(item["link"])
