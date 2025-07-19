def count_suits_iterative(suits):
    count = 0
    for suit in suits:
        count+=1
    return count

def  count_suits_recursive(suits):
    if suits == []:
       return 0
    return 1 + count_suits_recursive(suits[1:])

        
        

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_iterative(["Mark I", "Mark I", "Mark III", "Mark IV"]))


def sum_stones(stones):
    if stones == []:
       return 0
    return stones[0] + sum_stones(stones[1:])

print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))


def count_suits_iterative(suits):
    suits = set(suits)
    count = 0
    for suit in suits:
        count += 1
    return count

def count_suits_recursive(suits, memo = {}):
    
    if suits == []:
       return 0
    # if not in memo
    if suits[0] not in memo:
        memo[suits[0]] = suits[0]
        return 1 + count_suits_recursive(suits[1:], memo)
    # if in memo, return 0 + ...
    if suits[0] in memo:
        return 0 + count_suits_recursive(suits[1:], memo)


print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))


def fibonacci_growth(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_growth(n-1) + fibonacci_growth(n-2)

print(fibonacci_growth(5))
print(fibonacci_growth(8))

def power_of_four(n):
   # if n = 0 , return 1
    
    if n == 0:
        return 1
    if n > 0:
        return power_of_four(n-1) * 4
    if n < 0:
        return power_of_four(n+1) * (1/4)

print(power_of_four(2))
print(power_of_four(-2))


def strongest_avenger(strengths):
    
    def strongest_recursive(strengths, memo = float("-inf")):
        print(memo)
        if not strengths:
            return memo
        if strengths[0] > memo:
            return strongest_recursive(strengths[1:], strengths[0])
        return strongest_recursive(strengths[1:], memo)
        
    return  strongest_recursive(strengths)


print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
print(strongest_avenger([50, 75, 85, 60, 90]))

