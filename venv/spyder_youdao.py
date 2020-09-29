import requests
import json
def get_translate_date(key):
     url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
     salt1=get_salt()
     salt2=get_salt()
     Form_data={'i': key,'from': 'AUTO','to': 'AUTO','smartresult': 'dict','client': 'fanyideskweb','salt': str(salt1),'sign': getSign(key,salt1),'lts':str(salt2),'bv':'fb09df70417ed9e84c91bebfdf6a76a8','doctype': 'json','version': '2.1','keyfrom': 'fanyi.web','action': 'FY_BY_REALTlME'}
     response=requests.post(url,data=Form_data)
     content=json.loads(response.text)
     print(content)

def get_salt():
   import time,random
   salt=int(time.time()*1000) + random.randint(0,10)
   print('salt is' + str(salt))
   return salt

def get_md5(v):
   import hashlib
   md5= hashlib.md5()
   md5.update(v.encode("utf-8"))
   sign=md5.hexdigest()
   return sign

def getSign(key,salt):
   sign="fanyideskweb" + key + str(salt) + "]BjuETDhU)zqSxf-=B#7m"
   print('sign1 '+ sign )
   sign=get_md5(sign)
   print('sign ' + sign )
   return sign

if __name__=='__main__':
   get_translate_date('我爱中国')
