import pyautogui
import studentList
import pyperclip
import time
import requests

national_codes = [studentList.HAFTOM,studentList.HASHTOM,studentList.NOHOM]
star_group_index = 1

start_from_national_code = "********"
titles = {
    "subject":[" پژوهش "," دست سازه "," برنامه نویسی "," مناظره علمی "," ریاضی "],
    "x":51,
    "y":[563,347,434,522,607]
}


def new_submit(x,y):
    pyautogui.click(x,y)
def write_group_name(subject,index):
    pyautogui.click(1145,402)
    time.sleep(2)
    pyperclip.copy(" گروه " + subject + index)
    pyautogui.hotkey("ctrl", "v")
def add_user_to_group(paye,i):
    pyautogui.click(1091,454)
    time.sleep(2)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.write(paye[i])
    pyautogui.press('tab')
    time.sleep(5)
    pyautogui.click(437,609)
    time.sleep(4)    
def submit_to_kharazmi():
    time.sleep(4)
    pyautogui.click(289,710)
    time.sleep(8)
def individual_submit():
    insert = False
    for paye in national_codes:
        for code in paye:
            if code == start_from_national_code:
                insert = True
            if insert:
                new_submit(53,471)
                time.sleep(2)
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                time.sleep(2)
                pyautogui.write(code)
                pyautogui.press('tab')
                time.sleep(8)
                pyautogui.click(437,609)
                time.sleep(8)
def group_submit():
    code_counter = 0
    for paye in national_codes:
        for i in range(len(paye)//2):
            new_submit(titles["x"],titles["y"][0])#for bazarche
            time.sleep(2)
            write_group_name(titles['subject'][0],str(star_group_index + i))
            time.sleep(2)
            for _ in range(2):
                time.sleep(2)
                add_user_to_group(paye,code_counter)
                code_counter+=1
            submit_to_kharazmi()
        code_counter = 0

individual_submit()
#group_submit()