#coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains
import time
from base_page import BasePage

class LoginPage(BasePage):

	def username(self):
		return self.by_id('username')
#密码输入框
	def password(self):  
		return self.by_id('password')
#登录按钮
	def login_btn(self): 
		return self.by_id('submit_button')

#输入账号密码点击登录
	def login(self,username,password):
		self.username().send_keys(username)
		self.password().send_keys(password)
		self.login_btn().click()
#清除输入过的用户名或密码
	def login_and_clear_username(self, username, password):
		self.username().clear()
		self.username().send_keys(username)
		self.password().clear()
		self.password().send_keys(password)
		self.login_btn().click()
	
#退出函数
	def logout(self,dr):
		grzx = self.by_class("grzx_2")
		ActionChains(dr).move_to_element(grzx).perform()
		time.sleep(3)
		exit_button = self.by_xpath("/html/body/div/div/div[2]/div/ol/a[6]/li")
		exit_button.click()
#登陆成功后的个人中心元素
	def grzx(self):
		grzx_text = self.by_class("grzx_2").text
		print grzx_text
		return grzx_text

#获取错误提示框的内容
	def error(self):
		error_text = self.by_xpath("//*[@id='error_info']/div").text
		print error_text
		return error_text


