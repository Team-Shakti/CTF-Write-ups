flag='shaktictf{#####REDACTED#####}'
s=''
for i in flag:
    s+=chr((ord(i)-15))
print(base64.b64encode(bytes(s,'utf-8')))

#b'ZFlSXGVaVGVXbFRjamFlIVAiZFBkZmEkY1BWUmtqampqampQWFQlJCNlYyYnWCVlYyYlbg=='
