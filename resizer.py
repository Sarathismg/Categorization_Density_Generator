import cv2
import os

import numpy as np
import scipy.io

FIXED_WID = 256
FIXED_HEIGHT = 256

IMAGE_LOCATION = 'data_1/Images/'
ANNOTATION_LOCATION_1 = 'data_1/Sitting/'
ANNOTATION_LOCATION_2 = 'data_1/Standing/'

OUTPUT_IMAGE_LOCATION = 'data_1/Resized/Images/'
OUTPUT_ANNOTATION_LOCATION_1 = 'data_1/Resized/Sitting/'
OUTPUT_ANNOTATION_LOCATION_2 = 'data_1/Resized/Standing/'


filelist = os.listdir(IMAGE_LOCATION)

for k in filelist:
    print(k)
    imagel = IMAGE_LOCATION+'/'+k
    image = cv2.imread(imagel)
    h,w,d = image.shape
    dim = (FIXED_HEIGHT, FIXED_WID)
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    cv2.imwrite(OUTPUT_IMAGE_LOCATION+'/'+k, resized)
    mat_1 = mat_2 = None
    #mat = scipy.io.loadmat(ANNOTATION_LOCATION+'/GT_'+k[: -4]+'.mat')['image_info'][0][0][0][0][0]
    if os.path.isfile(ANNOTATION_LOCATION_1+k[0: -4]+".csv"):
        mat_1 = np.loadtxt(ANNOTATION_LOCATION_1+k[0: -4]+".csv", dtype='int', delimiter=',', ndmin=2)
        mat_1[:, 0] = mat_1[:, 0] * (FIXED_WID / w)
        mat_1[:, 1] = mat_1[:, 1] * (FIXED_HEIGHT / h)
        np.savetxt(OUTPUT_ANNOTATION_LOCATION_1 + '/' + k[0: -4] + '.csv', mat_1, delimiter=',')
    if os.path.isfile(ANNOTATION_LOCATION_2 + k[0: -4] + ".csv"):
        mat_2 = np.loadtxt(ANNOTATION_LOCATION_2+k[0: -4]+".csv", dtype='int', delimiter=',', ndmin = 2)
        mat_2[:, 0] = mat_2[:, 0] * (FIXED_WID / w)
        mat_2[:, 1] = mat_2[:, 1] * (FIXED_HEIGHT / h)
        np.savetxt(OUTPUT_ANNOTATION_LOCATION_2 + '/' + k[0: -4] + '.csv', mat_2, delimiter=',')
