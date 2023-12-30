from pywinauto import Application #pip install pywinauto
import pygetwindow as gw #pip install pygetwindow
import pyautogui #pip install pyautogui
import argparse 
import time
import webbrowser
from datetime import date 
from sys import exit


def main():
    """
    The main function.     
    """
    parser = argparse.ArgumentParser(
                      description='Automaticaly store and load chrome tabs in/from .txt files.'         
                                 )
    parser.add_argument("-s", "--store", help="Store urls in a .txt file which can be later used to reopen them. Takes in one argument: store_into_this_file.txt or currently (automatically creates a folder with current date)", type=str)
    parser.add_argument("-l", "--load", help="Opens urls from a .txt file in browser. Takes in one argument: file_to_load.txt")

    global args
    args = parser.parse_args()

    
    if args.store != None:
        urls = get_urls()
        store_urls(urls)
    elif args.load != None:
        load_urls()
    else:
        exit("Program is currently doing nothing, try -h.")
    

    
def get_urls() -> list:
    """
    Retrieves the URLs of open tabs in Google Chrome and returns them as a list.
    """
    focus_chrome_tab()
    app = Application(backend='uia')
    app.connect(title_re=".*Chrome.*")
    dlg = app.top_window()
    urls: list = []
    counter: int = 0
    while True:
        url: str = dlg.child_window(title="Address and search bar", control_type="Edit").get_value()
        if url == "":
            pyautogui.hotkey('ctrl', 'tab')
            continue
        if url not in urls:        
            urls.append(url)
            pyautogui.hotkey('ctrl', 'tab')
            continue
        if url in urls:
            counter += 1
            if counter == 2:
                break
            continue
    return urls


def load_urls() -> None:    
    """
    Load URLs from a .txt file and open them in the Chrome browser.
    """
    try:
        load_name: str = str(args.load)
        urls_from_file: list = []
        if load_name.endswith(".txt") != False:
            with open(load_name, "r") as load_urls:
                for line in load_urls.readlines():
                    urls_from_file.append(line)
        else:
            exit("Could not read this file, invalid format")

        for url in urls_from_file:
            webbrowser.open_new_tab(f"https://{url}")
            time.sleep(0.3)
    except:
        exit("Error occured while loading the window.")

    return 0


def store_urls(urls: list) -> None:
    """
    Store URLs in a .txt file.
    """
    if args.store == "currently":
        store_name: str = f"{date.today()}.txt"
    if args.store != "currently":
        store_name: str = str(args.store)
    if store_name.endswith(".txt") != False:
        with open(store_name, "w") as store_urls:
            for element in urls:
                store_urls.writelines(f"{element}\n")
    else:
        exit("Could not store this file, invalid format.")

    return 0

        

def focus_chrome_tab() -> None:
    """
    Brings the Google Chrome window to the foreground.
    """
    try:
        target_window = gw.getWindowsWithTitle("Google Chrome")
        if not target_window:
            exit("Window was not found")
        target_window = target_window[0]
        target_window.restore()
        target_window.activate()
    except:
        exit("Error occured. Is Chrome opened?")

    return 0

if __name__ == "__main__":  
    main()
    
