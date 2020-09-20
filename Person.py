class Person:

    def __init__(self, name, preferredExercises, workoutLocations, watch):
        self.name = name
        self.preferredExercises = preferredExercises
        self.workoutLocations = workoutLocations
        self.currentExerciseIndex = 0
        self.watch = watch

    def updateCurrentExercise(self):
        numExercises = len(self.preferredExercises)
        self.currentExerciseIndex = (self.currentExerciseIndex + 1) % numExercises

    def getCurrentExercise(self):
        return self.preferredExercises[self.currentExerciseIndex]

    def checkLocation(self):
        return self.watch.getLocation() in self.workoutLocations

    def checkSendNotification(self):
        return self.checkLocation() and self.watch.isActive()
