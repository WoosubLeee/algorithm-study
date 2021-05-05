import sys


# set를 활용해 중복을 제거한다.
words = set(sys.stdin.readline().strip() for _ in range(int(sys.stdin.readline().strip())))
"""
'\n'.join : 기존엔 반복문을 돌며 출력했는데 join을 활용하면 한 번에 출력할 수 있음

sorted(words, key=lambda word: (len(word), word)))
: words set를 정렬한다.
기준은 len(word)가 1순위(단어의 길이), word가 2순위(알파벳 기준)가 된다.
"""
sys.stdout.write('\n'.join(sorted(words, key=lambda word: (len(word), word))))
