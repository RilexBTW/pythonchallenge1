import webbrowser
import time
import base64

s = 'aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS9zZWFyY2g/cT1tYWtlK3N1cmUrdG8rdmVyaWZ5K2NvZGUrYmVmb3JlK3lvdStydW4raXQ='

a = 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ=='

b = base64.b64decode(s)

url = base64.b64decode(a)


open = webbrowser.open


def openUrl():
   open(url)
   time.sleep(5)
   open(b)


openUrl()


