#coding=utf-8
from selenium import webdriver
import unittest, time
from xml.dom import minidom
from public.base_page import *
from public.login_page import LoginPage
from public.lawyer_pick_case import LawyerPickCase
from public.user_appoint_lawyer import UserAppointLawyer
from public.lawyer_perfect_information import PerfectInformation

from selenium.webdriver.common.action_chains import ActionChains

class PerfectInformat(unittest.TestCase):

	def setUp(self):
		self.dr = webdriver.Firefox()
		self.dr.maximize_window()
		self.dr.implicitly_wait(30)
		self.base_url = "http://www.lawcheck.com.cn/lawCheck/login"
		self.verificationErrors = []
		
#律师完善信息
	def test_perfect_information(self):
		dr = self.dr
		dr.get(self.base_url)
		lp = LoginPage(dr)
		lp.login("13292903983","111111")
		time.sleep(2)
		pp = PerfectInformation(dr)
		pp.perfect_information()
		time.sleep(2)
		lp.logout(dr)

#律师交代理费
	def test_lawyer_pay_agent_free(self):
		dr = self.dr
		dr.get(self.base_url)
		lp = LoginPage(dr)
		lp.login("13292903983","111111")
		time.sleep(2)
		pp = PerfectInformation(dr)
		pp.lawyer_agent_free(dr)
		time.sleep(2)
		lp.logout(dr)


	def tearDown(self):
		self.dr.quit()
		self.assertEqual([],self.verificationErrors)

if __name__ == "__main__":
	unittest.main()


