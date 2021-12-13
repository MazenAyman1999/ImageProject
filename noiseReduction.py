'''
* Returns the given image filtered from noise.
*
* @param  img  a grey scale image with intensties from 0 to 1
* @return      the given image filtered from noise
'''
def noiseReduction(img):
    imgBrightness = np.mean(img)
    sigma = 1 / (2 * imgBrightness)
    imgFiltered = gaussian(img, sigma)
    return imgFiltered