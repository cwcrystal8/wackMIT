from Person import Person
import constants
import UI
import time
from Watch import Watch

def setUp():
    # Ask for name
    name = input("Enter your name: ")

    # Ask for workoutLocations
    workoutLocations = input("Enter your workout locations in a comma separated list: ").split(",")
    workoutLocations = [word.strip() for word in workoutLocations]

    # Ask for preferredExercises
    preferredExercises = input("Enter your preferred exercises in a comma separated list: ").split(",")
    preferredExercises = [word.strip() for word in preferredExercises]

    # Create watch
    watch = Watch()

    return Person(name, preferredExercises, workoutLocations, watch)

def loop(person):
    if person.checkSendNotification():
        response = input(f"Now seems like a good time to exercise. Would you like to exercise? (Y/N/Q) ")
        if response.lower() == "q":
            return None
        if response.lower() == "y":
            for i in range(len(person.preferredExercises)):
                response = input(f"Would you like to do {person.getCurrentExercise()}? (Y/N/Q) ")
                person.updateCurrentExercise()
                if response.lower() == "q":
                    return None
                if response.lower() == "y":
                    return True
            print("Looks like you don't want to exercise then...")
    return False

if __name__ == "__main__":
    person = setUp()
    while True:
        time.sleep(1)
        did_exercise = loop(person)
        if did_exercise:
            print(f"Wow! Great job {person.name}!")
        if did_exercise is None:
            print("Bye!")
            break
