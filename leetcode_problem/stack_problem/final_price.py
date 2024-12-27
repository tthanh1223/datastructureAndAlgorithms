#You are given an integer array prices where prices[i] is the price of the ith item in a shop.

#There is a special discount for items in the shop.
#If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i].
#Otherwise, you will not receive any discount at all.

# discount = prices[j] where j is the minimum index: j > i and prices[j] <= prices[i]

#Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.

# brutal force approach : O(n^2)
def find_prices_brutal_force(prices : list[int]) -> list[int]:
    final_prices = []
    for i in range(len(prices)):
        # find the minimum index such that j > i and prices[j] <= prices[i]
        found = False
        for j in range(i+1, len(prices)):
            if prices[i] >= prices[j]:
                found = True
                break
        if found:
            final_prices.append(prices[i]-prices[j])
        else:
            final_prices.append(prices[i])
    return final_prices

# Stack approach: O(n)
def find_prices_with_stack(prices : list[int]) -> list[int]:
    stack = []
    final_prices = prices.copy()
    for i in range(len(prices)):
        # While stack is not empty and the current price is less than or equal to the price at the index stored in the stack
        while len(stack) > 0 and prices[i] <= prices[stack[-1]]:
            index = stack.pop()
            final_prices[index] -= prices[i]
        stack.append(i)
    return final_prices
# Illustrate
# ex: [8,4,6,2,3]
# i = 0: stack = [0]
# i = 1:  4 < 8 => stack = [] and final_prices[0] = 8 - 4 = 4 ; stack = [1]
# i = 2: 6 > 4 => stack = [1,2]
# i = 3: 2 < 6 => stack = [1] and final_prices[2] = 6 - 2 = 4,
#        2 < 4 => stack = [] and final_prices[1] = 4 - 2 = 2,
#        stack = [3]
# i = 4: stack = [3,4]



if __name__ == '__main__':
    prices = [8,4,6,2,3]
    print(find_prices_with_stack(prices))