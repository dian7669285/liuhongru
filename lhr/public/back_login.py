#coding=utf-8
import time
from base_page import BasePage

class BackPage(BasePage):

	def username(self):
		return self.by_id('username')
#密码输入框
	def password(self):  
		return self.by_id('password')
#登录按钮
	def login_btn(self): 
		return self.by_xpath("//*[@class='login-button']/div/input")

#输入账号密码点击登录
	def back_login(self,username,password):
		self.username().send_keys(username)
		self.password().send_keys(password)
		time.sleep(8)
		self.login_btn().click()
#清除输入过的用户名或密码
	def login_and_clear_username(self, username, password):
		self.username().clear()
		self.username().send_keys(username)
		self.password().clear()
		self.password().send_keys(password)
		time.sleep(8)
		self.login_btn().click()
	
#退出函数
	def back_logout(self,dr):
		quit = self.by_link(u"退出")
		quit.click()
#案件委托管理菜单
	def case_manage(self):
		return self.by_link(u"案件委托管理")

#案件审核
	def case_review(self):
		return self.by_link(u"案件审核")

#审核按钮
	def review_btn(self):
		return self.by_link(u"审核")

#保存并审核通过

	def save_and_review(self):
		review_btn = self.by_xpath("//*[@class='col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main']/button[2]")
		print review_btn.text
		return review_btn

	def case_ay(self):
		return self.case_cause("100000","100005","100090")

#审核通过后，制定客服确认按钮
	def confirm_btn(self):
		return self.by_id("theComfirmButton")
#审核案件

	
	def review_case(self):
		self.case_manage().click()
		time.sleep(2)
		self.case_review().click()
		table = self.by_xpath("//*[@id='contentTable']/tbody")
		trs = table.find_elements_by_tag_name("tr")
		for tr in trs:
			print tr.text
			name = tr.find_element_by_tag_name("a").text
			print name 
			if name == u"刘红茹":
				tr.find_element_by_link_text(u"审核").click()
				break
			else:
				print u"没有找到此案件"
		time.sleep(2)
		self.case_ay()
		time.sleep(2)
		self.save_and_review().click()
		time.sleep(2)
		self.confirm_btn().click()
		self.dr.switch_to_alert().accept()

#审核代理费
	
#代理费明细
	def agent_review(self):
		return self.by_link(u"代理费明细")
#审核
	def revier_pass(self):
		self.case_manage().click()
		time.sleep(2)
		self.case_review().click()
		time.sleep(2)
		self.agent_review().click()
		table = self.by_xpath("//*[@id='contentTable']/tbody")
		trs = table.find_elements_by_tag_name("tr")
		for tr in trs:
			print tr.text
			case_num = tr.find_element_by_tag_name("a").text
			print case_num
			if case_num == u"2016(民)第3416号 ":
				self.js("confirmInfo('f7399665a622425fbb85','1','2016(民)第3416号')")
				break
			else:
				print u"没有找到此案件"

			self.by_class("btn btn-primary").click()
			self.dr.switch_to_alert().accept()
