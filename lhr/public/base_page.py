#coding=utf-8
from selenium import webdriver
import time,os
from selenium.webdriver.support.ui import Select

class BasePage:
	url = None
	dr = None
	domain =None

	def __init__(self,dr):
		self.domain ='http://www.lawcheck.com.cn/lawCheck/login'
		self.dr = dr

		
	def by_id(self, the_id):
		return self.dr.find_element_by_id(the_id)

	def by_name(self, the_name):
		return self.dr.find_element_by_name(the_name)

	def by_link(self, link_name):
		return self.dr.find_element_by_link_text(link_name)

	def by_class(self, the_class_name):
		return self.dr.find_element_by_class_name(the_class_name)

	def by_css(self, css):
		return self.dr.find_element_by_css_selector(css)

	def by_xpath(self, xpath):
		return self.dr.find_element_by_xpath(xpath)

	def js(self, js_text):
		return self.dr.execute_script(js_text)

	def jquery(self,jq_text):
		return self.dr.execute_script(jq_text)

	def input_address(self,province,city,distric):
		Select(self.by_id("casepub_address_province")).select_by_value(province)
		Select(self.by_id("casepub_address_city")).select_by_value(city)
		Select(self.by_id("casepub_address_distric")).select_by_value(distric)

	#案由
	def case_cause(self,first,second,third):
		Select(self.by_id("firstSelect")).select_by_value(first)
		self.js("changeSubLevel(2,'100000')")
		time.sleep(2)
		Select(self.by_id("secondSelect")).select_by_value(second)
		self.js("changeSubLevel(3,'100005')")
		time.sleep(2)
		Select(self.by_id("thirdSelect")).select_by_value(third)

	#在律师进行中列表中循环找案件
	def loop_list(self):
		jxz_list = self.by_id("inprocesscaselist")
		case_lists=jxz_list.find_elements_by_tag_name("div")
		for case in case_lists:
			case_number =self.by_css("#inprocesscaselist > div:nth-child(1) > div.lmb_bottom.clearfix > div.lmb_bottom_left > span").text
			print case_number
			if case_number == u"2016(民)第3416号":
				self.by_id("info0").click()
				break
			else:
				print u"没找到案件" 

	#在用户循环列表中找案件
	def user_loop_list(self):
		jxz_list = self.by_id("inprocesscaselist")
		case_lists=jxz_list.find_elements_by_tag_name("div")
		for case in case_lists:
			case_number =self.by_css("#inprocesscaselist > div:nth-child(1) > div.lmb_bottom.clearfix > div.lmb_bottom_left > span").text
			print case_number
			if case_number == u"2016(民)第3408号":
				self.by_id("lawcasedetails0").click()
				break
			else:
				print u"没找到案件"
