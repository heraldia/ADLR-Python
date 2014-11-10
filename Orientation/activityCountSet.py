
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

    def inforName(self):
        print self.activity

    def inform(self):
        #print self.__dict__
        print self.orientation,
        print ":",
        print self.count
        return 0

    def infor(self):
        #print self.__dict__
        print self.activity,  self.orientation, self.count
        #print '-'*30
        return 0

    def isEqual(self, activityPair ):
        return self.activity == activityPair.activity and\
                self.orientation == activityPair.orientation

    def isEqual(self, activity, orie ):
        return self.activity == activity and\
                self.orientation == orie

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
    tempTuple = ['Bathroom','N']
    tempTuple1 = ['Bathroom','S']
    tempTuple2 = ['Bathroom','NE']
    orientationSet.add('S')
    #print orientationSet
    '''
    activitiesOrientationPair = ActivitiesOrientationPair()
    activitiesOrientationPair.addTuple(activityTupleM)
    activitiesOrientationPair.infor()
    #activityCountSet = ActivityCountSet("Bathroom","N")
    '''
    objSetActiOriePairNames  = set()
    #actiObjSet = set()

    for activity in activitySet:
        for orientation in orientationSet:
            actiOriePairNameObj = ActivitiesOrientationPair(activity,orientation)
            #actiObjSet.add(actiOriePairNameObj)

            actiOriePairName = ActivityCountSet(actiOriePairNameObj)
            objSetActiOriePairNames .add(actiOriePairName)
            #print "+"

    for obj in objSetActiOriePairNames :
        if obj.isEqual(tempTuple[0],tempTuple[1]):
            obj. increment()
        if obj.isEqual(tempTuple1[0],tempTuple1[1]):
            obj. increment()
        if obj.isEqual(tempTuple2[0],tempTuple2[1]):
            obj. increment()
        if obj.isEqual(tempTuple[0],tempTuple[1]):
            obj. increment()
        #obj.inforName()
        obj.infor()
