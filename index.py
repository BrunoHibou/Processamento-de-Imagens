import numpy as np
from PIL import Image
import matplotlib.image as mpimg


def image_to_grey(path_name_image_01, name_image_02):
    img = Image.open(path_name_image_01)
    img_gray = img.convert('L')
    img_gray.save(name_image_02)
    return 0


def image_to_array(name_image_02):
    img = mpimg.imread(name_image_02)
    arr = np.array(img)
    return arr



# Sum
def sum_and_ponder_array(arr_01, arr_02, lines_columns):
    arr = arr_01

    for col in range(0, lines_columns):
        for lin in range(0, lines_columns):
            # np.seterr(over='ignore')
            num_01 = arr_01[lin][col]
            num_02 = arr_02[lin][col]
            pound = (int(num_01) + int(num_02)) / 2
            arr[lin][col] = pound
            # print("\n" + str(num_01) + " <e> " + str(num_02) + " <pound> " + str(pound))
        # print("---------- end of line -----------------")
    return arr


# Subtraction
def sub_and_ponder_array(arr_01, arr_02, lines_columns):
    arr = arr_01
    for col in range(0, lines_columns):
        for lin in range(0, lines_columns):
            num_01 = arr_01[lin][col]
            num_02 = arr_02[lin][col]
            if int(num_01) - int(num_02) < 0:
                pound = 0
            else:
                pound = (int(num_01) - int(num_02)) / 2
            arr[lin][col] = pound
            # print("\n" + str(num_01) + " <e> " + str(num_02) + " <pound> " + str(pound))
        # print("---------- end of line -----------------")
    return arr

# rotation

def image_rotation_identity(rotate_degree, lines_columns):

    theta = np.radians(rotate_degree)
    c, s = np.cos(theta), np.sin(theta)
    a = np.array(((c, -s), (s, c)))
    
    identity = np.identity(lines_columns)
    identity[0][0] = c
    identity[0][1] = -s
    identity[1][0] = s
    identity[1][1] = c

    return identity.astype(int)

def image_rotation(arr_image, arr_identity):

    return arr_identity.dot(arr_image)


# Neighborhood

def NN_interpolation(img, height, width):
    screen_h, screen_w = img.shape
    new_arr = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(height - 1):
        for j in range(width - 1):
            scrx = round(i * (screen_h / height))
            scry = round(j * (screen_w / width))
            new_arr[i, j] = img[scrx, scry]
    return new_arr

# Variables
first_image_path_name_image_01 = './first_small_img_test_10_10.jpg'
first_image_name_image_02 = 'first_small_img_test-01.jpg'

second_image_path_name_image_01 = './second_small_img_test_10_10.jpg'
second_image_name_image_02 = 'second_small_img_test-01.jpg'

print("\nStarting.... \n")

# Parsing the first image to Array
image_to_grey(first_image_path_name_image_01, first_image_name_image_02)
print(image_to_array(first_image_name_image_02))

print("\n\n---------------------------------------------------------------------------------\n\n")

# Parsing the second image to Array
image_to_grey(second_image_path_name_image_01, second_image_name_image_02)
print(image_to_array(second_image_name_image_02))

# Calling Array transform function
print("\n--------------New matrix image---------------------\n")
# Calling function Sum
arr = sum_and_ponder_array(image_to_array(first_image_name_image_02), image_to_array(second_image_name_image_02), 10)
# Calling function Subtraction
arr2 = sub_and_ponder_array(image_to_array(first_image_name_image_02), image_to_array(second_image_name_image_02), 10)

# Save the result of the new image on the root of project
Image.fromarray(arr).save('./new-converted-image-01.jpg')
Image.fromarray(arr2).save('./new-converted-image-02.jpg')


im_path = './first_small_img_test_10_10.jpg'
image = np.array(Image.open(im_path))

image1 = NN_interpolation(image, image.shape[0] * 2, image.shape[1] * 2)
image1 = Image.fromarray(image1.astype('uint8'))
image1.save('./first_small_img_test_10_10_out.jpg.jpg')


# rotation of 180 degrees

identity = image_rotation_identity(180, 10)
second_image = image_to_array('./first_small_img_test_10_10.jpg')
second_image = second_image.astype(int)
arr_rotate_result = image_rotation(second_image, identity)
arr_rotate_result = arr_rotate_result

print("\n------------------- Rotate Image -----------------------------\n\n")

print(arr_rotate_result)

# Create a new image after rotation process
Image.fromarray(arr_rotate_result.astype('uint8')).save('./new-rotated-image-01.jpg')


print("\nEnd of processing... ")


