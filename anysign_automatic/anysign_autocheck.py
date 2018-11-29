from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

# 시리얼번호
serial = '440C7E'
# 패스워드
password = 'qaws1234!@'

# 클래스 선언
class AnysignforPC():
    def __init__(self):
        # self.browser = input("> Which browser do you want? ")
        self.browser = ("c")

    # WebDriver Browser 가져오기
    def get_browser(self):
        while True:
            if self.browser in ("i"):
                self.driver = webdriver.Ie()
                break
            elif self.browser in ("c"):
                chrome_opt = Options()
                chrome_opt.add_argument("--disable-infobars")
                chrome_opt.add_argument("--disable-popup-blocking")
                self.driver = webdriver.Chrome(chrome_options=chrome_opt)
                break
            elif self.browser in ("f"):
                self.driver = webdriver.Firefox()
                break
            else:
                self.browser = input("다시입력 : ")
                continue

    # AnySign 접속
    def invoke_browser(self):
        self.driver.get('https://reaver.softforum.com/XecureDemo/up/qa_anySign/test/')
        time.sleep(1)

    # AnySign4PC 설정
    def pc_set(self):
        self.driver.find_element_by_id('Enable_AnySignLoad').click()
        time.sleep(1)
        self.driver.find_element_by_id('Enable_AnySignLite').click()
        self.driver.find_element_by_id('Enable_XecureKeyPadHTML5').click()
        # self.driver.find_element_by_id('Enable_XecureFreeSign').click()

    # 인증서 발급
    # 17.CMP
    def cmp(self):
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table[10]/tbody/tr[2]/td[3]/table/tbody/tr[2]/td[1]/button").click()
        self.driver.find_element_by_xpath('//*[@id="public_type"]/option[3]').click()
        time.sleep(1)
        # 인증기관 종류 개인 - 보험용 선택
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table[10]/tbody/tr[2]/td[3]/table/tbody/tr[2]/td[2]/button").click()
        time.sleep(2)
        # 인증서 발급 클릭
        self.driver.find_element_by_id('xwup_ok').click()
        time.sleep(2)
        # 패스워드 입력
        self.driver.find_element_by_id("xwup_savepasswd_tek_input1").send_keys(password)
        self.driver.find_element_by_id("xwup_savepasswd_tek_input2").send_keys(password)
        time.sleep(1)
        self.driver.find_element_by_id('xwup_ok').click()
        time.sleep(3)
        self.driver.save_screenshot('17.CMP.png')

    # 인증서 전자서명
    # 5. SignDataCMS
    def signdatacms(self):
        # 초기 셋팅
        anysign.invoke_browser()
        anysign.pc_set()
        # 출력 값을 Base64로
        self.driver.find_element_by_xpath('//*[@id="form_SignDataCMS"]/table/tbody/tr[4]/td[2]/input[4]').click()
        self.driver.find_element_by_xpath('//*[@id="form_SignDataCMS"]/table/tbody/tr[4]/td[2]/input[5]').click()
        # AnySign.SignDataCMS 클릭
        self.driver.find_element_by_xpath('//*[@id="form_SignDataCMS"]/table/tbody/tr[7]/td[2]/input[1]').click()
        time.sleep(2)
        self.driver.find_element_by_id('xwup_ok').click()
        time.sleep(2)
        # 패스워드 입력
        self.driver.find_element_by_id("xwup_certselect_tek_input1").send_keys(password)
        self.driver.find_element_by_id('xwup_OkButton').click()
        time.sleep(1)
        # 서버로 전송
        self.driver.find_element_by_xpath('//*[@id="form_SignDataCMS"]/table/tbody/tr[8]/td[2]/button[2]').click()
        time.sleep(1)
        self.driver.save_screenshot('5.SignDataCMS_Base64.png')
        result = self.driver.find_element_by_xpath("/html").text
        # print(result.text)
        search = "전자서명됩니다."
        if search in result:
            print("5.SignDataCMS_Base64 : PASS")
        else:
            print("5.SignDataCMS_Base64 : FAIL")

        # 초기 셋팅
        anysign.invoke_browser()
        anysign.pc_set()
        # 서명 시간 추가 (SignedAttributes)
        # AnySign.SignDataCMS 클릭
        self.driver.find_element_by_xpath('//*[@id="form_SignDataCMS"]/table/tbody/tr[7]/td[2]/input[1]').click()
        time.sleep(2)
        self.driver.find_element_by_id('xwup_ok').click()
        time.sleep(2)
        # 패스워드 입력
        self.driver.find_element_by_id("xwup_certselect_tek_input1").send_keys(password)
        self.driver.find_element_by_id('xwup_OkButton').click()
        time.sleep(1)
        # 서버로 전송
        self.driver.find_element_by_xpath('//*[@id="form_SignDataCMS"]/table/tbody/tr[8]/td[2]/button[2]').click()
        time.sleep(1)
        self.driver.save_screenshot('5.SignDataCMS_SignedAttributes.png')
        result = self.driver.find_element_by_xpath("/html").text
        # print(result.text)
        search = "전자서명됩니다."
        if search in result:
            print("5.SignDataCMS_SignedAttributes : PASS")
        else:
            print("5.SignDataCMS_SignedAttributes : FAIL")

    # 6. SignDataCMSWithHTMLEx
    def signdataserial(self):
        # 초기 셋팅
        anysign.invoke_browser()
        anysign.pc_set()
        #시리얼번호 입력
        # self.driver.find_element_by_name("aSerial").send_keys(serial)
        self.driver.find_element_by_xpath('//*[@id="form_SignDataCMSWithSerial"]/table/tbody/tr[3]/td[2]/input').send_keys(serial)
        # AnySign.SignDataCMS 클릭
        self.driver.find_element_by_xpath('//*[@id="form_SignDataCMSWithSerial"]/table/tbody/tr[9]/td[2]/input[1]').click()
        time.sleep(2)
        # 패스워드 입력
        self.driver.find_element_by_id("xwup_certselect_tek_input1").send_keys(password)
        time.sleep(1)
        self.driver.find_element_by_id('xwup_OkButton').click()
        time.sleep(1)
        # 서버에 확인
        # self.driver.find_element_by_xpath('//*[@id="form_SignDataCMS"]/table/tbody/tr[8]/td[2]/button[1]').click()
        # time.sleep(1)
        # self.driver.find_element_by_xpath('//*[@id="form_SignDataCMS"]/table/tbody/tr[8]/td[2]/button[1]').send_keys(Keys.ENTER)
        # 서버로 전송
        self.driver.find_element_by_xpath('//*[@id="form_SignDataCMSWithSerial"]/table/tbody/tr[11]/td[2]/button[2]').click()
        time.sleep(1)
        self.driver.save_screenshot('6.SignDataCMSWithSerial.png')
        result = self.driver.find_element_by_xpath("/html").text
        # print(result.text)
        search = "전자서명됩니다."
        if search in result:
            print("6.SignDataCMSWithHTMLEx : PASS")
        else:
            print ("6.SignDataCMSWithHTMLEx : FAIL")

    # 7. SignDataCMSWithHTMLEx
    def signdataex(self):
        # 초기 셋팅
        anysign.invoke_browser()
        anysign.pc_set()
        # AnySign.SignDataCMS 클릭
        self.driver.find_element_by_xpath('//*[@id="form_SignDataCMSWithHTMLEx"]/table/tbody/tr[9]/td[2]/input[1]').click()
        time.sleep(1)
        # 패스워드 입력
        self.driver.find_element_by_id("xwup_certselect_tek_input1").send_keys(password)
        self.driver.find_element_by_id('xwup_OkButton').click()
        time.sleep(1)
        # 서버로 전송
        self.driver.find_element_by_xpath('//*[@id="form_SignDataCMSWithHTMLEx"]/table/tbody/tr[12]/td[2]/button[2]').click()
        time.sleep(1)
        self.driver.save_screenshot('7.SignDataCMSWithHTMLEx.png')
        result = self.driver.find_element_by_xpath("/html").text
        # print(result.text)
        search = "전자서명됩니다."
        if search in result:
            print("7.SignDataCMSWithHTMLEx : PASS")
        else:
            print("7.SignDataCMSWithHTMLEx : FAIL")

    # 8. SignDataCMSWithHTMLExAndSerial
    def signdataexserial(self):
        # 초기 셋팅
        anysign.invoke_browser()
        anysign.pc_set()
        #시리얼번호 입력
        self.driver.find_element_by_xpath('//*[@id="form_SignDataCMSWithHTMLExAndSerial"]/table/tbody/tr[3]/td[2]/input').send_keys(serial)
        # AnySign.SignDataCMS 클릭
        self.driver.find_element_by_xpath('//*[@id="form_SignDataCMSWithHTMLExAndSerial"]/table/tbody/tr[11]/td[2]/input[1]').click()
        time.sleep(2)
        # 패스워드 입력
        self.driver.find_element_by_id("xwup_certselect_tek_input1").send_keys(password)
        time.sleep(1)
        self.driver.find_element_by_id('xwup_OkButton').click()
        time.sleep(1)
        # 서버로 전송
        self.driver.find_element_by_xpath('//*[@id="form_SignDataCMSWithHTMLExAndSerial"]/table/tbody/tr[14]/td[2]/button[2]').click()
        time.sleep(1)
        self.driver.save_screenshot('8.SignDataCMSWithHTMLExAndSerial.png')
        result = self.driver.find_element_by_xpath("/html").text
        # print(result.text)
        search = "전자서명됩니다."
        if search in result:
            print("8.SignDataCMSWithHTMLExAndSerial : PASS")
        else:
            print("8.SignDataCMSWithHTMLExAndSerial : FAIL")

    # 14. EnvelopeData
    def envelope(self):
        # 초기 셋팅
        anysign.invoke_browser()
        anysign.pc_set()
        # AnySign.SignDataCMS 클릭
        self.driver.find_element_by_xpath('//*[@id="form_EnvelopData"]/table/tbody/tr[10]/td[2]/input[1]').click()
        time.sleep(2)
        self.driver.find_element_by_id('xwup_OkButton').click()
        time.sleep(1)
        self.driver.save_screenshot('14.EnvelopeData.png')
    # 15. DeEnvelopeData
        self.driver.find_element_by_xpath('//*[@id="form_DeEnvelopData"]/table/tbody/tr[7]/td[2]/input[1]').click()
        time.sleep(1)
        # 패스워드 입력
        self.driver.find_element_by_id("xwup_certselect_tek_input1").send_keys(password)
        self.driver.find_element_by_id('xwup_OkButton').click()
        time.sleep(1)

        # 결과 화면 element 의 y 좌표까지 scroll
        default_x_position = 0
        elem_y_position = self.driver.find_element_by_xpath('//*[@id="15"]')
        y_position_of_elem = elem_y_position.location['y']
        self.driver.execute_script("window.scrollTo({0}, {1});".format(default_x_position, y_position_of_elem))
        self.driver.save_screenshot('15.DeEnvelopeData.png')
        # result = self.driver.find_element_by_xpath("//*[@id='form_DeEnvelopData']/table/tbody/tr[8]/td[2]/textarea").text
        # print(result)

# TC 구동하기
if __name__ == "__main__":
    anysign = AnysignforPC()

    anysign.get_browser()
    anysign.invoke_browser()
    anysign.pc_set()
    anysign.cmp()
    anysign.signdatacms()
    anysign.signdataserial()
    anysign.signdataex()
    anysign.signdataexserial()
    anysign.envelope()