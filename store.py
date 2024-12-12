class Product:
    def __init__(self, name, unitPrice, specialPrice=None):
        self.name = name
        self.unitPrice = unitPrice
        self.specialPrice = specialPrice

    def calculatePrice(self, quantity):
        if self.specialPrice:
            bundles = quantity // self.specialPrice["quantity"]
            remaining = quantity % self.specialPrice["quantity"]
            return bundles * self.specialPrice["price"] + remaining * self.unitPrice
        return quantity * self.unitPrice


class Checkout:
    def __init__(self, pricingRules):
        self.pricingRules = pricingRules
        self.cart = {}  # Stores the quantity of each product in the cart

    def scan(self, item):
        if item not in self.pricingRules:
            raise ValueError(f"Unknown product: {item}")
        self.cart[item] = self.cart.get(item, 0) + 1

    def calculateTotal(self):
        total = 0
        for item, quantity in self.cart.items():
            product = self.pricingRules[item]
            total += product.calculatePrice(quantity)
        return total