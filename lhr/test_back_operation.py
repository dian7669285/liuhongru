#coding=utf-8
from selenium import webdriver
import unittest, time
from xml.dom import minidom
from public.base_page import *
from public.login_page import LoginPage
from public.back_login import BackPage

from selenium.webdriver.common.action_chains import ActionChains

class BackOperation(unittest.TestCase):

	def setUp(self):
		self.dr = webdriver.Firefox()
		self.dr.maximize_window()
		self.dr.implicitly_wait(30)
		self.base_url = "http://www.testlawmanager.com/lawManager/login.html"
		self.verificationErrors = []
		
#登录后台审核案件
	def test_back_review(self):
		dr = self.dr
		dr.get(self.base_url)
		#实例化登陆页
		bp = BackPage(dr)
		#调用登陆函数
		bp.back_login("dba","123456")
		time.sleep(3)
		bp.review_case()
		time.sleep(3)
		bp.back_logout(dr)

#后台审核代理费
	def test_back_agent_review(self):
		dr = self.dr
		dr.get(self.base_url)
		#实例化登陆页
		bp = BackPage(dr)
		#调用登陆函数
		bp.back_login("dba","123456")
		time.sleep(3)
		bp.revier_pass()
		time.sleep(3)
		bp.back_logout(dr)


	def tearDown(self):
		self.dr.quit()
		self.assertEqual([],self.verificationErrors)

if __name__ == "__main__":
	unittest.main()


