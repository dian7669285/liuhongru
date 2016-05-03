#coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains
import time,os
from base_page import BasePage
from selenium.webdriver.support.ui import Select
from pyquery import PyQuery as pq
from lxml import etree

class PerfectInformation(BasePage):
	
#个人中心
	def grzx(self):
		return self.by_class("grzx_2")

#进行中案件
	def jxz_case(self): 
		return self.by_link(u"进行中案件")
#联系人姓名
	def touch_name(self):
		return self.by_id("touchName")

#联系人电话
	def touch_phone(self):
		return self.by_id("touchMobile")

#被告人姓名
	def beigao(self):
		return self.by_id("beigaorenName")

#保存
	def save_btn(self):
		return self.by_xpath("//*[@id='isShow']/div/div/input")
#完善信息
	def perfect_information(self):
		self.grzx().click()
		time.sleep(2)
		self.jxz_case().click()
		jxz_windows = self.dr.current_window_handle
		self.loop_list()
		time.sleep(2)
		all_handles = self.dr.window_handles
		for handle in all_handles:
			if handle != jxz_windows:
				self.dr.switch_to.window(handle)
				break
			else:
				print "未找到窗口！"
		self.touch_name().send_keys(u"张柏芝")
		self.touch_phone().send_keys(u"18810202015")
		self.beigao().send_keys(u"谢霆锋")
		self.save_btn().click()
#支付代理费页面按钮

	def agent_btn(self):
		return self.by_class("an_1")
#上传按钮
	def up_btn(self,dr):
		up = self.by_id("dailifeiUploadBtn")
		ActionChains(dr).move_to_element(up).perform()
		jquery = '$("input[name=fileName]").click()'
		self.jquery(jquery)

#代理费总金额
	def agent_free(self):
		return self.by_id("dailifeiAgencyNum")

#代理费支付金额
	def agent_pay_free(self):
		return self.by_id("dailifeiAgencyPayNum")
#代理费说明
	def agent_description(self):
		return self.by_id("dailifeiExplain")
#确定按钮
	def confirm_btn(self):
		return self.by_id("dailifeiConfirm")
#取消按钮
	def undo_btn(self):
		return self.by_id("dailifeiCancel")
#代理费
	def lawyer_agent_free(self,dr):
		self.grzx().click()
		time.sleep(2)
		self.jxz_case().click()
		jxz_windows = self.dr.current_window_handle
		print jxz_windows
		time.sleep(2)
		self.loop_list()
		time.sleep(2)
		all_handles = self.dr.window_handles
		for handle in all_handles:
			if handle != jxz_windows:
				self.dr.switch_to.window(handle)
				break
			else:
				print "未找到窗口！"
		time.sleep(2)
		self.agent_btn().click()
		time.sleep(2)
		self.up_btn(dr)
		time.sleep(3)
		os.system("E:\\lhr\\upfile.exe")

		time.sleep(3)

		self.agent_free().send_keys("10000")
		self.agent_pay_free().send_keys("10000")
		self.agent_description().send_keys(u"哈哈哈哈哈哈哈哈哈哈哈哈")
		self.confirm_btn().click()
		self.dr.switch_to_alert().accept()