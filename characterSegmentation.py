'''
* Returns a list of images of the characters in the given image.
*
* @param  img  a grey scale image with intensties from 0 to 1
* @return      a list of images of the characters in the given image
'''
def characterSegmentation(img):
    imgBinary = cv2.threshold(np.uint8(img * 255), 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    componentsCount, _, statistics, _ = cv2.connectedComponentsWithStats(imgBinary, 8, cv2.CV_32S)
    characters = []
    for i in range(2, componentsCount):
        x = statistics[i, cv2.CC_STAT_LEFT]
        y = statistics[i, cv2.CC_STAT_TOP]
        w = statistics[i, cv2.CC_STAT_WIDTH]
        h = statistics[i, cv2.CC_STAT_HEIGHT]
        characters.append(imgBinary[y : y + h, x : x + w])
    return characters