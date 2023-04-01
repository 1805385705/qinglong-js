from urllib3 import PoolManager
import os
import requests
import sys
import time

# 检查手机号是否相同
#def check_phone_numbers():
credentials = os.environ.get('hzj')
if credentials:
  phone = credentials.split('&')
#  for phone in phones:
#    print(phone)
  if len(phone) == len(set(phone)) and len(phone[0]) == 11:
    cookies = {
      'guardret': 'TmyO8+x0JOWZvOEw+8WW6Q==',
      'PHPSESSID': '170c3a0239d5c7570964ab54d7e904fc',
      'Let_IndexUsername': '1594721425',
      'Let_IndexPassword': 'd3d4acd35c429c99ab25e82306172e5b',
      'guard': '8d93b49ay6Xoz12FKQH41M5NsBAYhIVRSw==',
    }
    headers = {
      'Host': 'dxhz.suol.me',
      'Connection': 'keep-alive',
      # 'Content-Length': '24',
      'Accept': '*/*',
      'X-Requested-With': 'XMLHttpRequest',
      'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2007J17C Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36',
      'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'Origin': 'http://dxhz.suol.me',
      'Referer': 'http://dxhz.suol.me/index/index.html',
      # 'Accept-Encoding': 'gzip, deflate',
      'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
      # 'Cookie': 'guardret=TmyO8+x0JOWZvOEw+8WW6Q==; PHPSESSID=170c3a0239d5c7570964ab54d7e904fc; Let_IndexUsername=1594721425; Let_IndexPassword=d3d4acd35c429c99ab25e82306172e5b; guard=8d93b49ay6Xoz12FKQH41M5NsBAYhIVRSw==',
    }
    for num in phone:
      time.sleep(10)
      data = {
        'phone': num,
        'time': '25',
      }
      time.sleep(5)
#    for item in data:
      response = requests.post('http://dxhz.suol.me/index/ajax/order/act/add.html', cookies=cookies, headers=headers, data=data)
      
      print(num,response.text)
      sys.exit
  else:
    sys.exit('手机号相同或者错误，程序终止')

else:
  sys.exit('未找到环境变量hzj')
    



  


  