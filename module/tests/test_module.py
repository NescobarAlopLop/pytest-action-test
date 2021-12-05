import unittest


from .. import module


class TestModule(
    unittest.TestCase,
):
    def test_sum(
        self,
    ):
        self.assertEqual(
            first=3,
            second=module.sum(
                a=1,
                b=2,
            )
        )

    def test_square(
        self,
    ):
        self.assertEqual(
            first=9,
            second=module.square(
                a=3,
                power=2,
            )
        )
        # just to change a file
