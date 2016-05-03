#coding=utf-8
from selenium import webdriver
import unittest, time
from xml.dom import minidom
from public.base_page import *
from public.login_page import LoginPage
from public.lawyer_pick_case import LawyerPickCase

from selenium.webdriver.common.action_chains import ActionChains

class LawyerIntake(unittest.TestCase):

	def setUp(self):
		self.dr = webdriver.Firefox()
		self.dr.maximize_window()
		self.dr.implicitly_wait(30)
		self.base_url = "http://www.lawcheck.com.cn/lawCheck/login"
		self.verificationErrors = []
		
#律师申请接案
	def test_lawyer_intake_case(self):
		dr = self.dr
		dr.get(self.base_url)
		lp = LoginPage(dr)
		lp.login("13292903983","111111")
		time.sleep(2)
		lpc = LawyerPickCase(dr)
		lpc.lawyer_intake_case()
		time.sleep(2)
		lp.logout(dr)




	def tearDown(self):
		self.dr.quit()
		self.assertEqual([],self.verificationErrors)

if __name__ == "__main__":
	unittest.main()


