import unittest
class TestTemplate(unittest.TestCase):

    @classmethod
    def setUp(self):
        print "Setting up template tests"
       
    
    def testBlah(self):
        print "Testing blah"
        
        self.assertEquals(1,1,'A template testing comment')
