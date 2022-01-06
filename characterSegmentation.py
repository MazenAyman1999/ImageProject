'''
* Returns the given image with characters segmented.
*
* @param  img     a grey scale image with intensties from 0 to 1
* @param  method  method of character segmentation ("connectedComponents" or "blackHatMorphology")
* @return         the given image with characters segmented
'''
def characterSegmentation(img, method):
    if (method == "connectedComponents"):
        imgBinary = cv2.threshold(np.uint8(img * 255), 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        componentsCount, labels, _, _ = cv2.connectedComponentsWithStats(imgBinary, 8, cv2.CV_32S)
        characters = np.zeros(img.shape, dtype="uint8")
        for i in range(2, componentsCount):
            componentMask = np.uint8((labels == i) * 255)
            characters = cv2.bitwise_or(characters, componentMask)
    elif (method == "blackHatMorphology"):
        seBlackHat = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 13))
        characters = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, seBlackHat)
    else:
        characters = img.copy()
    return characters