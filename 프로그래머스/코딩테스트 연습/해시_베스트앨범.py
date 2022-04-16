def solution(genres, plays):
    genres_dict = {}
    for i in range(len(genres)):
        genre, count = genres[i], plays[i]
        if genre not in genres_dict:
            genres_dict[genre] = {
                'songs': [],
                'count': 0
            }

        genres_dict[genre]['songs'].append([i, count])
        genres_dict[genre]['count'] += count

    answer = []
    for genre_info in sorted(genres_dict.values(), key=lambda x: x['count'], reverse=True):
        songs = sorted(genre_info['songs'], key=lambda x: x[1], reverse=True)
        answer.extend(list(map(lambda x: x[0], songs))[:2])
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))