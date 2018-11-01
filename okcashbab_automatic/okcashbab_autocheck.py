from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 클래스 선언
class ShoppingOnInternet():
    def __init__(self):
        self.browser = input("> Which browser do you want? ")

    # WebDriver Browser 가져오기
    def get_browser(self):
        while True:
            if self.browser in ("i",):
                self.driver = webdriver.ie()
                break
            elif self.browser in ("c"):
                chrome_opt = Options()
                chrome_opt.add_argument("--disable-infobars")
                chrome_opt.add_argument("--disable-popup-blocking")
                self.driver = webdriver.Chrome(chrome_options = chrome_opt)
                break
            elif self.browser in ("f"):
                self.driver = webdriver.Firefox()
            else:
                self.browser = input("다시")
                continue

    # 11번가 이동
    def invoke_browser(self):
        url = "http://www.okcashbag.com/"
        self.driver.get(url)
        # self.driver.maximize_window()
        self.driver.save_screenshot('1_browser_on.png')
        try:
            print('> try ~ except')
        except "G마켓 - 쇼핑을 다 담다." not in self.driver.title:
            f = open('exceptions.txt', 'rw')
            f.write('Not exect title in driver.title\n')
            f.close()

    # 로그인 하기
    def login_to_homepage(self):
        # 로그인 정보 입력
        id = "kikibu"
        pw = "cktnsdl88"
        xpaths = {'id': "//input[@name='id']", 'pw': "//input[@name='pwd']"}

        # < 로그인하기 >
        # 1. 로그인 창 열기
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('gnbLogin').click()

        # 2. 로그인 정보 넣기
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('loginname').send_keys(id)
        self.driver.find_element_by_id('passwd').send_keys(pw)
        self.driver.save_screenshot('2_login_screen.png')
        self.driver.implicitly_wait(1)

        # 3. 로그인 버튼 클릭
        self.driver.find_element_by_xpath("//*[@id='memLogin']/div/input").click()


    # 출석체크
    def attendancecheck(self):
        # 출석체크 URL이동
        url = "http://www.11st.co.kr/browsing/MallPlanDetail.tmall?method=getMallPlanDetail&planDisplayNumber=935566"
        


# TC 구동하기
if __name__ == "__main__":
    shopping = ShoppingOnInternet()

    shopping.get_browser()
    shopping.invoke_browser()
    shopping.login_to_homepage()
    # shopping.buy_goods()

    # shopping.tear_down()