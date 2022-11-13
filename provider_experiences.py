from faker import Faker
import requests
import datetime

fake = Faker()

provider_filter_path = "http://192.168.100.69:3000/providers/filter"
path = "http://192.168.100.69:3000/provider-experiences"

payload = {
    "title": "",
    "company": "",
    "startDate": "2022-11-13T13:59:40.285Z",
    "endDate": "2022-11-13T13:59:40.285Z",
    "isCurrent": False,
    "providerId": 0
}

response = requests.get(provider_filter_path)
if response.ok:
    for i in range(100):
        providers = response.json()
        for provider in providers["data"]:
            title = fake.job()
            company = fake.company()
            # ISO 8601 format from faker
            start_date = fake.date_time_between(start_date="-10y", end_date="now").isoformat()
            end_date = fake.date_time_between(start_date="-10y", end_date="now").isoformat()
            print(start_date)
            print(end_date)
            payload["title"] = title
            payload["company"] = company
            payload["startDate"] = start_date
            payload["endDate"] = end_date
            payload["providerId"] = provider["id"]
            _ = requests.post(path, json=payload)
