from selenium import webdriver
from selenium.webdriver.chrome.service import Service
######
import chromedriver_autoinstaller # 셀레니움을 통해 크롤링, 스크래핑을 할 때 브라우저에 맞는 드라이버를 자동 설치해줌.
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0] # pc에 설치된 크롬 버전을 가져옴.

def make_web_driver(): # selenium 전용 자동화 Chrome 설정
    path = chromedriver_autoinstaller.install()                                 # 웹 드라이버가 설치되었는지 확인하고, 설치가 안되어있다면 설치해줌.
    options = webdriver.ChromeOptions()                                         # 브라우저 세팅
    options.add_argument("start-maximized")                                     # 창 최대화
    options.add_argument('--disable-blink-features=AutomationControlled')       # 자동 검색, 봇, 이것저것 걸러주는 것들을 우회함
    options.add_experimental_option("excludeSwitches", ["enable-automation"])   # 자동 검색, 봇, 이것저것 걸러주는 것들을 우회함
    options.add_experimental_option('useAutomationExtension', False)            # 자동 검색, 봇, 이것저것 걸러주는 것들을 우회함
    driver = webdriver.Chrome(options=options, service=Service(path))           # 옵션 값대로 실행. 
    driver.implicitly_wait(10)                                                  # 다음 웹 페이지 넘어올 때 최대 10초까지만 기다리라는 뜻.
                                                                                # time.sleep(10)은 무조건 10초 기다림.
                                                                                # explicitly wait도 있다. 웹 페이지 전체가 아니라 필요한 부분이 
                                                                                # 표시될 때까지만 기다려라라는 뜻.
    return driver