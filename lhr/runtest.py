#coding=utf-8
import unittest
import test_publish_case
import test_login
import time
import test_back_operation
import test_lawyer_intake
import test_user_appoint_lawyer
import test_perfect_information
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.support.ui import Select

#test_dir= './'
#discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
def all_test():
	suites = [] 
	suite = unittest.TestSuite()
	#前台登录
	#suite.addTest(test_login.TestLogin("test_login"))
	#发布案件
	#suite.addTest(test_publish_case.PublishCase("test_publish_succeed_1"))
	#后台审核案件通过
	#suite.addTest(test_back_operation.BackOperation("test_back_review"))
	#律师申请接案
	#suite.addTest(test_lawyer_intake.LawyerIntake("test_lawyer_intake_case"))
	#用户指定律师
	#suite.addTest(test_user_appoint_lawyer.UserAppoint("test_user_appoint_lawyer"))
	#律师完善信息
	#suite.addTest(test_perfect_information.PerfectInformat("test_perfect_information"))
	#支付代理费
	#suite.addTest(test_perfect_information.PerfectInformat("test_lawyer_pay_agent_free"))
	#后台审核代理费
	suite.addTest(test_back_operation.BackOperation("test_back_agent_review"))
	suites.append(suite)
	return suites

if __name__ == '__main__':
	alltestcase = all_test()
	now_time=time.strftime('%Y-%m-%d %H-%M-%S',time.localtime())
	filename = './report/'+now_time+'result.html'
	fp = open(filename,'wb')
	runner = HTMLTestRunner(stream=fp,
	title = u'测试报告',
	description= u'用例执行情况：')

	runner = unittest.TextTestRunner()
	runner.run(alltestcase[0])
	fp.close()