import turtle
import numpy as np
import os
import tempfile
import shutil
import cairosvg
import canvasvg
from stepMotionDrawing import colorChange
from motion_analysis import plot_trajectory

def drawMotion(filename,startPoint,step,timestamp = None, wifi_id = None, speed=1,delay=0,angle = 90):
    if timestamp is None:
        timestamp = ""
    if wifi_id is None:
        wifi_id = "None"

    turtle.clear() # Clear out the drawing (if any)
    turtle.reset()
    #turtle.bgpic("rshall.gif")
    turtle.bgpic("apt.gif")
    turtle.color("purple",'yellow')
    turtle.pensize(3)
    turtle.up()
    turtle.goto(100,100)
    turtle.write(timestamp)
    turtle.goto(startPoint[0],startPoint[1])
    turtle.down()
    turtle.write('s')
    #time.sleep(3)
    turtle.speed(speed)
    turtle.turtlesize(4)
    turtle.screensize(2000,2000)
    turtle.delay(delay)
    motion_squence_list = []
    orientation_list = []
    light_list = []
    acc_list = []
    step_list = []
    turtle.title(filename)
    for line in open(filename):
        if line[0] in ['O','L','S','A']:
            motion_squence_list.append(line[0])
            s_list = line.split(',')
            if line[0] == 'O':
                orientation_list.append(float(s_list[1]))
            elif line[0] == 'S':
                step_list.append(float(s_list[1]))
            elif line[0] == 'L':
                light_list.append(float(s_list[1]))
            elif line[0] == 'A':
                acc_list.append(__get_status(float(s_list[1]),float(s_list[2]),float(s_list[3])))

    x = np.array(orientation_list)
    y = np.diff(x)
    #print y
    orientation_list_diff = y.tolist()

    if len(orientation_list) > 0:
        turtle.right(orientation_list[0] - angle)
        turtle.forward(step)

    #print acc_list
    # draw
    light_list_iter = 0
    pre_i = 0
    i = 0
    i_acc = 0
    i_orientation = 0
    for ele in motion_squence_list:
        if ele == 'O':
            try:
                turtle.right(orientation_list_diff[i_orientation])
            except:
                pass
            i_orientation += 1
        elif ele == 'L':
            #turtle.color(light_list[light_list_iter])
            #turtle.color("#285078")
            tup = colorChange(light_list[light_list_iter],max(light_list))
            turtle.color(tup)
            light_list_iter = light_list_iter + 1
        elif ele == 'S':
            turtle.dot(10,'blue')
            turtle.dot((i-pre_i)/9,'red')
            turtle.forward(step)
            pre_i = i
        elif ele == 'A' and len(acc_list)>0:
            (temp_x, temp_y) = turtle.pos()
            turtle.up()
            turtle.goto(temp_x + 10 * i_acc, temp_y + 10 * i_acc)
            turtle.write(str(acc_list.pop(0)),font=("Arial", 13, "normal"))
            i_acc += 1
            turtle.goto(temp_x , temp_y)
            turtle.down()
        else:
            pass
        i += 1

    turtle.up()
    #turtle.goto(-150,-120)
    turtle.color("red")
    #turtle.write("D")
    turtle.hideturtle()
    #turtle.goto(200,200)
    turtle.color("blue")
    turtle.write(wifi_id)
    #time.sleep(6)
    return len(step_list)


"""
http://stackoverflow.com/questions/25050156/save-turtle-output-as-jpeg
"""

turtle.colormode(255)
red = 125
green = 70
blue = 38
pen = 10

def saveImg(name):
    #name = raw_input("What would you like to name it? \n")
    nameSav = name + ".pdf" # png
    tmpdir = tempfile.mkdtemp()                   # create a temporary directory
    tmpfile = os.path.join(tmpdir, 'tmp.svg')    # name of file to sa`ve SVG to
    ts = turtle.getscreen().getcanvas()
    canvasvg.saveall(tmpfile, ts)
    with open(tmpfile) as svg_input, open(nameSav, 'wb') as png_output:
        cairosvg.svg2png(bytestring=svg_input.read(), write_to=png_output)
    shutil.rmtree(tmpdir)     # clean up temp file(s)

def __get_status(xAcc, yAcc, zAcc):
    minThreshold = 3
    minminThreshold = 3
    minHight = 6
    #xy_det = abs(xAcc,yAcc)
    status = ' '
    if xAcc - yAcc > minThreshold and xAcc - zAcc > minThreshold and xAcc > minHight and abs(yAcc) < minminThreshold and abs(zAcc) < minminThreshold:
      status = 0
    if zAcc - xAcc > minThreshold and abs(yAcc) < minminThreshold and xAcc < -1 * minThreshold and zAcc > minThreshold :
      status = 5
    if xAcc - zAcc > minThreshold and abs(yAcc) < minminThreshold and xAcc < 1 * minThreshold and zAcc < -1 * minThreshold :
      status = 1
    if abs(yAcc) < minminThreshold and xAcc < -1 * minThreshold and zAcc < -1 * minThreshold :
      status = 3
    if xAcc - zAcc > minThreshold and yAcc - zAcc > minThreshold and zAcc < minHight * -1:
      status = 2
    if yAcc - xAcc > minThreshold and zAcc - xAcc > minThreshold and xAcc < minHight * -1 and (abs(yAcc) < minminThreshold or abs(zAcc) < minminThreshold):
      status = 4
    if zAcc - xAcc > minThreshold and zAcc - yAcc > minThreshold and zAcc > minHight and (abs(yAcc) < minminThreshold or abs(xAcc) < minminThreshold):
      status = 6
    if yAcc - xAcc > minThreshold and yAcc - zAcc > minThreshold and yAcc > minHight * 1:
      status = 7
    if xAcc - yAcc > minThreshold and zAcc - yAcc > minThreshold and yAcc < minHight * -1 and (abs(yAcc) < minminThreshold or abs(xAcc) < minminThreshold):
        status = 8
    return status


def draw():
    dst_book_dir = 'stepMotionPdf'
    if not os.path.exists(dst_book_dir):
        os.makedirs(dst_book_dir)
    rshall_file = r'amesHome.csv'
    rshall_file = r'd:\class\Semester5\research\light\python\LosRealProduct\dev\wifi\labelRound\amesHome\amesHome.csv'
    directory = r'E:\phil\ADLRecorder\Dataset\PhilNexus\motion\\'
    directory = r'D:\class\Semester5\research\ADLRecorder\code\Android\NexusSensors\DbRecords\AS\smh\philNexus\motion\\'
    prefix = 'PhilNexus_'
    suffix = '_motion.csv'
    timestamp = ''
    filename = 'PhilNexus_20161018_191716.csv'
    archor = filename[filename.index('_')+1: filename.index('.')]
    archor = '20160730_110646'
    archor = '0'
    for line in open(rshall_file):
        line_list = line.split(',')
        timestamp = line_list[0]
        wifi_id = line_list[5]
        filename = directory + prefix + timestamp + suffix
        if timestamp > archor:
            #filename_list = os.path.basename(filename).split('_')
            #timestamp = filename_list[1]+'_'+filename_list[2]
            step_count = drawMotion(filename,(0,0),15,timestamp, wifi_id)
            #saveImg(dst_book_dir+'/'+wifi_id.replace('\n','')+'_'+timestamp)
            if step_count > 4:
                saveImg(dst_book_dir+'/'+timestamp+'_'+wifi_id.replace('\n',''))
                plot_trajectory(directory, timestamp, '_s_'+str(step_count))

if __name__ == '__main__':
    draw()
