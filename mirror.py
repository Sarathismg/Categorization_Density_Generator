import csv
import os
from PIL import Image


def flip_image(image_path, saved_location):
    image_obj = Image.open(image_path)
    rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
    rotated_image.save(saved_location)


dir1 = 'data/M_Sitting'
dir2 = 'data/M_Standing'


dir5 = 'data/Images/Dimensions'
dir6 = 'data/M_Images'

dir7 = 'data/Images'

files = os.listdir(dir1)
'''
for file in files:
    x = 0
    y = 0
    with open(dir5 + '/' + file, newline='') as csvfile:
        rd = csv.reader(csvfile)
        for row in rd:
            x = int(row[0])
            y = int(row[1])

    with open(dir1 + '/' + file, newline='') as csvfile:
        rd = csv.reader(csvfile)
        for row in rd:
            m_x = x - int(row[0])
            m_y = row[1]
            a = []
            a.append(m_x)
            a.append(m_y)
            with open(dir3 + '/' + file, mode='a', newline='') as writer:
                e_writer = csv.writer(writer, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                e_writer.writerow(a)

files = os.listdir(dir2)

for file in files:
    x = 0
    y = 0
    with open(dir5 + '/' + file, newline='') as csvfile:
        rd = csv.reader(csvfile)
        for row in rd:
            x = int(row[0])
            y = int(row[1])

    with open(dir2 + '/' + file, newline='') as csvfile:
        rd = csv.reader(csvfile)
        for row in rd:
            m_x = x - int(row[0])
            m_y = row[1]
            a = []
            a.append(m_x)
            a.append(m_y)
            with open(dir4 + '/' + file, mode='a', newline='') as writer:
                e_writer = csv.writer(writer, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                e_writer.writerow(a)
'''
files = os.listdir(dir6)

for file in files:
    ff = file.split(".")
    flip_image(dir6+'/'+file,dir7+'/'+ff[0]+'.png')




