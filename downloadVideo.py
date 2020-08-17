import requests
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    , 'Accept': '*/*'
    , 'Origin': 'https://www.kanxue.com',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.kanxue.com/'
}

num = 0
file = open('kanxue', 'wb+')
while num <= 64:

    if num < 10:
        url = 'https://video.kanxue.com/36_431_YIqoQUTdfDfuRtql00000' + str(num) + '.ts'
    else:
        url = 'https://video.kanxue.com/36_431_YIqoQUTdfDfuRtql0000' + str(num) + '.ts'
    resp = requests.get(url, headers=headers, stream=True)
    num += 1
    print(resp, num)

    file.write(resp.content)
