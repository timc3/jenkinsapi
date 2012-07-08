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
        from jenkinsapi.jenkins import Jenkins
        log.info(repr(Jenkins))
    
    def testImportMainModules(self):
        import jenkinsapi.jenkins
        import jenkinsapi.job
        import jenkinsapi.artifact
        import jenkinsapi.node
        import jenkinsapi.fingerprint
        import jenkinsapi.build
        import jenkinsapi.result
        import jenkinsapi.view
        
if __name__ == "__main++":
    unittest.main()