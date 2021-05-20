from PIL import Image
import numpy as np



# Nearest Neighbor Interpolation Algorithm
# dstH is the height of the new image; dstW is the width of the new image
def NN_interpolation(img, altura_final, largura_final):
    altura = img.shape[1]
    largura = img.shape[0]
    img2 = np.zeros((altura_final, largura_final, 3), dtype=np.uint8)
    for p in range(altura_final - 1):
        for q in range(largura_final - 1):
            x = round(p * (altura / altura_final))
            y = round(q * (largura / largura_final))
            img2[p, q] = img[x, y]
    return img2


im_path = './first_small_img_test-01.jpg'
image = np.array(Image.open(im_path))
altura_inicial = image.shape[1]
largura_inicial = image.shape[0]
image1 = NN_interpolation(image, largura_inicial * 3, altura_inicial * 3)
image1 = Image.fromarray(image1.astype('uint8')).convert('RGB')
image1.save('out.png')