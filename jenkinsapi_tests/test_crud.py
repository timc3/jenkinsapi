import random
import unittest

from jenkinsapi.jenkins import Jenkins
from jenkinsapi_tests.test_config import defaultConfig
from hamcrest import assert_that, greater_than
from string import ascii_letters


class test_crud(unittest.TestCase):
    
    def setUp(self):
        self.api = Jenkins(**defaultConfig.__dict__)
        
    def random_id(self, length=10):
        return "".join(random.choice(ascii_letters) for a in range(0,length))
        
    def testRepr(self):
        '''
        Verify that we can make a valid api object
        and that it can be used to make a string repr
        '''
        api_repr = repr(self.api)
        assert_that(len(api_repr), greater_than(0))
        
    def testCreateJob(self):
        """
        Test simple creating & deleting a job.
        """
        newjobname = "test_job_%s" % self.random_id()
        self.api.create_job(newjobname)
        assert_that( self.api.has_job(newjobname))
        self.api.delete_job(newjobname)
        assert_that(not(self.api.has_job(newjobname)))
        
    def testCheckNonExistantJob(self):
        """
        Think of a job name that most probably does not exist, and
        verify that this is indeed the case
        """
        newjobname = "test_job_%s" % self.random_id()
        assert_that(not(self.api.has_job(newjobname)))
    
if __name__ == "__main++":
    unittest.main()