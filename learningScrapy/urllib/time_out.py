from urllib.request import urlopen

# Set time out value too short, may cause error
for i in range(1, 100):
    try:
        file = urlopen("http://yum.iqianyue.com", timeout=1)
        data = file.read()
        print(len(data))
    except Exception as e:
        print("Error-->" + str(e))