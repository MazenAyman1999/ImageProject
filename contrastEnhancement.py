'''
* Returns the given image after contrast enhancement.
*
* @param  img  a grey scale image with intensties from 0 to 1
* @return      the given image after contrast enhancement
'''
def contrastEnhancement(img):
    cov = np.std(img) / np.mean(img)
    if (cov < 0.5):
        imgEnhanced = exposure.equalize_hist(img)
    else:
        gamma = np.log(np.mean(img)) / np.log(0.5)
        imgEnhanced = exposure.adjust_gamma(img, gamma)
    return imgEnhanced