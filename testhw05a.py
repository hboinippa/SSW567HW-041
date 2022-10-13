import json
import unittest
import unittest.mock
from unittest.mock import patch
from unittest import mock
from unittest.mock import Mock
#from hw05a import getCommitnum, getUserRepos
from GITHUBAPI import githubapi

class TestHw04a(unittest.TestCase):
        
    @patch("GITHUBAPI.githubapi")
    #@patch.object(, "fetch_user_repo")
    def test_fetch_user_repo_mock_api(self, mock_fetch_user_repo):
        response_file = open('./response_fetch_user_repo.json')        
        repo_call_response = json.load(response_file)
        #mock_fetch_user_repo.return_value = Mock(status_code = 200)
        mock_fetch_user_repo.return_value = True
       # mock_fetch_user_repo.return_value.json =json.loads(json.dumps(repo_call_response))
        response = githubapi('Monicaprojects21')
        #print(response)
        self.assertEqual(response,True)
        response_file.close()
       


        
if __name__ == '_main_':
    print('Running unit tests')
    unittest.main(exit=False)