#a 
customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")

price_per_unit = float(input("Enter price per unit (KZT): "))
quantity = int(input("Enter quantity: "))

subtotal = price_per_unit * quantity
#b
if subtotal > 5000:
    discount = subtotal * 0.10
else:
    discount = 0

total = subtotal - discount
#c
print("=" * 30)
print("SHOP RECEIPT")
print("=" * 30)

print("Customer : " + customer_name)
print("Product : " + product_name)
print("Price : " + str(price_per_unit) + " KZT")
print("Quantity : " + str(quantity))

print("-" * 30)

print("Subtotal : " + str(subtotal) + " KZT")
print("Discount : " + str(discount) + " KZT")
print("Total : " + str(total) + " KZT")

print("=" * 30)
#d
print("Discount applied:", subtotal > 5000)
print("Paid more than 3000:", total > 3000)