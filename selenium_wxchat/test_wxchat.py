from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBaidu:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").click()
        self.driver.find_element_by_id("kw").send_keys("霍格沃兹测试学院")
        self.driver.find_element_by_id("su").click()
        ele = self.driver.find_element_by_link_text("霍格沃兹测试学院 – 软件自动化测试开发培训_接口性能测试")
        assert ele

class TestWework:
    def test_Wework(self):
        # 复用只支持chrome浏览器
        opt = webdriver.ChromeOptions()
        # 设置debug地址
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(10)
        # 在当前页面点击通讯录
        self.driver.find_element_by_id("menu_contacts").click()
        # 获取cookie信息
        cookie = self.driver.get_cookies()
        # 把cookie存如yaml文件内
        with open("data.yaml","w",encoding="UTF-8") as f:
            yaml.dump(cookie,f)

    def test_cookies(self):
        # 实例化driver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 访问扫码登录页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        # 读取cookie
        with open("data.yaml",encoding="UTF-8") as f:
            yaml_cookie = yaml.safe_load(f)
            for cookie in yaml_cookie:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("menu_contacts").click()
        sleep(2)
        # 添加成员
        self.driver.find_element_by_link_text("添加成员").click()
        sleep(2)
        self.driver.find_element_by_id("username").send_keys("张三")
        self.driver.find_element_by_id("memberAdd_english_name").send_keys("zs")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("1234")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("18649716788")
        self.driver.find_element_by_id("memberAdd_telephone").send_keys("0597-3762145")
        self.driver.find_element_by_id("memberAdd_mail").send_keys("test@qq.com")
        self.driver.find_element_by_id("memberEdit_address").send_keys("厦门")
        self.driver.find_element_by_link_text("保存").click()
        ele = self.driver.find_elements_by_xpath('//table/tbody//td[@title="张三"]')
        assert ele

        # 删除成员
        self.driver.find_element_by_xpath('//td[@title="张三"]/preceding-sibling::td/input').click()
        self.driver.find_element_by_link_text("删除").click()
        sleep(2)
        self.driver.find_element_by_xpath('//a[@d_ck="submit"]').click()






