import os
import time
import sys




introtext = """
  ______                                     ______                   __                     
 /      \                                   /      \                 /  |                    
/$$$$$$  |    __   ______   _______        /$$$$$$  |  ______    ____$$ |  ______    _______ 
$$ |  $$ |   /  | /      \ /       \       $$ |  $$/  /      \  /    $$ | /      \  /       |
$$ |  $$ |   $$/  $$$$$$  |$$$$$$$  |      $$ |      /$$$$$$  |/$$$$$$$ |/$$$$$$  |/$$$$$$$/ 
$$ |  $$ |   /  | /    $$ |$$ |  $$ |      $$ |   __ $$ |  $$ |$$ |  $$ |$$    $$ |$$      \ 
$$ \__$$ |   $$ |/$$$$$$$ |$$ |  $$ |      $$ \__/  |$$ \__$$ |$$ \__$$ |$$$$$$$$/  $$$$$$  |
$$    $$/    $$ |$$    $$ |$$ |  $$ |      $$    $$/ $$    $$/ $$    $$ |$$       |/     $$/ 
 $$$$$$/__   $$ | $$$$$$$/ $$/   $$/        $$$$$$/   $$$$$$/   $$$$$$$/  $$$$$$$/ $$$$$$$/  
       /  \__$$ |                                                                            
       $$    $$/                                                                             
        $$$$$$/                                                                              
"""

desc1 = """
  ____  _             _            _   
 / ___|| |_ _   _  __| | ___ _ __ | |_ 
 \___ \| __| | | |/ _` |/ _ \ '_ \| __|
  ___) | |_| |_| | (_| |  __/ | | | |_ 
 |____/ \__|\__,_|\__,_|\___|_| |_|\__|
"""

desc2 = """
  ____                                                          
 |  _ \ _ __ ___   __ _ _ __ __ _ _ __ ___  _ __ ___   ___ _ __ 
 | |_) | '__/ _ \ / _` | '__/ _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
 |  __/| | | (_) | (_| | | | (_| | | | | | | | | | | |  __/ |   
 |_|   |_|  \___/ \__, |_|  \__,_|_| |_| |_|_| |_| |_|\___|_|   
                  |___/                                         
"""

desc3 = """
   ____       __  __                       _     _ _      _   
  / ___|___  / _|/ _| ___  ___    __ _  __| | __| (_) ___| |_ 
 | |   / _ \| |_| |_ / _ \/ _ \  / _` |/ _` |/ _` | |/ __| __|
 | |__| (_) |  _|  _|  __/  __/ | (_| | (_| | (_| | | (__| |_ 
  \____\___/|_| |_|  \___|\___|  \__,_|\__,_|\__,_|_|\___|\__|
"""

def typewriter(text):
    for char in (text):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0001)


os.system('cls')
typewriter(introtext)
time.sleep(0.5)
os.system('cls')
typewriter(desc1)
time.sleep(0.5)
os.system('cls')
typewriter(desc2)
time.sleep(0.5)
os.system('cls')
typewriter(desc3)
os.system(3)
os.system('cls')