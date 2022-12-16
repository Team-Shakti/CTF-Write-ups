from base64 import b64decode

x = 'ZFlSXGVaVGVXbFRjamFlIVAiZFBkZmEkY1BWUmtqampqampQWFQlJCNlYyYnWCVlYyYlbg=='

x = b64decode(x)
flag = ''
for i in x:
    flag = flag + chr(i +15)
