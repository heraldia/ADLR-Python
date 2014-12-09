
class ActivityPredictionSet:

    def __init__(self,actualActivity,predictionSet):
        self.actualActivity = actualActivity
        self.predictionSet = predictionSet

    def infor(self):
        print self.actualActivity
        print self.predictionSet

class ActivitiesSet:

    #activitiesSet = set()
    def __init__(self):
       self.activitiesSet = set()

    '''
    def __init__(self,activityTuple):
        self.activitiesSet.add(activityTuple)
    '''

    def addTuple(self,activityTuple):
        self.activitiesSet.add(activityTuple)

    def infor(self):
        print self.activitiesSet

if __name__=="__main__":
    dinnerSet = set()
    dinnerSet.add('cooking')
    dinnerSet.add('music and eating')
    ActivityPredict1 = ActivityPredictionSet('Dinner',dinnerSet)
    ActivityPredict1.infor()

