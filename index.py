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
            if (int(num_01) - int(num_02) < 0):
                pound = 0
            else:
                pound = (int(num_01) - int(num_02)) / 2
            arr[lin][col] = pound
            # print("\n" + str(num_01) + " <e> " + str(num_02) + " <pound> " + str(pound))
        # print("---------- end of line -----------------")
    return arr


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

print("\nEnd of processing... ")
