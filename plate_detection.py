#returns the plate of the car
def Plate_detection(car_img,car_gray,car_edge):
    car_c = binary_dilation(car_edge)
    car_c = binary_erosion(car_c)
    countours = np.asarray( find_contours(car_c ,level = 0.8,fully_connected='high'))
    bounding_boxes = []

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            location = approx
            break
    mask = np.zeros(car_gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [location], 0,255, -1)
    new_image = cv2.bitwise_and(car_img, car_img, mask=mask)
