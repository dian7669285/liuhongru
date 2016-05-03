#coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains
import time,os
from base_page import BasePage
from selenium.webdriver.support.ui import Select

class PublishPage(BasePage):
	
#委托人
	def client(self):
		return self.by_class('wm_inpu')
#起诉地点
	def area(self):  
		return self.input_address("11","1105","110505")
#案件描述
	def case_content(self): 
		return self.by_id('caseContent')

#代理费
	def agent_place(self):
		return self.by_id("agencyUser")

#诉讼标的额
	def casecost_place(self):
		return self.by_id("caseCostUser")

#上传附件
	def upload(self):
		return self.by_class("sc    ")

#指定律师
	def appoint_lawer(self):
		return self.by_class("zdlsbtn")
#填写律师真实姓名

	def realname(self):
		return self.by_id("realName")

#搜索按钮

	def find(self):
		return self.by_id("searchLawyer")
#指定按钮

	def appoint_btn(self):
		return self.by_class("wm_ly_zdtbtn")

#发布
	def pub_case_btn(self):
		return self.by_id("case_pub")

#发布案件
	def publish_case(self,client,case_content,agent_place,casecost_place):
		self.client().clear()
		self.client().send_keys(client)
		time.sleep(3)
		self.area()
		self.case_content().clear()
		self.case_content().send_keys(case_content)
		time.sleep(3)
		self.agent_place().clear()
		self.agent_place().send_keys(agent_place)
		time.sleep(3)
		self.casecost_place().clear()
		self.casecost_place().send_keys(casecost_place)
		time.sleep(3)
		#self.upload().click()
		#os.system("D:\\check\\testcase\\public\\upfile.exe")
		#self.appoint_lawer().click()
		#self.realname().send_keys(u"唐先婷")
		#self.find().click()
		#time.sleep(3)
		#self.appoint_btn().click()
		self.pub_case_btn().click()
		time.sleep(3)


