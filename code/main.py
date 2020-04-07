import os
import cv2
import numpy as np
from preprocess import load_data
from utils import parse_pre_json, parse_post_json
import matplotlib.pyplot as plt
from scipy.misc import imread #system must have scipy version:1.1.0 not latest version, higher version has issue with imread module


def create_pre_mask(polygons, img_size):

    img_mask = np.zeros(img_size, np.uint8)

    int_coords = lambda x: np.array(x).round().astype(np.int32) # fn to convert coordinates to int
    exteriors = [int_coords(poly.exterior.coords) for poly in polygons]
    interiors = [int_coords(pi.coords) for poly in polygons 
                for pi in poly.interiors]
    
    cv2.fillPoly(img_mask, exteriors, 1)
    cv2.fillPoly(img_mask, interiors, 0)
    
    return img_mask

def create_post_mask(polygons, img_mask, damage_level):

    int_coords = lambda x: np.array(x).round().astype(np.int32) # fn to convert coordinates to int
    exteriors = [int_coords(poly.exterior.coords) for poly in polygons]
    interiors = [int_coords(pi.coords) for poly in polygons 
                for pi in poly.interiors]
    #color to represent damage level: RED, BLUE, YELLOW, PINK
    labels = {'destroyed': (255,0,0), 'major-damage': (0,0,255), 'minor-damage': (255,255,0), 'no-damage': (255,192,203)}
    
    for i in range(len(exteriors)):
        cv2.fillPoly(img_mask, [exteriors[i]], labels[damage_level[i]])
    
    return img_mask
        
if __name__ == '__main__':

    base_dir = os.getcwd()
    pre_disaster , post_disaster = load_data()

    for image in pre_disaster:

        img = cv2.imread(base_dir + '/train/images/' + image)
        img_size = img.shape[:2]

        label = pre_disaster[image]
        json_file =  base_dir+ '/train/labels/' + label
        
        multipolygon = parse_pre_json(json_file)
        mask = create_pre_mask(multipolygon, img_size)

        plt.imsave(base_dir+'/masks/'+ image, mask, cmap = 'gray')
        
    for image in post_disaster:

        img = imread(base_dir + '/train/images/' + image, 0)

        label = post_disaster[image]
        json_file =  base_dir+ '/train/labels/' + label
        
        multipolygon , damage_level = parse_post_json(json_file)
        mask = create_post_mask(multipolygon, img, damage_level)

        plt.imsave(base_dir+'/masks/'+ image, mask)

