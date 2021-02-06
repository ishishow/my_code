import sys
UNDER_1000_PER_PRICE = 180
UNDER_2000_PER_PRICE = 275
UNDER_3000_PER_PRICE = 290
OVER_3000_PER_PRICE = 300

args = sys.argv
if len(args) != 2:
    print("Error please input meat weight!")
    sys.exit()

weight = int(args[1])
price = 0

if weight > 10000:
    print("Error please don't buy over 10000 weight!")
    sys.exit()



def under_1000_gram():
    return(UNDER_1000_PER_PRICE*5)

def under_2000_gram(weight,price):
    if weight >= 1500:
        return (weight-1500), (price+UNDER_2000_PER_PRICE*15)
    else:
        return (weight-1000), (price+UNDER_2000_PER_PRICE*10)

def under_3000_gram(weight, price):
    if weight >= 2500:
        return (weight-2500),(price+UNDER_3000_PER_PRICE*25*0.8)
    else:
        return (weight-2000),(price+UNDER_3000_PER_PRICE*20*0.8)


def over_3000_gram(weight, price):
    coefficient = weight // 500
    return(price + OVER_3000_PER_PRICE*coefficient*5*0.8)


if 500 <= weight < 1000:
    price = under_1000_gram()
elif 1000 <= weight < 2000:
    _, price = under_2000_gram(weight)
elif 2000 <= weight < 3000:
    tmp = weight
    while weight >= 1000:
        weight, price = under_2000_gram(weight,price)
    _, once_price = under_3000_gram(tmp, price)
    if price < once_price:
        price = once_price
print(price)







