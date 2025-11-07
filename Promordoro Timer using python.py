#Promordoro Timer using python
import time
import random
def Promordoro_timer():
    print("Welcome to the Pomodoro Timer!")
    work_duration = 25 * 60  # 25 minutes
    break_duration = 5 * 60   # 5 minutes

    while True:
        print("Starting a Pomodoro session. Focus for 25 minutes!")
        time.sleep(work_duration)
        print("Time's up! Take a 5-minute break.")
        time.sleep(break_duration)
        cont = input("Do you want to start another Pomodoro session? (y/n): ")
        if cont.lower() != 'y':
            print("Thank you for using the Pomodoro Timer. Goodbye!")
            break
Promordoro_timer()