def solution(coin, cards):
    n = len(cards)
    curr_coin = coin
    card_idx = int(n / 3)
    hand = cards[:card_idx]
    curr_round = 0
    
    ret = decision_dfs(card_idx, curr_coin, hand, cards, n)
    
    # Why off by one???
    return ret + 1

def decision_dfs(card_idx, curr_coin, hand, cards, n):
    sums = []
    for i in range(len(hand)):
        for j in range(i, len(hand)):
            sums.append(hand[i] + hand[j])
    
    # Leaf node
    if card_idx >= n:
        return 0
    
    ret = 0
    
    # Spend two coins
    if curr_coin - 2 >= 0:
        hand.append(cards[card_idx])
        hand.append(cards[card_idx+1])
        for i in range(len(hand)):
            for j in range(i, len(hand)):
                if hand[i] + hand[j] == n + 1:
                    next_hand = [ x for x in hand if x not in [hand[i], hand[j]] ]
                    ret = max(ret, 1 + decision_dfs(card_idx + 2, curr_coin - 2, next_hand, cards, n))

        hand.pop(-1)
        hand.pop(-1)
    
    # Spend 1st
    if curr_coin - 1 >= 0:
        hand.append(cards[card_idx])
        for i in range(len(hand)):
            for j in range(i, len(hand)):
                if hand[i] + hand[j] == n + 1:
                    next_hand = [ x for x in hand if x not in [hand[i], hand[j]] ]
                    ret = max(ret, 1 + decision_dfs(card_idx + 2, curr_coin - 1, next_hand, cards, n))
        hand.pop(-1)
    
    # Spend 2nd
    if curr_coin - 1 >= 0:
        hand.append(cards[card_idx + 1])
        for i in range(len(hand)):
            for j in range(i, len(hand)):
                if hand[i] + hand[j] == n + 1:
                    next_hand = [ x for x in hand if x not in [hand[i], hand[j]] ]
                    ret = max(ret, 1 + decision_dfs(card_idx + 2, curr_coin - 1, next_hand, cards, n))
        hand.pop(-1)
    
    # Discard both
    for i in range(len(hand)):
        for j in range(i, len(hand)):
            if hand[i] + hand[j] == n + 1:
                next_hand = [ x for x in hand if x not in [hand[i], hand[j]] ]
                ret = max(ret, 1 + decision_dfs(card_idx + 2, curr_coin, next_hand, cards, n))
    
    return ret