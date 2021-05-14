import requests

user_ids = []
# send requests for attendee lists, 1 page with 100 result limit at a time
for page_no in range(30):
    # needs access token + api key
    attendee_list_data = {"current_page":str(page_no),"isPaginate":1,"sort":2,"input":"","filter":"0,0,0","limit":100,"event_id":4284,"organiser_id":897707,"api_key":,"access_token":,"app_version":"1.0.0","device_type":"WEB","userProfileFields":{}}
    attendee_list_req = requests.post("https://pyconus2021.hubilo.com/api/v1/app/paginate_attendee_list_v2", data=attendee_list_data)
    attendee_list = attendee_list_req.json()
    # idk just in case something goes wrong
    try:
        user_ids += [x['_id'] for x in attendee_list['data']['attendees']]
    except Exception as e:
        print(Exception)
        continue
    # looks like it tops out at 1744
    print(len(user_ids))

outfile = open('user_ids.txt', 'w')
outfile.write(str(user_ids))
