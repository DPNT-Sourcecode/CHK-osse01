from lib.solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckoutSolution:

    def test_multiple_basket_cases(self):
        basket = CheckoutSolution()

        assert basket.checkout("A") == 50