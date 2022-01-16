import unittest


from .. import module2


class TestModule(
    unittest.TestCase,
):
    def test_sum(
        self,
    ):
        self.assertEqual(
            first=3,
            second=module2.sum(
                a=1,
                b=2,
            )
        )

    def test_square(
        self,
    ):
        self.assertEqual(
            first=9,
            second=module2.square(
                a=3,
                power=2,
            )
        )
