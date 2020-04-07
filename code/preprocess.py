import os
import glob

def load_images():

	base_dir = os.getcwd()
	img_dir = base_dir + '/train/images'
	os.chdir(img_dir)
	pre_disaster = sorted(glob.glob('*pre_disaster.png'))
	post_disaster = sorted(glob.glob('*post_disaster.png'))
	os.chdir(base_dir)

	return pre_disaster, post_disaster

def load_labels():

	base_dir = os.getcwd()
	label_dir = base_dir + '/train/labels'
	os.chdir(label_dir)
	pre_disaster = sorted(glob.glob('*pre_disaster.json'))
	post_disaster = sorted(glob.glob('*post_disaster.json'))
	os.chdir(base_dir)

	return pre_disaster, post_disaster


def load_data():

	pre_x, post_x = load_images()
	pre_y, post_y = load_labels()
	pre_dictionary = {}
	post_dictionary = {}

	for img,label in zip(pre_x,pre_y):
		pre_dictionary[img] = label

	for img,label in zip(post_x,post_y):
		post_dictionary[img] = label

	return pre_dictionary, post_dictionary


