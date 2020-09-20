class Person:

    def __init__(self):
        self.name = getName() #string
        self.preferredExercises = getPreferredExcercises() #list
        self.workoutLocations = getWorkoutLocations() #\shrug
        self.currentExerciseIndex = 0 #int
        self.watch = getWatch() #Watch Object

    def updateCurrentExercise(self):
        numExercises = len(self.preferredExercises)
        self.currentExerciseIndex = (self.currentExerciseIndex + 1)%numExercises

    def getCurrentExercise(self):
        return self.preferredExercises[self.currentExerciseIndex]

    def updateLocation(self, loc=None):
        if loc: self.currentLocation = loc               
 
        watch = self.watch
        ###do fancy watch calls###
        self.currentLocation = watch.getLocation

    def checkLocation(self, currentLocation):
        if currentLocation in self.workoutLocations: return True
        return False

    def checkActive(self, ext=False):
        if external: return external

        watch = self.watch
        ###do fancy watch calls###
        if watch.getActive(): return True
        return False

    def checkSendNotification(self, currentLocation):
        if checkLocation() and checkActive(ext=True): return True
        else: False
        
