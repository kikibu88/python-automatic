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

    # G마켓 이동
    def invoke_browser(self):
        url = "http://www.gmarket.co.kr/"
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
        id = "korbart"
        pw = "gmw22920"
        xpaths = {'id': "//input[@name='id']", 'pw':"//input[@name='pwd']"}

        # < 로그인하기 >
        # 1. 로그인 창 열기
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('css_login_box').click()

        # 2. 로그인 정보 넣기
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(xpaths['id']).send_keys(id)
        self.driver.find_element_by_xpath(xpaths['pw']).send_keys(pw)
        self.driver.save_screenshot('2_login_screen.png')
        self.driver.implicitly_wait(1)

        # 3. 로그인 버튼 클릭
        self.driver.find_element_by_css_selector("input[type=\"image\"]").click()

    # 상품 구매하기
    def buy_goods(self):
        # 1. 검색 '대통령의 말하기' -> 버튼 클릭!
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("keyword").clear()
        self.driver.find_element_by_id("keyword").send_keys(u"대통령의 말하기")
        self.driver.find_element_by_css_selector("button.button_search").click()
        self.driver.save_screenshot('3_search_results.png')
        self.driver.implicitly_wait(1)

        # 2. 검색 결과 중 상품 선택
        self.driver.find_element_by_css_selector("span.title").click()

        # 상품 상세 설명 및 구매 창이 열릴 때 새 창이 열린다! window를 새창으로 바꿔주지 않으면 element ID를 찾지 못한다.
        for windows in self.driver.window_handles:
            pass
        current_window = windows

        self.driver.switch_to_window(current_window)

        self.driver.maximize_window()
        self.driver.implicitly_wait(1)
        self.driver.save_screenshot('4_select_goods.png')

        # 3. 즉지 구매 클릭

        # 옵션 선택 버튼 element 의 y 좌표까지 scroll
        default_x_position = 0
        elem_y_position = self.driver.find_element_by_xpath('//div[@id="optOrderComb_0"]/button')
        y_position_of_elem = elem_y_position.location['y']
        self.driver.execute_script("window.scrollTo({0}, {1});".format(default_x_position, y_position_of_elem))

        # 옵션 1 선택 - 옵션 1 버튼 클릭
        option1 = self.driver.find_element_by_xpath('//div[@id="optOrderComb_0"]/button')
        option1.click()
        self.driver.implicitly_wait(1)

        # 옵션 1 선택 - 첫번째 옵션 선택
        option_choice1 = self.driver.find_element_by_xpath('//div[@id="optOrderComb_0"]/ul/li[1]')
        option_choice1.click()
        self.driver.implicitly_wait(1)

        # 옵션 2 선택 - 옵션2 버튼 클릭
        option2 = self.driver.find_element_by_xpath('//div[@id="optOrderComb_1"]/button')
        option2.click()
        self.driver.implicitly_wait(1)

        # 옵션 2 선택 - 첫번째 옵션 선택
        option_choice2 = self.driver.find_element_by_xpath('//div[@id="optOrderComb_1"]/ul/li[1]')
        option_choice2.click()
        self.driver.implicitly_wait(1)

        # 구매하기 버튼 위치까지 scroll
        y_position = self.driver.find_element_by_id("coreInsOrderBtn")
        elem_y_position = y_position.location['y']
        self.driver.execute_script("window.scrollTo({0}, {1});".format(default_x_position, elem_y_position))

        self.driver.implicitly_wait(1)
        self.driver.find_element_by_id("coreInsOrderBtn").click()
        self.driver.save_screenshot('5_select_options_and_checkout.png')

    # It;s time to say Good-bye~
    def tear_down(self):
        # 열려있는 windows 가져오기
        opened_window_list = self.driver.window_handles

        # 열려있는 모든 windows 로그아웃 후 닫기
        index = len(opened_window_list)
        while index:
            self.driver.switch_to_window(self.driver.window_handles[index-1])
            index = index - 1
            self.driver.find_element_by_xpath("//span[@class='myinfo']/a").click()
            self.driver.close()

# TC 구동하기
if __name__ == "__main__":
    shopping = ShoppingOnInternet()

    shopping.get_browser()
    shopping.invoke_browser()
    shopping.login_to_homepage()
    shopping.buy_goods()

    shopping.tear_down()