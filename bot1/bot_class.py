import bot1.constans as constans
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from bot1.item import item as  item_module
import pandas as pd

class bot(webdriver.Chrome):
    def __init__(self, driver_path='../../chromedriver.exe'):
        self.driver_path = driver_path
        super(bot,self).__init__()
        self.implicitly_wait(10)
        self.maximize_window()


    def land_first_page(self):
        self.get(constans.BASE_URL)

    def refresh(self):
        return super().refresh()

    def report_items(self):
        items = []
        elements = self.find_elements(By.CLASS_NAME, 'list_product_a')
        for item in elements:
            arr = []
            alts = item.find_elements(By.CLASS_NAME, "list_product_icons")
            arr.append(item.text)
            for alt in alts :
                arr.append(alt.get_attribute('alt'))
            items.append(item_module(arr))
            
        # for item in items:
        #     print(item)
        self.save_as_csv(items)
        
    def save_as_csv(self,items):
        file_url = constans.save_file_url
        data = [item.to_dict() for item in items]
        df = pd.DataFrame(data)
        df.to_csv(file_url, index=False)











    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.quit()
