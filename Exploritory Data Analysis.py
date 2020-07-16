import urllib.request
import re
import os
import socket

socket.setdefaulttimeout(3)

# url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
# urllib.request.urlretrieve(url, '/Users/joycemegumi/Documents/GitHub/FashionRecSys/Street2Fashion_Dataset/photos/images/test.jpg')


stores = {}
with open("./Street2Fashion_Dataset/storenames.txt", "r") as f:
    data = f.read().splitlines()
for line in data:
    stores[line.lower()] = []
    path = './Street2Fashion_Dataset/photos/images/' + line.lower()
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)
print(stores)


storeLinks = []
with open("./Street2Fashion_Dataset/photos/photos_copy.txt", "rt") as f:
    data = f.read().splitlines()
for line in data:
    for sName in stores:
        if line.__contains__(sName):
            stores[sName].append({
                "id": line[:9],
                "url": line[10:]
            })


for storeName, store in stores.items():
    for image in store:
        path = './Street2Fashion_Dataset/photos/images/' + storeName + '/' + image['id'] + '.jpg'
        if os.path.exists(path):
            print('Skipping due to existing image')
            continue
        print('Fetching image: ' + image['url'])
        try:
            urllib.request.urlretrieve(
                image['url'],
                path, 
            )
        except Exception as e:
            print('Couldn\'t fetch photo')


print(len(storeLinks))
