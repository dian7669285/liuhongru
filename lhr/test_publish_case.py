#coding=utf-8
from selenium import webdriver
import unittest, time
from xml.dom import minidom
from public.base_page import *
from public.login_page import LoginPage
from public.publish_page import PublishPage

from selenium.webdriver.common.action_chains import ActionChains

class PublishCase(unittest.TestCase):

	def setUp(self):
		self.dr = webdriver.Firefox()
		self.dr.maximize_window()
		self.dr.implicitly_wait(30)
		self.base_url = "http://www.lawcheck.com.cn/lawCheck/login"
		self.verificationErrors = []
		
#正确的用户名和密码登录
	def test_publish_succeed_1(self):
		dr = self.dr
		dr.get(self.base_url)
		#实例化登陆页
		lp = LoginPage(dr)
		#调用登陆函数
		lp.login("18810202015","111111")
		time.sleep(3)
		self.dr.get("http://www.lawcheck.com.cn/lawCheck/lawCase/casepubwleft?issueType=0")
		pc = PublishPage(dr)
		pc.publish_case(u"刘红茹",u"刘红茹","100000","10000")
		time.sleep(8)
		#调用退出函数
		lp.logout(dr)

#字符限制验证
	def test_publish_failed_2(self):
		dr = self.dr	
		dom = minidom.parse('publish_data.xml')
		root = dom.documentElement
		publishs = root.getElementsByTagName('publish')
		for pub in publishs:
			print pub
			client = pub.getAttribute("client")
			case_content = pub.getAttribute("case_content")
			agent_place = pub.getAttribute("agent_place")
			casecost_place = pub.getAttribute("casecost_place")
			error_msg = pub.firstChild.data
			print error_msg
			dr.get(self.base_url)
			lp = LoginPage(dr)
			#调用登陆函数
			lp.login("18810202015","111111")
			self.dr.get("http://www.lawcheck.com.cn/lawCheck/lawCase/casepubwleft?issueType=0")
			pc = PublishPage(dr)
			pc.publish_case(client,case_content,agent_place,casecost_place)
			text = dr.switch_to_alert().text
			print text
			time.sleep(2)
			self.assertEqual(text,error_msg)
			time.sleep(2)
			dr.switch_to_alert().accept()
			#调用退出函数
			time.sleep(8)
			lp.logout(dr)


	def tearDown(self):
		self.dr.quit()
		self.assertEqual([],self.verificationErrors)

if __name__ == "__main__":
	unittest.main()


