import requests

user_ids = eval(open('user_ids.txt', 'r').read())
print(len(user_ids))
for id in user_ids:
    # needs access token + api key
    view_profile_data = {"access_token":,"organiser_id":897707,"event_id":4284,"api_key":,"app_version":"1.0.0","device_type":"WEB","target":id}
    view_profile_req = requests.post("https://pyconus2021.hubilo.com/api/v1/app/view_profile_v2", data=view_profile_data)
    if view_profile_req.status_code != 200:
        print(view_profile_req.text)
