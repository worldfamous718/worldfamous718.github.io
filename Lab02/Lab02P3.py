#
# World McCrea
# 5/27/2024
# Program for Bargain Swap Shop Loyalty Rewards
#
# Ask user for total purchase amount
purchase_total = float(input('Enter the total purchase amount: '))

# Ask if user is in loyalty program
loyalty_check = input('Is the customer a loyalty member? y/n?: ').lower()
while loyalty_check != 'y' and loyalty_check != 'n':
      print('Please enter y or n ONLY')
      loyalty_check = input('Is the customer a loyalty member? y/n?: ').lower()

# Calculate sales tax on total
tax_on_total = purchase_total * .065

# Calculate grand total
grand_total = purchase_total + tax_on_total

# Display tax amount and total with tax
print(f'Sales tax: ${tax_on_total: .2f} \n'
      f'Total after tax: ${grand_total: .2f}')

# determine gift card eligibility
# if loyalty yes else loyalty no
if loyalty_check == 'y':
      if grand_total >= 50 and grand_total <= 100:
            print('Gift Card Award; $15')
      elif grand_total > 100:
            print('Gift Card Award: $25')
      else:
            print('Gift Card Award: $0')
else:  #loyaly_check == 'n':
      if grand_total > 100:
            print('Gift Card Award: $5')
      else: print('Gift Card Amount: $0')










