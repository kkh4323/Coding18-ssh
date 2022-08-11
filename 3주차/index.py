import use_selenium as us # use_selenium.py를 땡겨옴(라이브러리 아님!)
import elem_selectors as es # elem_selectors.py를 땡겨옴(라이브러리 아님!)
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

target_url = "https://coupang.com"

def get_rocket_prod_list(): # 로켓 배송 상품리스트 가져오기
    driver = us.make_web_driver()
    driver.get(target_url)
    time.sleep(1) # 프로세스 일시 정지. 웹 로딩 시간 때문인듯.
    driver.find_element(By.CSS_SELECTOR, es.INPUT_SEARCH_SELECTOR).send_keys("사무용 의자", Keys.ENTER)
    page_html = BeautifulSoup(driver.page_source, 'html.parser')
    prod_page = page_html.select_one(es.PROD_LIST_SELECTOR)
    prod_all_items = prod_page.select(es.PROD_ITEM_SELECTOR)

    rocket_prod_list = []
    for prod in prod_all_items:
        is_rocket = prod.get("data-is-rocket") #[로켓 배송] 태그가 있는 상품만 구분
        if is_rocket == 'true':
            prod_name = prod.select_one("div.descriptions-inner div.name").text
            print(prod_name.strip()) # strip()을 통해서 텍스트 앞뒤의 여백 제거
            rocket_prod_list.append(prod)
    return rocket_prod_list

get_rocket_prod_list()


