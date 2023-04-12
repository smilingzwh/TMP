import requests
import time
URL = 'https://jsonplaceholder.typicode.com/posts/{}/comments'
email_name = []

def get_time(func):
    def inner(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        end_time = time.time()
        print('总共耗时---->',end_time-start_time)
        return res
    return inner

@get_time
def send_request(url=URL):
    with open('./email.txt','w+') as fo:
        for num in range(1,101):
            req = requests.request(method='get',url=url.format(num))
            for data in req.json():
                email_name.append(data['email'])
                fo.write(data['email'])
                fo.write('\n')
    return email_name
if __name__ == '__main__':
    res = send_request()
    print(res)