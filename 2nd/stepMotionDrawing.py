import turtle
import time
import numpy as np
import math
import threading
import thread
import pdb


'''
def colorChange1(actual_light_level, max_light):
    #light_color_base = 1
    x1 = x2 = x3 = 0
    x = 1.0 * actual_light_level/ max_light
    if x < 0.33 :
        x1 = x+0.66
        x2 = x3 = 0
    elif x >= 0.33 and x < 0.67:
        x2 = x+0.33
        x1 = x3 = 0
    else:
        x3 = x
        x1 = x2 = 0

    res_light_color = (x1, x2, x3)
    return res_light_color

def colorChange2(actual_light_level, max_light):
    x = int(27 * actual_light_level/ max_light)
    print x
    x1 =x2 = x3 = 0

    if x >= 18:
        x3 = float(x-18) / 9
        x2 = 1
        x1 = 1
    elif x < 18 and x>= 9:
        x2 = float(x-9) / 9
        x1 = 1
    elif x < 9:
        x1 = float(x)/9

    (aa,temp) = divmod(x , 16)
    (aa,temp) = divmod(temp , 8)
    x3 = float(temp/8)

    res_light_color = (x1, x2, x3)
    print res_light_color
    return res_light_color
'''

def colorChange(actual_light_level, max_light):
    x = 1000 *float( actual_light_level/ max_light)
    x1 =x2 = x3 = 0

    if x >= 100:
        x3 = math.log(x) / 9
        x2 = 1
        x1 = 1
        if x3>1: x3 = 1
    elif x < 100 and x >= 10:
        x2 = math.log(x) / 4
        x1 = 1
        if x2>1: x2 = 1
    elif x < 10 and x > 0:
        x3 = 0.5
        x2 = 0.5
        x1 = math.log(x) / 3
        if x1>1: x1 = 1
    elif x == 0:
        x3=x2=x1 = 0.1

    if x1 < 0 : x1 = 0
    if x2 < 0 : x2 = 0
    if x3 < 0 : x3 = 0


    res_light_color = (x1, x2, x3)
    #print res_light_color
    return res_light_color


def drawMotion(filename,startPoint,step,speed=1,delay=10):
    turtle.bgpic("apt1.gif")
    turtle.color("purple",'yellow')
    turtle.pensize(3)
    turtle.goto(startPoint[0],startPoint[1])
    time.sleep(11)
    turtle.speed(speed)
    turtle.turtlesize(4)
    turtle.screensize(1300,1400)
    turtle.delay(delay)
    motion_squence_list = []
    orientation_list = []
    light_list = []
    step_list = []
    turtle.title(filename)
    for line in open(filename):
        if line[0] in ['O','L','S'] and line[1] == ':':
            motion_squence_list.append(line[0])
            s_list = line.split(',')
            if line[0] == 'O':
                orientation_list.append(float(s_list[1]))
            if line[0] == 'S':
                step_list.append(float(s_list[1]))
            if line[0] == 'L':
                light_list.append(float(s_list[1]))

    x = np.array(orientation_list)
    y = np.diff(x)
    #print y
    orientation_list_diff = y.tolist()

    turtle.right(orientation_list[0]-180)
    turtle.forward(step)

    light_list_iter = 0
    pre_i = 0
    for i, j in enumerate(orientation_list_diff):
        turtle.right(j)

        if motion_squence_list[i] == 'L':
            #turtle.color(light_list[light_list_iter])
            #turtle.color("#285078")
            tup = colorChange(light_list[light_list_iter],max(light_list))
            turtle.color(tup)
            light_list_iter = light_list_iter + 1
        elif motion_squence_list[i] == 'S':
            turtle.dot(10,'blue')
            turtle.dot((i-pre_i)/2,'red')
            turtle.forward(step)
            pre_i = i
        else:
            pass


    turtle.up()
    #turtle.goto(-150,-120)
    turtle.color("red")
    turtle.write("Done")
    time.sleep(3)

def drawMotionFromASfile(filename,startPoint,step,speed=1,delay=10,ending = 7):
    turtle.bgpic("apt.gif")
    turtle.color("purple",'yellow')
    turtle.pensize(3)
    turtle.goto(startPoint[0],startPoint[1])
    time.sleep(3)
    turtle.speed(speed)
    turtle.turtlesize(4)
    turtle.screensize(1500,1700)
    turtle.delay(delay)
    orientation_list = []
    light_list = []
    step_list = []
    turtle.title(filename)
    startingLineNum = 10
    iterStarting = 0
    for line in open(filename):
        if iterStarting > startingLineNum and 'yunfei' in line and 'Debugger' not in line and 'expire' not in line:
            s_list = line.split(',')
            step_list.append(float(s_list[-1]))
            light_list.append(float(s_list[1]))
            orientation_list.append(float(s_list[5]))
        else:
            iterStarting = iterStarting + 1

    x = np.array(orientation_list)

    y = np.diff(x)
    orientation_list_diff = y.tolist()

    turtle.right(orientation_list[0]-90)
    turtle.forward(step)

    radi = 0
    for i, j in enumerate(orientation_list_diff):
        turtle.right(j)
        turtle.delay(delay)
        tup = colorChange(light_list[i],max(light_list))
        turtle.color(tup)
        if step_list[i] > step_list [i-1]:
            turtle.dot(radi/20, "blue")
            turtle.dot(10)
            turtle.stamp()
            turtle.forward(step)
            radi = 0
        elif step_list[i] == step_list [i-1]:
            radi = radi + 1

    #turtle.goto(-150,-120)
    turtle.goto(startPoint[0],startPoint[1])
    turtle.up()
    turtle.color("purple")
    turtle.write("Done")
    time.sleep(ending)


def drawMotionFromLightRecordData(filename,startPoint,step,speed=1,delay=10,ending = 7):
    turtle.bgpic("apt.gif")
    turtle.color("purple",'yellow')
    turtle.pensize(3)
    turtle.goto(startPoint[0],startPoint[1])
    time.sleep(3)
    turtle.speed(speed)
    turtle.turtlesize(4)
    turtle.screensize(1500,1700)
    turtle.delay(delay)

    orientation_list = []
    light_list = []
    step_list = []
    zAccer_list = []

    turtle.title(filename)
    lineIter = 0
    for line in open(filename):
        if lineIter > 7 and line != "" :
            s_list = line.split(',')
            if len(s_list) > 10:
                step_list.append(float(s_list[-1].replace('\n','')))
                light_list.append(float(s_list[1]))
                if (float(s_list[9])>= 0 ):
                    orientation_list.append(float(s_list[4]))
                elif (float(s_list[9])< 0 ):
                    orientation_list.append(-1.0 * float(s_list[4]))
                zAccer_list.append(float(s_list[9]))
        lineIter = lineIter + 1;

    x = np.array(orientation_list)

    y = np.diff(x)
    orientation_list_diff = y.tolist()

    turtle.right(orientation_list[0]-90)

    turtle.forward(step)

    radi = 0
    for i, j in enumerate(orientation_list_diff):
        turtle.right(j)
        turtle.delay(delay)
        tup = colorChange(light_list[i],max(light_list))
        turtle.color(tup,'red')
        if step_list[i] > step_list [i-1]:
            turtle.dot(radi/20, "blue")
            turtle.dot(10)
            turtle.stamp()
            turtle.forward(step * (step_list[i]-step_list[i-1]))
            radi = 0
        elif step_list[i] == step_list [i-1]:
            radi = radi + 1

    _x,_y = turtle.pos()[0:2]
    turtle.goto((_x+startPoint[0])*0.66,(_y+startPoint[1])*0.66)
    time.sleep(2)
    turtle.goto((_x+startPoint[0])*0.33,(_y+startPoint[1])*0.33)
    time.sleep(2)
    turtle.goto(startPoint[0],startPoint[1])
    turtle.up()
    #turtle.goto(-150,-120)
    time.sleep(2)
    turtle.color("purple")
    turtle.write("Done")
    time.sleep(ending)

def testCase(case=0):
    if case == 0 :
        filename = 'Phil_20160402_015844.csv'
        startPoint = (0,-335)
        step = 50
        drawMotion(filename,startPoint,step,1,5)
    if case == 1 :
        filename = r'c:/Users/Yunfei/Downloads/received/Phil_20160402_135327_motion.csv'
        startPoint = (300,-100)
        step = 5
        drawMotion(filename,startPoint,step)
    if case == 2 :
        filename = r'allIn1.csv'
        startPoint = (300,-100)
        step = 5
        drawMotion(filename,startPoint,step,1,0)
    if case == 3 :
        filename = r'allIn2.csv'
        startPoint = (0,-270)
        step = 5
        drawMotion(filename,startPoint,step,1,0)
    if case == 4 :
        filename = r'allIn3.csv'
        startPoint = (0,-270)
        step = 5
        drawMotion(filename,startPoint,step,1,0)
    if case == 5 :
        filename = r'allIn4.csv'
        startPoint = (0,-270)
        step = 5
        drawMotion(filename,startPoint,step,1,0)
    if case == 6 :
        filename = r'allIn5.csv'
        startPoint = (0,-270)
        step = 5
        drawMotion(filename,startPoint,step,1,0)
    if case == 7 :
        filename = r'd:/class/Semester5/research/light/lightAS/output1/ChicagoBasement.csv'
        startPoint = (0,-110)
        step = 50
        drawMotionFromASfile(filename,startPoint,step,0,0.2,3)
    if case == 8 :
        filename = r'd:/class/Semester5/research/light/lightAS/output1/ChicagoRoute1.csv'
        startPoint = (100,110)
        step = 30
        drawMotionFromASfile(filename,startPoint,step,1,0.5,10)
    if case == 9 :
        filename = r'd:/class/Semester5/research/light/lightAS/output1/AmesTestLuminaryAngle1.csv'
        startPoint = (100,110)
        step = 30
        drawMotionFromASfile(filename,startPoint,step,1,0.53,10)
    if case == 10 :
        #filename = r'd:\class\Semester5\research\ADLRecorder\code\AdlDemo\losHtml\step.log'
        filename = r'step.log'
        startPoint = (100,110)
        step = 8
        drawMotionFromLightRecordData(filename,startPoint,step,1,0.53,1)


'''
def generateJsonFile(interval = 10, filename = "Phil_20160402_015844.csv" ):
    #filename = r'allIn2.csv'
    for line in open(filename):
        f_json = open (r'asr\allIn1.json','w')
        f_json.write(line)
        f_json.close()
        time.sleep(1.0 * interval / 100)
'''

if __name__ == '__main__':
    #testCase(0)
    #testCase(7)
    testCase(10)

    #generateJsonFile(10)
    '''
    thread.Thread(testCase, (0,))
    thread.start_new_thread(generateJsonFile, (10,))
    threads = []
    t1 = threading.Thread(target=testCase,args=(0,))
    threads.append(t1)
    t2 = threading.Thread(target=generateJsonFile,args=(10,))
    threads.append(t2)
    for t in threads:
        t.setDaemon(True)
        t.start()
    '''


    ''' trash
    if line[0] == 'L' and line[1] == '-':
        light_list_str = line.split(',')[1:-1]
        for e in light_list_str:
            light_list.append(float(e))

    if line[0] == 'S' and line[1] == '-':
        step_list = line.split(',')[1:-1]
    if line[0] == 'O' and line[1] == '-':
        orientation_list_str = line.split(',')[1:-1]
        for e in orientation_list_str:
                orientation_list.append(float(e))
    '''



