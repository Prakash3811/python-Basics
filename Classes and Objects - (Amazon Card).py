class Card:
    def __init__(self, imageUrl, deviceType, price, rating):
        self.imageUrl = imageUrl
        self.deviceType = deviceType
        self.price = price
        self.rating = rating


product1 = Card("Dummy-url 1", "Mobile", 56000, 4.5)
product2 = Card("Dummy-url 2", "Laptop", 94000, 4.8)
product3 = Card("Dummy-url 3", "Smart-watch", 18000, 3.5)


print("Product - 1 :")
print("imageUrl:", product1.imageUrl)
print("deviceType:", product1.deviceType)
print("price:", product1.price)
print("rating:", product1.rating)
print()

print("Product - 2 :")
print("imageUrl:", product2.imageUrl)
print("deviceType:", product2.deviceType)
print("price:", product2.price)
print("rating:", product2.rating)
print()

print("Product - 3 :")
print("imageUrl:", product3.imageUrl)
print("deviceType:", product3.deviceType)
print("price:", product3.price)
print("rating:", product3.rating)
