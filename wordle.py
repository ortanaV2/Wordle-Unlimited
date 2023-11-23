import time
from rich import print as printr
import json
import random
import datetime
import os

with open("userdata.json", "r") as user:
    user_data = json.load(user)
with open("dataset.json", "r") as dataset:
    word_list = json.load(dataset)
session_xp = user_data[0]
session_count = user_data[1]
if session_xp == 0:
    session_xp = 1

while True:
    start_time = datetime.datetime.now()
    chosen_word = random.choice(word_list)
    data_list = [letter for letter in chosen_word]
    try_data = [[],[],[],[],[],[]]
    os.system("cls")
    win = False
    for tries in range(6):
        while True:
            guess = (str(input("\nGuess the word: "))).lower()
            if len(guess) > 5:
                print("too long!")
            elif len(guess) < 5:
                print("too short!")
            else:
                if guess in word_list:
                    if guess == chosen_word:
                        end_time = datetime.datetime.now()
                        time_took = end_time - start_time
                        total_seconds = time_took.total_seconds()
                        minutes = int((total_seconds % 3600) // 60)
                        seconds = int(total_seconds % 60)
                        xp_gain = int(((100-((total_seconds)+1/2))+2)/(tries))
                        os.system("cls")
                        for letter in chosen_word:
                            printr(f"[black on green]{letter} ", end='', flush=True)
                            time.sleep(0.25)
                        printr("\n\n[white on blue] You won! ")
                        time.sleep(0.2)
                        print("_"*15)
                        print(f"Tries: {tries+1}")
                        time.sleep(0.2)
                        print("_"*15)
                        print(f"Time: {minutes}m {seconds}s")
                        time.sleep(0.2)
                        print("_"*15)
                        print(f"Gain: +{xp_gain}xp")
                        session_xp+=xp_gain
                        time.sleep(0.2)
                        print("_"*15)
                        print(f"Experience: {session_xp}xp")
                        time.sleep(0.2)
                        print("_"*15)
                        session_count+=1
                        print(f"Session: {session_count}")
                        time.sleep(0.2)
                        print("_"*15)
                        input("\n[Press enter to restart]")
                        win = True
                        user_data[0] = session_xp
                        user_data[1] = session_count
                        with open("userdata.json", "w") as user:
                            json.dump(user_data, user)
                    break
                else:
                    print("unknown word.")
        if win:
            break
        for letter in guess:
                try_data[tries].append(str(letter))
        os.system("cls")
        for line in try_data:
            if line != []:
                word_count=0
                for letter in line:
                    if letter == data_list[word_count]:
                        printr(f"[black on green]{letter} ", end='', flush=True)
                        time.sleep(0.1)
                    elif letter in data_list:
                        printr(f"[black on yellow]{letter} ", end='', flush=True)
                        time.sleep(0.1)
                    else:
                        printr(f"[white on grey]{letter} ", end='', flush=True)
                        time.sleep(0.1)
                    word_count+=1
                print() #formatting
    
    if not win:
        time.sleep(0.2)
        printr("\n\n[black on red] You lost. ")
        print(f"Solution: {chosen_word}")
        time.sleep(0.2)
        input("\n[Press enter to restart]")
