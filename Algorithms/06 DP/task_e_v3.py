"""TAsk E Solution"""

PRIZE_PRICE = 101
MAX_PRICE = 1000
VERY_BIG_NUMBER = 10 ** 10

def find_candidates(prices, tickets_use, tickets):
    if len(prices) == 0:
        return -1, -1, -1
    
    min_price_idx = -1
    min_price_val = MAX_PRICE
    min_over_thres_idx = -1
    min_over_price = MAX_PRICE
    to_repl_idx = -1
    to_repl_price = -MAX_PRICE
    
    for i, cur in enumerate(tickets_use):
        if cur: #ticket used here
            if prices[i] >= PRIZE_PRICE and prices[i] <= min_over_price:
                min_over_price = prices[i]
                min_over_thres_idx = i
            elif prices[i] < PRIZE_PRICE and prices[i] < min_price_val:
                min_price_val = prices[i]
                min_price_idx = i
                
    for i, cur in enumerate(tickets_use):
        if cur or i <= min_over_thres_idx:
            continue
        if prices[i] > to_repl_price:
            to_repl_price = prices[i]
            to_repl_idx = i
            
    return min_over_thres_idx, min_price_idx, to_repl_idx


def eat_it(prices):
    tickets = [0] * (len(prices) + 1)
    spendings = [0] * len(prices)
    tickets_use = [False] * len(prices)
    
    for i in range(len(prices)):
        if i == 0:
            if prices[i] < PRIZE_PRICE:
                tickets[i + 1] = tickets[i]
            else:
                tickets[i + 1] = tickets[i] + 1
            spendings[0] = prices[0]
            continue
            
        if tickets[i] > 0 and prices[i] > 0:
            tickets[i + 1] = tickets[i] - 1
            tickets_use[i] = True
        elif tickets[i] > 0 and prices[i] == 0:
            tickets_use[i] = False
            tickets[i + 1] = tickets[i]
        else:
            min_over_idx, min_price_idx, to_repl_idx = find_candidates(prices[:i], tickets_use[:i], tickets[:i])
            res1 = (spendings[i - 1] + prices[i], tickets[i]) #buy lunch
            if min_price_idx >= 0:
                res2 = (spendings[i - 1] + prices[min_price_idx], tickets[i]) #move voucher to last position
            else:
                res2 = (VERY_BIG_NUMBER, tickets[i])
            if min_over_idx >= 0 and to_repl_idx >= 0:
                res3 = (spendings[i - 1] + prices[min_over_idx] - prices[to_repl_idx], tickets[i]) #get additional voucher
            elif min_over_idx >= 0 and to_repl_idx < 0:
                res3 = (spendings[i - 1] + prices[min_over_idx], tickets[i] + 1)
            else:
                res3 = (VERY_BIG_NUMBER, tickets[i] + 2)
                
            if res1 < res2 and res1 < res3:
                if prices[i] >= PRIZE_PRICE:
                    tickets[i + 1] = tickets[i] + 1
                else:
                    tickets[i + 1] = tickets[i]
                tickets_use[i] = False
            elif res2 < res1 and res2 < res3:
                tickets_use[min_price_idx] = False
                tickets_use[i] = True
                for j in range(min_price_idx, i):
                    tickets[j + 1] += 1
                tickets[i + 1] = tickets[i] - 1
            elif res3 <= res1 and res3 <= res2:
                tickets_use[min_over_idx] = False
                if to_repl_idx >= 0:
                    tickets_use[to_repl_idx] = True
                    for j in range(to_repl_idx, i):
                        tickets[j + 1] -= 1
                tickets_use[i] = True
                for j in range(min_over_idx, i):
                    tickets[j + 1] += 1
                tickets[i] += 1
                tickets[i + 1] = tickets[i] - 1
        for i, cur in enumerate(tickets_use[:i + 1]):
            if i == 0:
                spendings[i] = prices[i]
            else:
                if cur:
                    spendings[i] = spendings[i - 1]
                else:
                    spendings[i] = spendings[i - 1] + prices[i]
                    
    #Collect results
    total = spendings[-1]
    k1 = tickets[-1]
    k2 = sum(tickets_use)
    days = []
    for i, cur in enumerate(tickets_use):
        if cur:
            days.append(i + 1)
                
    return total, k1, k2, days

if __name__ == '__main__':
    n_days = int(input())
    prices = []
    for _ in range(n_days):
        prices.append(int(input()))
    if n_days == 0:
        print(0)
        print(0, 0)
    elif n_days == 1:
        print(prices[0])
        print(int(prices[0] >= PRIZE_PRICE), 0)
    else:
        total, k1, k2, days = eat_it(prices)
        print(total)
        print(k1, k2)
        print('\n'.join([str(x) for x in days]))
