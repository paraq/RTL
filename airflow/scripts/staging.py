def staging(url, start_date, end_date):
     import requests
     import json
     api_request = "{}?startPeriod={}&endPeriod={}&format=jsondata".format(url, start_date, end_date)
     print(api_request)
     response = requests.get(api_request)
     print(response.status_code)
     data = response.text
     with open("/data/data.json", "w") as f:
         json.dump(json.loads(data), f)

