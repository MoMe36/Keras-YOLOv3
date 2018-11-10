from PIL import Image 
import numpy as np 
import matplotlib.pyplot as plt

# image = './../melo_dataset/5.jpg'
# image = Image.open(image)

# np_im = np.array(image)
# magn = np.array([70,70])
# bounds = np.array([[236,675],[407,605]])

def extract_patch(image, boundaries, padding_magn, char_height = 130, image_size = 224):


	np_im = np.array(image)
	padding_magn = np.array([70,70])
	padding = np.tile(np.array([-1,1]), [2,1])
	padding = padding*padding_magn.reshape(-1,1)

	boundaries = np.clip(boundaries + padding, 0, np_im.shape[:2])


	sub_im = np_im[boundaries[0][0]:boundaries[0][1],boundaries[1][0]:boundaries[1][1],:]
	dims = sub_im.shape
	ind_max = np.argmax(dims)
	ind_min = 1 if ind_max == 0 else 0

	max_dims = sub_im.shape[ind_max]

	center_min = int(sub_im.shape[ind_max]/2.)
	half = int(sub_im.shape[ind_min]/2)
	add_one = 1 if sub_im.shape[ind_min] % 2 != 0 else 0 
	
	sub_boundaries = [center_min - half, center_min + half + add_one]

	full_matrix = np.zeros((max_dims, max_dims, 3)).astype(int)
	full_matrix[:,sub_boundaries[0]:sub_boundaries[1], :] = sub_im

	new_image = Image.fromarray(full_matrix.astype(np.uint8), 'RGB')
	new_image = new_image.resize([image_size, image_size])
	new_image.show()

	return new_image