from lib.solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckoutSolution:

    def test_indv_cases(self):
        basket = CheckoutSolution()

        assert basket.checkout("K") == 70
        assert basket.checkout("ABCDEFGHIJKLMNOPQRSTUVW") == 795

    def test_multiple_basket_cases(self):
        basket = CheckoutSolution()

        #neg check
        assert basket.checkout("-1") == -1

        #test indv items
        assert basket.checkout("") == 0
        assert basket.checkout("A") == 50
        assert basket.checkout("B") == 30
        assert basket.checkout("C") == 20
        assert basket.checkout("D") == 15
        assert basket.checkout("E") == 40
        assert basket.checkout("F") == 10
        assert basket.checkout("G") == 20
        assert basket.checkout("H") == 10
        assert basket.checkout("I") == 35
        assert basket.checkout("J") == 60
        assert basket.checkout("K") == 70
        assert basket.checkout("L") == 90
        assert basket.checkout("M") == 15
        assert basket.checkout("N") == 40
        assert basket.checkout("O") == 10
        assert basket.checkout("P") == 50
        assert basket.checkout("Q") == 30
        assert basket.checkout("R") == 50
        assert basket.checkout("S") == 20
        assert basket.checkout("T") == 20
        assert basket.checkout("U") == 40
        assert basket.checkout("V") == 50
        assert basket.checkout("W") == 20
        assert basket.checkout("X") == 17
        assert basket.checkout("Y") == 20
        assert basket.checkout("Z") == 21

        #test A offers
        assert basket.checkout("AAA") == 130
        assert basket.checkout("AAAA") == 180
        assert basket.checkout("AAAAA") == 200
        assert basket.checkout("AAAAAA") == 250
        assert basket.checkout("AAAAAAA") == 300

        #test B offers
        assert basket.checkout("BB") == 45
        assert basket.checkout("BBB") == 75

        #test sum
        assert basket.checkout("ABCD") == 50 + 30 + 20 + 15

        #test two offers
        assert basket.checkout("AAABBCD") == 130 + 45 + 20 + 15
        assert basket.checkout("EEAB") == 130

        #E offers
        assert basket.checkout("EEB") == 80
        assert basket.checkout("EB") == 70
        assert basket.checkout("EEBB") == 110
        assert basket.checkout("EEBBB") == 125
        assert basket.checkout("EEEEBB") == 160

        #F offers
        assert basket.checkout("F") == 10
        assert basket.checkout("FF") == 20
        assert basket.checkout("FFF") == 20
        assert basket.checkout("FFFF") == 30
        assert basket.checkout("FFFFFF") == 40

        #H offers
        assert basket.checkout("HHHHH") == 45
        assert basket.checkout("HHHHHHA") == 45 + 10 + 50
        assert basket.checkout("HHHHHHHHHHHO") == 80 + 10 + 10

        #K offers
        assert basket.checkout("KK") == 120
        assert basket.checkout("KKKK") == 300
        assert basket.checkout("KKKKA") == 350

        #N offers
        assert basket.checkout("NNNM") == 120
        assert basket.checkout("NNNMN") == 160
        assert basket.checkout("NNNNNM") == 200

        #P offers
        assert basket.checkout("PPPPP") == 200

        #Q offers
        assert basket.checkout("QQQ") == 80

        #R offers
        assert basket.checkout("RRRQ") == 150

        #U offers
        assert basket.checkout("UUUU") == 120

        #V offers
        assert basket.checkout("VV") == 90
        assert basket.checkout("VVV") == 130

        #Group offers
        assert basket.checkout("STX") == 45
        assert basket.checkout("XYZ") == 45
        assert basket.checkout("TYY") == 45
        assert basket.checkout("STXZZ") == 82
        assert basket.checkout("STXSTX") == 90
        assert basket.checkout("STXYS") == 82
        assert basket.checkout("STXSTZZ") == 107
        assert basket.checkout("K") == 70
        assert basket.checkout("ABCDEFGHIJKLMNOPQRSTUVW") == 795







