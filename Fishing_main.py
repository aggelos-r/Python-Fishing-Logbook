import os
import time
from PIL import Image
BLUE = "\033[34m"
LIGHT_RED = "\033[38;5;197m"
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
ORANGE = "\033[38;5;208m"

max_trips=30
place1 = {str(i): f"Fishing/Places/place1_{i}.txt" for i in range(1, max_trips+1)} 
place2 = {str(i): f"Fishing/Places/place2_{i}.txt" for i in range(1, max_trips+1)} 
place3 = {str(i): f"Fishing/Places/place3_{i}.txt" for i in range(1, max_trips+1)} 
place4 = {str(i): f"Fishing/Places/place4_{i}.txt" for i in range(1, max_trips+1)} 
place5 = {str(i): f"Fishing/Places/place5_{i}.txt" for i in range(1, max_trips+1)} 

place1_images = {str(i): [] for i in range(1, max_trips + 1)}
place2_images = {str(i): [] for i in range(1, max_trips + 1)}
place3_images = {str(i): [] for i in range(1, max_trips + 1)}
place4_images = {str(i): [] for i in range(1, max_trips + 1)}
place5_images = {str(i): [] for i in range(1, max_trips + 1)}

Fishing={"1":place1,
         "2":place2,
         "3":place3,
         "4":place4,
         "5":place5}

Fishing_images={"1":place1_images,
                "2":place2_images,
                "3":place3_images,
                "4":place4_images,
                "5":place5_images}

def clear_terminal():
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')


def find_fishing_trip(AA,BB,mt):
    while True:
        clear_terminal()
        print(f"{ORANGE}Select the location where the fishing trip took place:{RESET}")
        print(f"1. Fishing_place_1")
        print(f"2. Fishing_place_2")
        print(f"3. Fishing_place_3")
        print(f"4. Fishing_place_4")
        print(f"5. Fishing_place_5")
        print(f"0. Return to the main MENU")
        choice=input(f"{BLUE}Make a choice: {RESET}")
        while choice not in ["0","1","2","3","4","5"]:
            print(f"{RED}Invalid choice, try again{RESET}")
            choice=input(f"{BLUE}Make a choice: {RESET}")
        if choice != "0" :
            try:
                i=0
                for j in range(1,mt+1):
                    j=str(j)
                    if os.path.getsize(AA[choice][j]) != 0:
                        i+=1
                choice=str(choice)
                if i!=0:
                    clear_terminal()
                    print(f"{ORANGE}There are {i} saved fishing trips for this location{RESET}")
                    for j in range(i):
                        with open(AA[choice][str(j+1)],"r",encoding="utf-8") as file:
                            info = file.readline().strip().replace("Date/Time :", "").strip().split(",")[0].strip()
                        print(f"{j+1}. {info}")
                    print(f"{BLUE}Press a number from 1-{i} to view info about the corresponding trip{RESET}") 
                    choice1=input(f"{BLUE}Make a choice: {RESET}")
                    while choice1 not in map(str,range(1,i+1)) :
                        print(f"{RED}Invalid choice, try again{RESET}")
                        choice1=input(f"{BLUE}Make a choice: {RESET}")
                    x="a"
                    while x!="":
                        clear_terminal()
                        print(f"{ORANGE}Information about the fishing trip:{RESET}")
                        with open(AA[choice][choice1],"r",encoding="utf-8") as file:
                            print(file.read())
                        print(" ")
                        if isinstance(BB[choice][choice1], list) and len(BB[choice][choice1]) > 0:
                            print(f"{GREEN}There are {len(BB[choice][choice1])} photos from this trip")
                            for j in range(len(BB[choice][choice1])):
                                x=input(F"{GREEN}Press << ENTER >> to see a photo from this trip, or << 1 >> to skip the photos: {RESET}")
                                while x not in ["","1"]:
                                    print(f"{RED}Invalid choice, try again{RESET}")
                                    x=input(F"{GREEN}Press << ENTER >> to see a photo from this trip, or << 1 >> to skip the photos: {RESET}")
                                if x=="1":
                                    break
                                img = Image.open(BB[choice][choice1][j])
                                img.show()
                        if int(choice1)==i:
                            x=input(F"{GREEN}Press << ENTER >> to return to the MENU: {RESET}")
                        else:
                            x=input(F"{GREEN}Press << ENTER >> to return to the MENU or << 1 >> to view info about the next fishing trip in this place: {RESET}")
                            while x not in ["","1"]:
                                print(f"{RED}Invalid choice, try again{RESET}")
                                x=input(F"{GREEN}Press << ENTER >> to return to the MENU or << 1 >> to view info about the next fishing trip in this place: {RESET}")
                            choice1=str(int(choice1)+1)
                else:
                    print(" ")
                    print(F"{RED}No fishing trips saved for this location, choose another{RESET}")
                    time.sleep(2)
            except FileNotFoundError:
                print("")
                print(f"{RED}A FILE DOES NOT EXIST{RESET}")
                time.sleep(2)
        else:
            break

def add_fishing_trip(AA,BB,mt):
    clear_terminal()
    print(f"{ORANGE}Select the location where the fishing trip took place:{RESET}")
    print(f"1. Fishing_place_1")
    print(f"2. Fishing_place_2")
    print(f"3. Fishing_place_3")
    print(f"4. Fishing_place_4")
    print(f"5. Fishing_place_5")
    print(f"If the location is not in the MENU, press << 0 >> to return to the main MENU")
    choice=input(f"{BLUE}Make a choice: {RESET}")
    while choice not in ["0","1","2","3","4","5"]:
            print(f"{RED}Invalid choice, try again{RESET}")
            choice=input(f"{BLUE}Make a choice: {RESET}")
    if choice != "0":
        try:
            i=1
            for j in range(1,mt+1):
                j=str(j)
                if os.path.getsize(AA[choice][j]) != 0:
                    i+=1
            i=str(i)
            choice=str(choice)
            clear_terminal()
            date="Date/Time : "+input(F"{BLUE}When did the fishing take place (day/month/year , start time-->end time): {RESET}")
            weather="\nWeather : "+input(F"{BLUE}Describe the weather (e.g. wind, waves, temperature, rain, pressure, moon, clouds): {RESET}")
            fish="\nFish : "+input(F"{BLUE}What fish were caught, how many kilos: {RESET}")
            extra="\nComments : "+input(F"{BLUE}Add any comments if you'd like: {RESET}")
            with open(AA[choice][i],"a",encoding="utf-8") as file:
                file.write(date)
                file.write(weather)
                file.write(fish)
                file.write(extra)
            print(F"{GREEN}The information for this fishing trip was saved{RESET}")
            time.sleep(2)
        except FileNotFoundError:
            print("")
            print(f"{RED}A FILE DOES NOT EXIST{RESET}")
            time.sleep(2)

def main():
    while True:
        clear_terminal()
        print(f"{ORANGE}Menu{RESET}")
        print(f"1. Find previous fishing trips")
        print(f"2. Add a fishing trip")
        print(f"3. Exit program")
        choice=input(f"{BLUE}Make a choice: {RESET}")
        while choice not in ["1","2","3"]:
            print(f"{RED}Invalid choice, try again{RESET}")
            choice=input(f"{BLUE}Make a choice: {RESET}")
        choice=int(choice)
        print(" ")
        if choice == 3 :
            print(F"{LIGHT_RED}EXITING PROGRAM{RESET}")
            break
        elif choice == 1:
            find_fishing_trip(Fishing,Fishing_images,max_trips)
        elif choice == 2:
            add_fishing_trip(Fishing,Fishing_images,max_trips)


if __name__=="__main__":
    main()
