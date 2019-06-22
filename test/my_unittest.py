import unittest 
import HtmlTestRunner


REPORT_FOLDER = '/home/python_proj/Django/ci_overview/ci_overview/templates'


class MyTest(unittest.TestCase):
  

    def setUp(self):
        pass
    #清退工作
    def tearDown(self):
        pass
    #具体的测试用例，一定要以test开头
    def test_1(self):
        self.assertEqual(3, 3, "test sum fail")

    def test_2(self):
        self.assertEqual(2 , 2, "test sum fail")

    def test_3(self):
        self.assertTrue(0)

if __name__=='__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(MyTest))
    runner = HtmlTestRunner.HTMLTestRunner(output=REPORT_FOLDER,report_title="Mytest",descriptions='None',report_name='MyUnitTest')
    runner.run(suite)
