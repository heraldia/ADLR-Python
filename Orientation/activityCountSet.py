
class ActivityCountSet:

    """
    def __init__(self,activity,orientation):
        self.activity = activity
        self.orientation = orientation
        self.count = 0
    """

    def __init__(self,activityOrientationPair):
        self.activity = activityOrientationPair.activity
        self.orientation = activityOrientationPair.orientation
        self.count = 0

    def infor(self):
        print self.__dict__
        print self.activity,  self.orientation, self.count
        print '-'*30

    def isEqual(self, activityPair ):
        return self.activity == activityPair.activity and\
                self.orientation == activityPair.orientation

    def increment(self):
        #if self.activityOrientationPair
        self.count += 1

class ActivitiesOrientationPair:

    def __init__(self,activity, orientation ):
        self.activity = activity
        self.orientation = orientation

    '''
    def __init__(self):
        self.activitiesSet = set()

    def addTuple(self,activityTuple):
        self.activitiesSet.add(activityTuple)
    '''

    def infor(self):
        print self.activitiesSet

if __name__=="__main__":
    #bathRoomN = ["Bathroom","N"]
    activitySet = set(["Bathroom"])
    orientationSet = set(['N','NW','NE'])
    orientationSet.add('S')
    #print orientationSet
    '''
    activitiesOrientationPair = ActivitiesOrientationPair()
    activitiesOrientationPair.addTuple(activityTupleM)
    activitiesOrientationPair.infor()
    #activityCountSet = ActivityCountSet("Bathroom","N")
    '''
    objSet = set()
    actiObjSet = set()

    for activity in activitySet:
        for orientation in orientationSet:
            #actiOriePairNameStr = str(activity)+str(orientation)
            #actiOriePairNameObj = "act"+str(activity)+str(orientation)
            actiOriePairNameObj = ActivitiesOrientationPair(activity,orientation)
            actiObjSet.add(actiOriePairNameObj)

            actiOriePairName = ActivityCountSet(actiOriePairNameObj)
            objSet.add(actiOriePairName)
            #print "+"

    for obj in objSet :
        for tuiple in actiObjSet:
            if obj.isEqual(tuiple):
                obj. increment()
        print obj.infor()
