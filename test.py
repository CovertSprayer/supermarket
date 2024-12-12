import unittest
from store import Product, Checkout

class TestProduct(unittest.TestCase):
    def test_case_1(self):
        product = Product("C", 20)
        self.assertEqual(product.calculatePrice(3), 60)
        self.assertEqual(product.calculatePrice(1), 20)

    def test_case_2(self):
        product = Product("A", 50, {"quantity": 3, "price": 130})
        self.assertEqual(product.calculatePrice(3), 130)
        self.assertEqual(product.calculatePrice(4), 180)
        self.assertEqual(product.calculatePrice(5), 230)
        self.assertEqual(product.calculatePrice(6), 260)

class TestCheckout(unittest.TestCase):
    pricingRules = {
        "A": Product("A", 50, {"quantity": 3, "price": 130}),
        "B": Product("B", 30, {"quantity": 2, "price": 45}),
        "C": Product("C", 20),
        "D": Product("D", 15),
    }
    
    def calculate(self, inp):
        checkout = Checkout(self.pricingRules)
        for item in inp:
            checkout.scan(item)
        return checkout.calculateTotal()

    def test_case_1(self):
        total = self.calculate("")
        self.assertEqual(total, 0)

    def test_case_2(self):
        total = self.calculate("A")
        self.assertEqual(total, 50)

    def test_case_3(self):
        input = "AB"
        total = self.calculate(input)
        self.assertEqual(total, 80)
        
    def test_case_4(self):
        input = "CDBA"
        total = self.calculate(input)
        self.assertEqual(total, 115)
        
    def test_case_5(self):
        input = "AA"
        total = self.calculate(input)
        self.assertEqual(total, 100)
        
    def test_case_6(self):
        input = "AAA"
        total = self.calculate(input)
        self.assertEqual(total, 130)
        
    def test_case_7(self):
        input = "AAAA"
        total = self.calculate(input)
        self.assertEqual(total, 180)
        
    def test_case_8(self):
        input = "AAAAA"
        total = self.calculate(input)
        self.assertEqual(total, 230)
        
    def test_case_9(self):
        input = "AAAAAA"
        total = self.calculate(input)
        self.assertEqual(total, 260)
        
    def test_case_10(self):
        input = "AAAB"
        total = self.calculate(input)
        self.assertEqual(total, 160)
        
    def test_case_11(self):
        input = "AAABB"
        total = self.calculate(input)
        self.assertEqual(total, 175)
        
    def test_case_12(self):
        input = "AAABBD"
        total = self.calculate(input)
        self.assertEqual(total, 190)
        
    def test_case_13(self):
        input = "DABABA"
        total = self.calculate(input)
        self.assertEqual(total, 190)

if __name__ == "__main__":
    unittest.main()