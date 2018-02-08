import cv2
import line_detection as l
from vector import distance,pnt2line
import numpy as np
import time
import neural_network_predict as nnp
from scipy import ndimage

cc=-1
def nextId():
    global cc
    cc += 1
    return cc

def inRange(r, item, items):
    retVal = []
    for obj in items:
        mdist = distance(item['center'], obj['center'])
        if (mdist < r):
            retVal.append(obj)
    return retVal

def predict(img):
    # denoised = cv2.fastNlMeansDenoisingColored(
    #     img, h=18,hColor=25, searchWindowSize=21, templateWindowSize=7)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('a',gray)
    #cv2.waitKey(10000)
    ret, thresh1 = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY)
    #cv2.imshow('a', thresh1)
    #cv2.waitKey(10000)
    im2, contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if(not contours):
        return -1
    c = max(contours, key=cv2.contourArea)

    x, y, w, h = cv2.boundingRect(c)
    rect = thresh1[y:y + h, x:x + w]

    final = cv2.resize(rect, (28, 28), interpolation=cv2.INTER_NEAREST)

    val = nnp.predict(final)

    return val

def resenje(path):

    cap = cv2.VideoCapture(path)

    ret, firstFrame = cap.read()
    blueLine = l.get_blue(firstFrame)
    greenLine = l.get_green(firstFrame)

    kernel = np.ones((2,2),np.uint8)
    lower = np.array([230, 230, 230])
    upper = np.array([255, 255, 255])

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('images/output-rezB.avi',fourcc, 20.0, (640,480))

    elements = []
    t =0
    counter = 0
    times = []

    while 1:
        start_time = time.time()
        ret, img = cap.read()

        if ret == False:
            break

        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        mask = cv2.inRange(img, lower, upper)
        img0 = 1.0 * mask

        img0 = cv2.dilate(img0, kernel)  # cv2.erode(img0,kernel)
        img0 = cv2.dilate(img0, kernel)

        labeled, nr_objects = ndimage.label(img0)
        objects = ndimage.find_objects(labeled)

        for i in range(nr_objects):
            loc = objects[i]
            (xc, yc) = ((loc[1].stop + loc[1].start) / 2,
                        (loc[0].stop + loc[0].start) / 2)
            (dxc, dyc) = ((loc[1].stop - loc[1].start),
                          (loc[0].stop - loc[0].start))

            (xc, yc) = (int(xc),int(yc))
            (dxc, dyc) = (int(dxc), int(dyc))

            cv2.circle(img, (xc, yc), 16, (25, 25, 255), 1)

            if (dxc > 11 or dyc > 11):
                cv2.circle(img, (xc, yc), 16, (25, 25, 255), 1)
                elem = {'center': (xc, yc), 'size': (dxc, dyc), 't': t}
                # find in range
                lst = inRange(18, elem, elements)
                nn = len(lst)
                (x, y) = (loc[1].start, loc[0].start)
                if nn == 0:
                    elem['id'] = nextId()
                    elem['t'] = t
                    elem['bluePass'] = False
                    elem['greenPass'] = False
                    pred = predict(img[y: y + dyc, x: x + dxc])
                    elem['history'] = [{'center': (xc, yc), 'size': (dxc, dyc), 't': t, 'val': pred}]
                    elem['value'] = pred
                    elements.append(elem)
                elif nn == 1:
                    if (t % 10 == 0):
                        pred = predict(img[y: y + dyc, x: x + dxc])
                    else:
                        pred = -1
                    lst[0]['value'] = pred
                    lst[0]['center'] = elem['center']
                    lst[0]['t'] = t
                    lst[0]['history'].append({'center': (xc, yc), 'size': (dxc, dyc), 't': t,'val': pred})
                    lst[0]['future'] = []


        for el in elements:
            tt = t - el['t']
            if (tt < 3):
                dist, pnt, r = pnt2line(el['center'], blueLine[0], blueLine[1])
                c = (25, 25, 255)
                if r > 0:
                    cv2.line(img, pnt, el['center'], (0, 255, 25), 1)
                    if (dist < 14):
                        c = (0, 255, 160)
                        if el['bluePass'] == False:
                            el['bluePass'] = True
                            valueHistory = [a['val'] for a in el['history']]
                            history = [a[0] for a in valueHistory if a != -1]
                            val = np.argmax(np.bincount(history))
                            counter += val

                dist, pnt, r = pnt2line(el['center'], greenLine[1], greenLine[0])
                c = (25, 25, 255)
                if r > 0:
                    cv2.line(img, pnt, el['center'], (0, 255, 25), 1)
                    if (dist < 14):
                        c = (0, 255, 160)
                        if el['greenPass'] == False:
                            el['greenPass'] = True
                            valueHistory = [a['val'] for a in el['history']]
                            history = [a[0] for a in valueHistory if a != -1]
                            val = np.argmax(np.bincount(history))
                            counter -= val
                            print('-' + str(val))

                cv2.circle(img, el['center'], 16, c, 2)

                id = el['id']
                cv2.putText(img, str(el['id']),
                            (el['center'][0] + 10, el['center'][1] + 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, 255)
                # for hist in el['history']:
                #     ttt = t - hist['t']
                #     if (ttt < 100):
                #         cv2.circle(img, hist['center'], 1, (0, 255, 255), 1)


        elapsed_time = time.time() - start_time
        times.append(elapsed_time * 1000)
        cv2.putText(img, 'Counter: ' + str(counter), (400, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (90, 90, 255), 2)

        # print nr_objects
        t += 1
        if t % 10 == 0:
            print
            t
        # cv2.imshow('frame', img)
        # k = cv2.waitKey(30) & 0xff
        # if k == 27:
        #    break
        # out.write(img)
    out.release()
    cap.release()
    cv2.destroyAllWindows()

    # for el in elements:
    #     valueHistory = [a['val'] for a in el['history']]
    #     history = [a[0] for a in valueHistory if a != -1]
    #     val = np.argmax(np.bincount(history))
    #     if el['greenPass'] == True:
    #         counter -= val
    #         print('-' + str(val))
    #     if el['bluePass'] == True:
    #         counter += val
    #         print('-' + str(val))
    print(counter)
    et = np.array(times)
    return counter

