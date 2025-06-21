from lib.solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckoutSolution:

    def test_multiple_basket_cases(self):
        basket = CheckoutSolution()

        #test indv items
        assert basket.checkout("A") == 50
        assert basket.checkout("B") == 30
        assert basket.checkout("C") == 20
        assert basket.checkout("D") == 15

        #test A offers
        assert basket.checkout("AAA") == 130
        assert basket.checkout("AAAA") == 180
        assert basket.checkout("AAAAA") == 230
        assert basket.checkout("AAAAAA") == 260

        #test B offers
        assert basket.checkout("BB") == 45
        assert basket.checkout("BBB") == 75

        #test sum
        assert basket.checkout("ABCD") == 50 + 30 + 20 + 15
        #test two offers
        assert basket.checkout("AAABBCD") == 130 + 45 + 20 + 15