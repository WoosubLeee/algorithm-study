def solution(phone_book):
    phone_dict = {}

    for phone in phone_book:
        phone_dict[phone] = 1

    for phone in phone_book:
        for i in range(1, len(phone)):
            if phone[:i] in phone_dict:
                return False

    return True


phone_book = ["123","456","789"]
print(solution(phone_book))