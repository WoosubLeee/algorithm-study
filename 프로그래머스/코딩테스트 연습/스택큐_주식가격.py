def solution(prices):
    answer = [0]*len(prices)

    stack = []
    for i, price in enumerate(prices):
        while stack:
            if stack[-1]['price'] > price:
                popped = stack.pop()
                answer[popped['index']] = i - popped['index']
            else:
                break
        stack.append({
            'index': i,
            'price': price
        })

    while stack:
        popped = stack.pop()
        answer[popped['index']] = len(prices) - popped['index'] - 1

    return answer


print(solution([1, 2, 3, 2, 3]))