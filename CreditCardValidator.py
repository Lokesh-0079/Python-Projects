# To check credit card validation -->  remove any "-" or " ",add odd digits from right to left, then add doubled every even digit from right to left, if the sum is a 2-digit number, sum the internal digits until a single digit, now add the previous 2 steps and check if the number is divisible by 10, if it does it is valid, otherwise not valid

sum_odd_digits=0 #odd digits in the number from right to left
sum_even_digits=0  #even digits in the number from right to left
total=0 # sum of even and odd sum
#Step 1
card_number= input("Enter the credit card number: ")
card_number=card_number.replace("-","")
card_number=card_number.replace(" ","")
card_number=card_number[::-1]
#print(card_number)

#STEP 2
for x in card_number[::2]:
    sum_odd_digits+=int(x)
print(f"The sum of odd digits is: {sum_odd_digits}" )

#STEP 3

for x in card_number[1::2]:
    x = int(x)
    x+=x*2

    if x >= 10:
        sum_even_digits+=(1+(x % 10))
    else:
        sum_even_digits+=x
print(f"The sum of even digits is: {sum_even_digits}" )
#STEP 4
total=sum_odd_digits+sum_even_digits
print(f"The sum of total digits is: {total}" )
#STEP 5
print("The credit card is VALID!" if total % 10 ==0 else "This credit card is INVALID!")