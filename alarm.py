import time
import pygame

def alarm():
    duration = input("What time do you want to be informed? (HH:MM):\n")
    title = input("Alarm Title: ")
    while True:
        t = time.localtime()
        current = f"{t.tm_hour:02d}:{t.tm_min:02d}"
        print(f"Current time: {current}", end="\r")

        if current == duration:
            print(f"\n⏰ {title} - TIME'S UP")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            break

        time.sleep(1)



pygame.mixer.init()

sound = "/home/akim/Downloads/fahhhhhhhhhhhhhh.mp3"
pygame.mixer.music.load(sound)

def countdown(length):
    for i in range(length, -1, -1):
        print(i)
        time.sleep(1)

    print("DING!! DING!! DING!!")
    print("Time's up")

    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)


while True:
    menu = input(
    "-" * 25 +
    "\n1. Countdown\n"
    "2. Alarm\n" +
    "'q' to quit\n" +
    "-" * 25 +
    "\nSelect option: "
)
    if menu == "1":
        length1 = int(input("how long?: "))
        countdown(length1)
        break
    elif menu == "2":
        alarm()
        break
    elif menu.lower() == "q":
        break
    else :
        print("fix your input. try again ")
