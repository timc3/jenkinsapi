import logging
import unittest

log = logging.getLogger(__name__)

class test_imports(unittest.TestCase):

    def testImportOne(self):
        import jenkinsapi
        log.info(repr(jenkinsapi))
            
    def testImportTwo(self):
        import jenkinsapi.jenkins
        log.info(repr(jenkinsapi.jenkins))
    
    def testImportThree(self):
        import jenkins
        log.info(repr(jenkins))
    
    def testImportFour(self):
        from jenkinsapi.jenkins import Jenkins
        log.info(repr(Jenkins))
    

if __name__ == "__main++":
    unittest.main()