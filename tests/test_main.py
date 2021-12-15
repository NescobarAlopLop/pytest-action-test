import unittest.mock
import unittest
import os

import main


class MainTestCase(
    unittest.TestCase,
):
    @unittest.mock.patch.dict(
        os.environ,
        {
            'INPUT_PATH': 'pytest-coverage.txt',
            'ONLY_CHANGED': 'True',
        },
    )
    def test_main(
        self,
    ):
        pytest_cov_file_path = os.environ['INPUT_PATH']
        show_only_changed_files = os.environ['ONLY_CHANGED']