#coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains
import time,os
from base_page import BasePage
from selenium.webdriver.support.ui import Select

class LawyerPickCase(BasePage):
	
#案件委托按钮
	def case_entrust(self):
		return self.by_link(u"案件委托")

#查看详情按钮
	def see_details(self): 
		return self.by_link(u"查看详情")

#申请结案按钮
	def apply_case(self):
		return self.by_class("sqja")

#描述输入框
	def intake(self):
		return self.by_id("description")

#确认接案
	def confirm_intake(self):
		return self.by_class("red_btn")	

#律师申请接案操作步骤
	def lawyer_intake_case(self):
		self.case_entrust().click()
		time.sleep(2)
		jxz_windows = self.dr.current_window_handle
		table = self.by_xpath("//*[@id='caseEntrust']")
		trs = table.find_elements_by_tag_name("tr")
		for tr in trs:
			print tr.text
			name = tr.find_element_by_xpath("//*[@id='zhtai']/a").text
			print name
			if name == u"刘红茹":
				self.see_details().click()
				break
			else:
				print u"没有找到此案件"
		time.sleep(3)
		all_handles = self.dr.window_handles
		for handle in all_handles:
			if handle != jxz_windows:
				self.dr.switch_to.window(handle)
				break
			else:
				print "未找到窗口！"
		self.apply_case().click()
		self.intake().send_keys(u"我有能力接受你的案件")
		self.confirm_intake().click()
		self.dr.switch_to_alert().accept()
