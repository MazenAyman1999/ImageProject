'''
* Returns the plate number.
*
* @param  original img and grey scale image with intensties from 0 to 1 and image with edges
* @return      the plate number of a car
'''
def Plate_detection(car_edge,car_gray):
        
    arr = np.uint8(car_edge)
    contours = cv.findContours(arr.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    contours = sorted(contours, key=cv.contourArea, reverse=True)[:10]
    location = None
    for contour in contours:
        approx = cv.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            location = approx
            break
    Xmin = np.inf
    Xmax = 0
    Ymin = np.inf
    Ymax = 0
    for i in range(len(location)):
        point = location[i]
        if(point[0][0] > Xmax):
            Xmax = point[0][0]
        if(point[0][0] < Xmin):
            Xmin = point[0][0]
        if(point[0][1] > Ymax):
            Ymax = point[0][1]
        if(point[0][1] < Ymin):
            Ymin = point[0][1]
    return car_gray[Ymin:Ymax,Xmin:Xmax]
