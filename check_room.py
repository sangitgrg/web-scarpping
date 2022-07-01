import requests
import configparser

from mail_sender import SendMail

url = 'https://chintai.sumai.ur-net.go.jp/chintai/api/bukken/detail/detail_bukken_room/'
headers = {'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}

config = configparser.ConfigParser()
config.read('config.ini')
danchi_list = config['App']['lists']
email_message = ''

xx = danchi_list.split('\n')
for danchi in xx:
    danchi = danchi.strip()
    danchi_info = danchi.split(':')
    payload = {
        "rent_low": "",
        "rent_high": "",
        "floorspace_low": "",
        "floorspace_high": "",
        "shisya": danchi_info[0],
        "danchi": danchi_info[1],
        "shikibetu": 0,
        "newBukkenRoom": "",
        "orderByField": 0,
        "orderBySort": 0,
        "pageIndex": 0,
        "pageIndex": 0,
        "sp": ""
    }

    res = requests.post(url, data=payload)
    if(res.text != 'null'):
        first_val = res.json()
        avail_count =first_val[0]["allCount"]
        if(avail_count == '1'):
            email_message += f'{avail_count} rooms available at {danchi} at price {first_val[0]["rent"]} \n'
            #print(f'{avail_count} rooms available at {danchi} at price {first_val[0]["rent"]}')
        else:
            email_message += f'{avail_count} rooms available at {danchi} \n'
            #print(f'{avail_count} rooms available at {danchi}')
    else:
        email_message += f'no avialable at {danchi} \n'
        #print(f'no avialable at {danchi}')

SendMail(email_message)
