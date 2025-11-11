purchase_amount = float(input("Enter the purchase amount: "))
if purchase_amount >= 1000:
    discount = 0.10
elif purchase_amount >= 500:  
    discount = 0.05
else:
    discount = 0.0
final_price = purchase_amount * (1 - discount)
print('The final price after discount is: $', str(final_price))