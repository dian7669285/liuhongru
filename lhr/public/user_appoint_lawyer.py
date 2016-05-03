#coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains
import time,os
from base_page import BasePage
from selenium.webdriver.support.ui import Select

class UserAppointLawyer(BasePage):
	
#个人中心
	def grzx(self):
		return self.by_class("grzx_2")

#案件详情
	def case_details(self): 
		return self.by_id("lawcasedetails0")

#指定他按钮
	def appoint_btn(self):
		return self.by_class("zhig")
#确认
	def comm(self):
		return self.by_id("qdqdqd")

#用户指定律师
	def user_appoint_lawyer(self):
		self.grzx().click()
		time.sleep(2)
		jxz_windows = self.dr.current_window_handle
		self.user_loop_list()
		time.sleep(2)
		all_handles = self.dr.window_handles
		for handle in all_handles:
			if handle != jxz_windows:
				self.dr.switch_to.window(handle)
				break
			else:
				print "未找到窗口！"
		self.appoint_btn().click()
		self.comm().click()




