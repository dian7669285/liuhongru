#coding=utf-8
from selenium import webdriver
import unittest, time
from xml.dom import minidom
from public.base_page import *
from public.login_page import LoginPage

from selenium.webdriver.common.action_chains import ActionChains

class TestLogin(unittest.TestCase):

	def setUp(self):
		self.dr = webdriver.Firefox()
		self.dr.maximize_window()
		self.dr.implicitly_wait(30)
		self.base_url = "http://www.lawcheck.com.cn/lawCheck/login"
		self.verificationErrors = []
		
#正确的用户名和密码登录
	def test_login(self):
		dr = self.dr
		dr.get(self.base_url)
		#实例化登陆页
		lp = LoginPage(dr)
		#调用登陆函数
		lp.login("18810202015","111111")
		time.sleep(3)
		#登录成功后显示个人中心
		self.assertEqual(lp.grzx(),u"个人中心")
		#调用退出函数
		lp.logout(dr)

#错误的用户名和密码登录
	def test_login_failed(self):
		dr = self.dr
		dr.get(self.base_url)
		#打开xml文档
		dom = minidom.parse('login_data.xml')
		#得到文档元素对象
		root = dom.documentElement
		#获取tagname为login的元素
		logins = root.getElementsByTagName('login')
		#print logins
		for login in logins:
			print login
			#获取login标签的username属性值
			username = login.getAttribute("username")
			print username
			#获取login标签的password属性值
			password = login.getAttribute("password")
			print password
			#获取login标签对的值
			error_msg = login.firstChild.data
			print error_msg
			time.sleep(3)
			lp = LoginPage(dr)
			#调用登陆函数
			lp.login_and_clear_username(username,password)
			time.sleep(3)
			#断言提示和文件的文字一致
			self.assertEqual(lp.error(),error_msg)


	def tearDown(self):
		self.dr.quit()
		self.assertEqual([],self.verificationErrors)

if __name__ == "__main__":
	unittest.main()


