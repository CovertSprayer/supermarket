from store import Product, Checkout

pricingRules = {
    "A": Product("A", 50, {"quantity": 3, "price": 130}),
    "B": Product("B", 30, {"quantity": 2, "price": 45}),
    "C": Product("C", 20),
    "D": Product("D", 15),
}

checkout = Checkout(pricingRules)

inp = input("Enter input value: ")
for item in inp:
    checkout.scan(item)
    
result = checkout.calculateTotal()
print(f"Output: {result}")