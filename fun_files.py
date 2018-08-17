# This is a program that lets me experiment with file stuff

import os
os.chdir('C:/Users/pwheeler')

# print(os.listdir('C:/Users/pwheeler/Pictures'))
# os.mkdir('organized')
# os.rename('C:/Users/pwheeler/ACHE.jpg','C:/Users/pwheeler/Pictures/ACHE.jpg')
# print (os.getcwd())


# def extract_place (a):
#     loop=0
#     position = []
#     places = []
#     for i in a:
#         if a[loop]=="_":
#             position.append(loop)
#             loop=loop+1
#         else:
#             loop=loop+1
#     # print (position[0])
#     places.append(a[position[0]+1:position[1]])
#     # print (places)
#     print (loop)
#     print (position)
#     print (places)

def extract_place (a):
    return a.split("_")[0:]

def make_place_dir (a):
    for i in a:
        os.mkdir(i)

print (extract_place("2018-06-06_MountainView_16:20:00.jpg"))