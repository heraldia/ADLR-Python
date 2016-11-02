import glob
import os
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 10

offset = 0
def motionData2Timeline(dirFi, nameIndex = None, startingDate = None, endingDate = None):
    if nameIndex is None:
        nameIndex = -2
    outputFileName = dirFi.split('/')[nameIndex]+'_motion_timeline.csv'
    if endingDate is None:
        endingDate = 'a'
    if startingDate is None:
        startingDate = '0'

    output_file = open(outputFileName, 'w')
    """
    header = [dateTime,date,Time,step,xAcc,yAcc,zAcc,azimuth,pitch,roll,light,
            pressure,latitude,longitude,altitude,batteryCharging,batteryPercent,
            screenOn,earplug,screenOrientation,diffStep]
    """
    output_file.write('dateTime,date,Time,step,xAcc,yAcc,zAcc,azimuth,pitch,roll,light,'+
            'pressure,latitude,longitude,altitude,batteryCharging,batteryPercent,'+
            'screenOn,earplug,screenOrientation,diffStep\n')
    __i_file = 0
    for ele_file in glob.glob(dirFi+'\motion\*_motion.csv'):
        timeInFile = filter(str.isdigit, os.path.basename(ele_file))
        if timeInFile > startingDate and timeInFile <= endingDate:

            date,time = os.path.basename(ele_file).split('_')[1:3]
            ele_motion = ['0']*(19+offset)
            #print float(time)
            i = 0
            for ele_line in open(ele_file):
                s_ele_line = ele_line.split(',')
                if s_ele_line[0].lower() == 's':
                    if __i_file == 0:
                        __previous_step = s_ele_line[1]
                        __i_file += 1
                    ele_motion[1+offset] = s_ele_line[1]
                    ele_motion[18+offset] = __compare_positive(float(s_ele_line[1]) - float(__previous_step),0)
                    __previous_step = s_ele_line[1]
                elif s_ele_line[0].lower() == 'a':
                    ele_motion[2+offset] = s_ele_line[1]
                    ele_motion[3+offset] = s_ele_line[2]
                    ele_motion[4+offset] = s_ele_line[3]
                elif s_ele_line[0].lower() == 'o':
                    ele_motion[5+offset] = s_ele_line[1]
                    ele_motion[6+offset] = s_ele_line[2]
                    ele_motion[7+offset] = s_ele_line[3]
                elif s_ele_line[0].lower() == 'l':
                    ele_motion[8+offset] = s_ele_line[1]

                if not '0' in ele_motion[2+offset : 7+offset]:
                    _time,_carry_date = __updateTime2(time,i)
                    ele_motion[0] =  __dateFormat(date, _carry_date) + ' ' + _time + ',' + __dateFormat(date, _carry_date) + ',' + _time
                    output_file.write(','.join(ele_motion)+'\n')
                i += 1
    output_file.close()

def motionData2Timeline_indoor(dirFi, nameIndex = None, startingDate = None, endingDate = None):
    '''
    2016-10-15 23:52:18
    '''
    if nameIndex is None:
        nameIndex = -2

    if startingDate is None:
        startingDate = '0'
    if endingDate is None:
        endingDate = 'a'

    outputFileName = dirFi.split('/')[nameIndex]+'_indoor_motion_%s_%s.csv'%(startingDate,endingDate)

    output_file = open(outputFileName, 'w')
    header = "dateTime,date,Time,step,xAcc,yAcc,zAcc,azimuth,pitch,roll,light,longitude,altitude,batteryCharging,batteryPercent,screenOn,earplug,screenOrientation,diffStep,proximity,gravX,gravY,gravZ,rotX,rotY,rotZ\n"

    output_file.write(header)
    __i_file = 0
    for ele_file in glob.glob(dirFi+'\motion\*_motion.csv'):
        indoor_flag = False

        csv_file = dirFi+'csv/'+os.path.basename(ele_file).replace('_motion','')
        #print ele_file, csv_file
        if 'orion' in ''.join(open(csv_file).readlines()).lower() :
            indoor_flag = True
        timeInFile = filter(str.isdigit, os.path.basename(ele_file))
        if indoor_flag and timeInFile > startingDate and timeInFile <= endingDate:

            date,time = os.path.basename(ele_file).split('_')[1:3]
            ele_motion = ['0']*(len(header.split(','))-2+offset)
            i = 0
            for ele_line in open(ele_file):
                s_ele_line = ele_line.split(',')
                if s_ele_line[0].lower() == 's':
                    if __i_file == 0:
                        __previous_step = s_ele_line[1]
                        __i_file += 1
                    ele_motion[1+offset] = s_ele_line[1]
                    ele_motion[16+offset] = __compare_positive(float(s_ele_line[1]) - float(__previous_step),0)
                    __previous_step = s_ele_line[1]
                elif s_ele_line[0].lower() == 'a':
                    ele_motion[2+offset] = s_ele_line[1]
                    ele_motion[3+offset] = s_ele_line[2]
                    ele_motion[4+offset] = s_ele_line[3]
                elif s_ele_line[0].lower() == 'o':
                    ele_motion[5+offset] = s_ele_line[1]
                    ele_motion[6+offset] = s_ele_line[2]
                    ele_motion[7+offset] = s_ele_line[3]
                elif s_ele_line[0].lower() == 'l':
                    ele_motion[8+offset] = s_ele_line[1]
                elif s_ele_line[0].lower() == 'p':
                    ele_motion[17+offset] = s_ele_line[1]
                elif s_ele_line[0].lower() == 'g':
                    ele_motion[18+offset] = s_ele_line[1]
                    ele_motion[19+offset] = s_ele_line[2]
                    ele_motion[20+offset] = s_ele_line[3]
                elif s_ele_line[0].lower() == 'r':
                    ele_motion[21+offset] = s_ele_line[1]
                    ele_motion[22+offset] = s_ele_line[2]
                    ele_motion[23+offset] = s_ele_line[3]

                #if not '0' in ele_motion[2+offset : 7+offset] and not '0' in ele_motion[11+offset : 17+offset ]:
                #if not '0' in ele_motion[2+offset : 7+offset] and ele_motion[16+offset] < 50:
                _time,_carry_date = __updateTime2(time,i)
                ele_motion[0] =  __dateFormat(date, _carry_date) + ' ' + _time + ',' + __dateFormat(date, _carry_date) + ',' + _time
                output_file.write(','.join(ele_motion)+'\n')
                #print ele_motion
                i += 1
    output_file.close()

def sensorData2Timeline(dirFi, nameIndex = None, startingDate = None, endingDate = None):
    if nameIndex is None:
        nameIndex = -2
    outputFileName = dirFi.split('/')[nameIndex]+'_motion_timeline.csv'
    if endingDate is None:
        endingDate = 'a'
    if startingDate is None:
        startingDate = '0'

    output_file = open(outputFileName, 'w')
    output_file.write('dateTime,date,Time,step,xAcc,yAcc,zAcc,azimuth,pitch,roll,light,'+
            'pressure,latitude,longitude,altitude,batteryCharging,batteryPercent,'+
            'screenOn,earplug,screenOrientation,temperature,voltage,booleanStep,diffStep\n')
    __i_file = 0
    for ele_file in glob.glob(dirFi+'\csv\*.csv'):
        timeInFile = filter(str.isdigit, os.path.basename(ele_file))
        if timeInFile > startingDate and timeInFile <= endingDate:
            #print timeInFile
            date,time = os.path.splitext(os.path.basename(ele_file))[0].split('_')[1:3]
            ele_motion = ['0']*(22+offset)
            firstLine = 0
            for ele_line in open(ele_file):
                if firstLine == 0 :
                    s_ele_line = ele_line.split(',')
                    if __i_file == 0:
                        __previous_step = s_ele_line[6]
                        __i_file += 1
                    ele_motion[1+offset] = s_ele_line[6]
                    ele_motion[21+offset] = __compare_positive(float(s_ele_line[6]) - float(__previous_step),0)
                    __previous_step = s_ele_line[6]
                    #ele_motion[1+offset] = s_ele_line[6] # step

                    ele_motion[2+offset] = s_ele_line[1] # accel
                    ele_motion[3+offset] = s_ele_line[2]
                    ele_motion[4+offset] = s_ele_line[3]

                    ele_motion[5+offset] = s_ele_line[15] # error? azimuth
                    ele_motion[6+offset] = s_ele_line[16]
                    ele_motion[7+offset] = s_ele_line[17]

                    ele_motion[8+offset] = s_ele_line[0] # light

                    ele_motion[9+offset] = s_ele_line[8]  # pressure

                    ele_motion[10+offset] = s_ele_line[9] # latitude
                    ele_motion[11+offset] = s_ele_line[10]
                    ele_motion[12+offset] = s_ele_line[11]
                    ele_motion[20+offset] = s_ele_line[7]
                    firstLine += 1

                elif 'bat' in ele_line :
                    s_ele_line = ele_line.split(',')
                    s_ele_line = map (lambda ele : ele.replace('\n',''), s_ele_line)
                    _len = len(s_ele_line)
                    ele_motion[13+offset] = s_ele_line[1] # batteryCharging
                    if _len > 9:
                        ele_motion[14+offset] = s_ele_line[9]  # batteryPercent
                    if _len > 10:
                        ele_motion[15+offset] = s_ele_line[10] # screenOn
                    if _len > 11:
                        ele_motion[16+offset] = s_ele_line[11] # earplug
                    if _len > 12:
                        ele_motion[17+offset] = s_ele_line[12] # screenOrientation

                    if _len > 6:
                        ele_motion[18+offset] = s_ele_line[6] # temperature
                    if _len > 7:
                        ele_motion[19+offset] = s_ele_line[7] # voltage

                _time,_carry_date = __updateTime1(time)
                #ele_motion[0] = __dateFormat(date,_carry_date) + ',' + _time
                #ele_motion[0] = __dateFormat(date, _carry_date) + ',' + _time + ',' + __dateFormat(date, _carry_date) + ' ' + _time
                ele_motion[0] =  __dateFormat(date, _carry_date) + ' ' + _time + ',' + __dateFormat(date, _carry_date) + ',' + _time
            output_file.write(','.join(ele_motion)+'\n')
    output_file.close()

def sensorData2Timeline_indoor(dirFi, nameIndex = None, startingDate = None, endingDate = None):
    if nameIndex is None:
        nameIndex = -2
    outputFileName = dirFi.split('/')[nameIndex]+'_indoor_sensor_timeline.csv'
    if endingDate is None:
        endingDate = 'a'
    if startingDate is None:
        startingDate = '0'

    output_file = open(outputFileName, 'w')
    output_file.write('dateTime,date,Time,step,xAcc,yAcc,zAcc,azimuth,pitch,roll,light,'+
            'pressure,latitude,longitude,altitude,batteryCharging,batteryPercent,'+
            'screenOn,earplug,screenOrientation,temperature,voltage,booleanStep,diffStep\n')
    __i_file = 0
    for ele_file in glob.glob(dirFi+'\csv\*.csv'):
        indoor_flag = False
        if 'orion' in ''.join(open(ele_file).readlines()).lower() :
            indoor_flag = True
        timeInFile = filter(str.isdigit, os.path.basename(ele_file))
        if indoor_flag and timeInFile > startingDate and timeInFile <= endingDate:
            #print timeInFile
            date,time = os.path.splitext(os.path.basename(ele_file))[0].split('_')[1:3]
            ele_motion = ['0']*(22+offset)
            firstLine = 0
            for ele_line in open(ele_file):
                if firstLine == 0 :
                    s_ele_line = ele_line.split(',')
                    if __i_file == 0:
                        __previous_step = s_ele_line[6]
                        __i_file += 1
                    ele_motion[1+offset] = s_ele_line[6]
                    ele_motion[21+offset] = __compare_positive(float(s_ele_line[6]) - float(__previous_step),0)
                    __previous_step = s_ele_line[6]
                    #ele_motion[1+offset] = s_ele_line[6] # step

                    ele_motion[2+offset] = s_ele_line[1] # accel
                    ele_motion[3+offset] = s_ele_line[2]
                    ele_motion[4+offset] = s_ele_line[3]

                    ele_motion[5+offset] = s_ele_line[15] # error? azimuth
                    ele_motion[6+offset] = s_ele_line[16]
                    ele_motion[7+offset] = s_ele_line[17]

                    ele_motion[8+offset] = s_ele_line[0] # light

                    ele_motion[9+offset] = s_ele_line[8]  # pressure

                    ele_motion[10+offset] = s_ele_line[9] # latitude
                    ele_motion[11+offset] = s_ele_line[10]
                    ele_motion[12+offset] = s_ele_line[11]
                    ele_motion[20+offset] = s_ele_line[7]
                    firstLine += 1

                elif 'bat' in ele_line :
                    s_ele_line = ele_line.split(',')
                    s_ele_line = map (lambda ele : ele.replace('\n',''), s_ele_line)
                    _len = len(s_ele_line)
                    ele_motion[13+offset] = s_ele_line[1] # batteryCharging
                    if _len > 9:
                        ele_motion[14+offset] = s_ele_line[9]  # batteryPercent
                    if _len > 10:
                        ele_motion[15+offset] = s_ele_line[10] # screenOn
                    if _len > 11:
                        ele_motion[16+offset] = s_ele_line[11] # earplug
                    if _len > 12:
                        ele_motion[17+offset] = s_ele_line[12] # screenOrientation

                    if _len > 6:
                        ele_motion[18+offset] = s_ele_line[6] # temperature
                    if _len > 7:
                        ele_motion[19+offset] = s_ele_line[7] # voltage

                _time,_carry_date = __updateTime1(time)
                #ele_motion[0] = __dateFormat(date,_carry_date) + ',' + _time
                #ele_motion[0] = __dateFormat(date, _carry_date) + ',' + _time + ',' + __dateFormat(date, _carry_date) + ' ' + _time
                ele_motion[0] =  __dateFormat(date, _carry_date) + ' ' + _time + ',' + __dateFormat(date, _carry_date) + ',' + _time
            output_file.write(','.join(ele_motion)+'\n')
    output_file.close()


def __dateFormat(date, carry_date):
    if carry_date == 0 :
        return date[0:4]+'-'+date[4:6]+'-'+date[6:8]
    elif carry_date > 0 :
        year = int(date[0:4])
        month = int(date[4:6])
        day = int(date[6:8])+1
        if day > 31:
            day = 1
            month += 1
            if month > 12:
                month = 1
                year += 1
        return __zfillFormat(year,4)+'-'+__zfillFormat(month,2)+'-'+ __zfillFormat(day,2)

def __timeFormat(time):
    carry_date = 0
    time = __zfillFormat(time,6)
    hour = int(time[0:2])
    minute = int(time[2:4])
    second = int(time[4:6])
    if second >= 60 :
        second -= 60
        minute += 1
        if minute >=60:
            minute -= 60
            hour += 1
            if hour == 24:
                hour = 0
                carry_date = 1
    return __zfillFormat(hour,2) +':'+ __zfillFormat(minute,2) +':'+ __zfillFormat(second,2), carry_date

def __zfillFormat(time, digits):
    return str(time).zfill(digits)

def __compare_positive(num1, num2):
    __diff = np.abs(num1 - num2)
    return str(np.max(__diff, 0 ))

def __updateTime1(time):
    return __timeFormat(int(time)+15)

def __updateTime2(time, i):
    detTime = 0.06
    second, microSecond = str(float(time) + i * detTime).split('.')[0:2]
    finalTime , carry_date = __timeFormat(second)[0:2]
    return finalTime+'.'+microSecond , carry_date


def _test_timeFormat():
    print __timeFormat(235965)
def _test_dateFormat():
    print __dateFormat('20161231',1)


from matplotlib.backends.backend_pdf import PdfPages
def __gener_sensorFusion4Motion_singleFile(dirFi,time_in_file):
    pp = PdfPages('sensorFusion4Motion.pdf')
    filename = dirFi+'motion/PhilNexus_'+ time_in_file+'_motion.csv'
    fig,step = __plot(filename)
    fig.savefig(pp,format='pdf')
    pp.close()

def __gener_sensorFusion4Motion_rshall(dirFi, rshall_file = None):
    if rshall_file is None:
        rshall_file = r'd:\class\Semester5\research\light\python\LosRealProduct\dev\wifi\labelRound\rshall.csv'
    pp = PdfPages('sensorFusion4Motion_5steps.pdf')
    for line in open(rshall_file):
        time_in_file = line.split(',')[0]
        filename = dirFi+'motion/PhilNexus_'+ time_in_file+'_motion.csv'
        fig,step = __plot(filename)
        if step > 5:
            fig.savefig(pp,format='pdf')
    pp.close()

def __plot(_i_filename):
    #t_list = ('dateTime','date','Time','step','xAcc','yAcc','zAcc','azimuth','pitch','roll','light','diffStep','proximity','gravX','gravY','gravZ','rotX','rotY','rotZ')
    #print _i_filename
    date, time = os.path.splitext(os.path.basename(_i_filename))[0].split('_')[1:3]
    title = str(__dateFormat(date,0)) + ' ' + str(__timeFormat(time)[0])

    count_step = 0
    step_list = []
    light_list = []
    xAcc_list = []
    yAcc_list = []
    zAcc_list = []
    azimuth_list = []
    pitch_list   = []
    roll_list    = []
    xRot_list = []
    yRot_list = []
    zRot_list = []
    xGrav_list = []
    yGrav_list = []
    zGrav_list = []
    xGyro_list = []
    yGyro_list = []
    zGyro_list = []
    proxi_list = []

    step = 0
    light = 0
    xAcc = 0
    yAcc = 0
    zAcc = 0
    azimuth = 0
    pitch   = 0
    roll    = 0
    xRot = 0
    yRot = 0
    zRot = 0
    xGrav = 0
    yGrav = 0
    zGrav = 0
    xGyro = 0
    yGyro = 0
    zGyro = 0
    proxi = 0

    for line in open(_i_filename):
        step = 0
        ele_line = line.split(',')
        if 'A' in ele_line[0]:
            xAcc = ele_line[1]
            yAcc = ele_line[2]
            zAcc = ele_line[3]
        elif 'O' in ele_line[0]:
            azimuth = ele_line[1]
            pitch   = ele_line[2]
            roll    = ele_line[3]
        elif 'G' in ele_line[0]:
            xGrav = ele_line[1]
            yGrav = ele_line[2]
            zGrav = ele_line[3]
        elif 'S' in ele_line[0]:
            step = 1
            count_step += 1
        elif 'P' in ele_line[0]:
            proxi = ele_line[1]
        elif 'L' in ele_line[0]:
            light = ele_line[1]
        elif 'R' in ele_line[0]:
            xRot = ele_line[1]
            yRot = ele_line[2]
            zRot = ele_line[3]
        elif 'Y' in ele_line[0]:
            xGyro = ele_line[1]
            yGyro = ele_line[2]
            zGyro = ele_line[3]

        xAcc_list.append(xAcc)
        yAcc_list.append(yAcc)
        zAcc_list.append(zAcc)
        azimuth_list.append(azimuth)
        pitch_list.append(pitch)
        roll_list.append(roll)
        xGrav_list.append(xGrav)
        yGrav_list.append(yGrav)
        zGrav_list.append(zGrav)
        xRot_list.append(xRot)
        yRot_list.append(yRot)
        zRot_list.append(zRot)
        xGyro_list.append(xGyro)
        yGyro_list.append(yGyro)
        zGyro_list.append(zGyro)
        light_list.append(light)
        step_list.append(step)
        proxi_list.append(proxi)

    fig = plt.figure()
    ax1 = plt.subplot(711)
    ax2 = plt.subplot(712)
    ax3 = plt.subplot(713)
    ax4 = plt.subplot(714)
    ax5 = plt.subplot(715)
    ax6 = plt.subplot(716)
    ax7 = plt.subplot(717)

    plt.sca(ax1)
    plt.title(title + '  step' + ' Proximity')
    plt.plot(step_list,'or-', proxi_list,'-')

    plt.sca(ax2)
    plt.title('accelerometer')
    plt.plot(xAcc_list,'r-')
    plt.plot(yAcc_list,'b-')
    plt.plot(zAcc_list,'g-')
    plt.plot([0]*len(xAcc_list),'y--')

    plt.sca(ax3)
    plt.title('Orientation')
    plt.plot(azimuth_list,'r-')
    plt.plot(pitch_list,'b-')
    plt.plot(roll_list,'g-')

    plt.sca(ax4)
    plt.title('Gyroscope')
    plt.plot(xGyro_list,'r-')
    plt.plot(yGyro_list,'b-')
    plt.plot(zGyro_list,'g-')

    plt.sca(ax5)
    plt.title('Rotation')
    plt.plot(xRot_list,'r-')
    plt.plot(yRot_list,'b-')
    plt.plot(zRot_list,'g-')

    plt.sca(ax6)
    plt.title('Light')
    plt.plot(light_list,'-')

    plt.sca(ax7)
    plt.title('Gravity')
    plt.plot(xGrav_list,'r-')
    plt.plot(yGrav_list,'b-')
    plt.plot(zGrav_list,'g-')
    plt.plot([0]*len(xGrav_list),'y--')
    #plt.show()
    return fig, count_step

def __plot2pdf():
    plt.title('Gravity')
    xGrav_list=[1,2,3]
    yGrav_list=[3,2,1]
    zGrav_list=[-2,2,2]

    plt.plot([0]*len(xGrav_list),'y--')
    plt.plot(xGrav_list,'r-')
    plt.plot(yGrav_list,'b-')
    plt.plot(zGrav_list,'g-')
    plt.show()

    pass

def plot_trajectory(dirFi,timestamp = None, step_count = None):
    if timestamp is None:
        timestamp = '0'

    pp = PdfPages('stepMotionPdf/'+timestamp+step_count+'.pdf')
    filename = dirFi+'PhilNexus_'+ timestamp+'_motion.csv'
    fig,step = __plot(filename)
    fig.savefig(pp,format='pdf')
    pp.close()



if __name__ == '__main__':
    #dirFi = r'd:\class\Semester5\research\ADLRecorder\code\Android\NexusSensors\DbRecords\AS\smh\MinxianLi\\'
    dirFi_0 = r'd:/class/Semester5/research/ADLRecorder/code/Android/NexusSensors/DbRecords/AS/smh/philNexus/'
    dirFi_1 = r'e:/phil/ADLRecorder/Dataset/PhilNexus/'
    rshall_0  = r'd:\class\Semester5\research\light\python\LosRealProduct\dev\wifi\labelRound\rshall.csv'
    rshall_1  = 'rshall.csv'
    rshall_2  = r'time_localization_result_no_step_diff_process_grouping_step2_grouping_step2.csv'
    #motionData2Timeline(dirFi, nameIndex = -2, startingDate = '20160901')
    #sensorData2Timeline(dirFi, nameIndex = -2, startingDate = '2016090502',endingDate = '2016090602')
    #sensorData2Timeline_indoor(dirFi, nameIndex = -2, startingDate = '2016090602',endingDate = '2016090702')
    #motionData2Timeline_indoor(dirFi, nameIndex = -2, startingDate = '2016092202',endingDate = '2016092302')
    #motionData2Timeline_indoor(dirFi, nameIndex = -2) #startingDate = '2016092202',endingDate = '2016092302')
    __gener_sensorFusion4Motion_rshall(dirFi_1, rshall_2)
    #__gener_sensorFusion4Motion_singleFile(dirFi_0, '20160823_073623')
    #__plot2pdf()




