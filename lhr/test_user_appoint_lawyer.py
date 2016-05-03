#coding=utf-8
from selenium import webdriver
import unittest, time
from xml.dom import minidom
from public.base_page import *
from public.login_page import LoginPage
from public.lawyer_pick_case import LawyerPickCase
from public.user_appoint_lawyer import UserAppointLawyer

from selenium.webdriver.common.action_chains import ActionChains

class UserAppoint(unittest.TestCase):

	def setUp(self):
		self.dr = webdriver.Firefox()
		self.dr.maximize_window()
		self.dr.implicitly_wait(30)
		self.base_url = "http://www.lawcheck.com.cn/lawCheck/login"
		self.verificationErrors = []
		
#用户指定律师
	def test_user_appoint_lawyer(self):
		dr = self.dr
		dr.get(self.base_url)
		lp = LoginPage(dr)
		lp.login("18810202015","111111")
		time.sleep(2)
		ual = UserAppointLawyer(dr)
		ual.user_appoint_lawyer()
		time.sleep(2)
		lp.logout(dr)




	def tearDown(self):
		self.dr.quit()
		self.assertEqual([],self.verificationErrors)

if __name__ == "__main__":
	unittest.main()


