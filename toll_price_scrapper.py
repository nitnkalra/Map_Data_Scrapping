from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import pandas as pd
import numpy as np
import time

while True:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options)
    driver.get('https://www.expresslanes.com/map-your-trip')

    direction = driver.find_element(By.XPATH, '//*[@id="DirectionSelect"]')
    direction.click()
    select_dd= Select(direction)

    entry_data_list = []

    for i in range(1,3):
        select_dd.select_by_index(i)
        direction_data = select_dd.first_selected_option.text
        
        entry = driver.find_element(By.XPATH, '//*[@id="EntrySelect"]')
        entry.click()
        entry_dd = Select(entry)
        entry_options = entry_dd.options
        
        exit = driver.find_element(By.XPATH, '//*[@id="ExitSelect"]')
        exit_dd = Select(exit)

        for entry_index in range(1, len(entry_options)):
            entry_dd.select_by_index(entry_index)
            entry_data = entry_dd.first_selected_option.text

            exit_options = exit_dd.options

            for exit_index in range(1, len(exit_options)):
                exit_dd.select_by_index(exit_index)
                exit_data = exit_dd.first_selected_option.text

                route_button = driver.find_element(By.XPATH, '//*[@id="ViewRouteButton"]')
                route_button.click()
                time.sleep(2)

                #WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="FormStep5"]')))
                data = driver.find_element(By.XPATH, '//*[@id="FormStep5"]')
                f_data = data.text.split('\n')
                price = [element for element in f_data if '$' in element]
                if len(price)>0:
                    toll_price = price[0]

                else:
                    toll_price ='nan'
                #toll_price = next((element for element in f_data if '$' in element), np.nan)

                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                entry_data_list.append({'Direction': direction_data,
                                        'Entry': entry_data,
                                        'Exit': exit_data,
                                        'Toll Price': toll_price,
                                        'Timestamp': current_time})

    driver.quit()
    df = pd.DataFrame(entry_data_list)
    filename= "data_" + datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+"_.csv"
    df.to_csv(filename, index=False)
    print(f"file {filename} saved succesfully ")
    
    time.sleep(1800)
    
