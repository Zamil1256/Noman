#Grosery store price checker

key=input("Enter a key within(apple,banana,milk):")
prices={
    'apple':3,
    'banana':1,
    'milk':5
     }
#if(key=='apple'):
#   print(prices[key])
#elif(key=='banana'):
#    print(prices[key])
#elif(key=='milk'):
#    print(prices[key])
#else:
#     print("Item not found")

if(key in prices):
    print(prices[key])
else:
    print("Item not found") 

