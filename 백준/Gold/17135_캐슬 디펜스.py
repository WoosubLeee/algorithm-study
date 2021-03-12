import copy


class Archer:

    def __init__(self, x, D):
        self.x = x
        self.D = D

    def fetch_target(self, field):
        for d in range(1, self.D+1):
            for e in range(-d+1, d):
                if 0 <= self.x + e < len(field[0]):
                    enemy_x = self.x + e
                    if len(field) - (d-abs(e)) >= 0:
                        enemy_y = len(field) - (d-abs(e))
                        if field[enemy_y][enemy_x]:
                            return enemy_y, enemy_x
        else:
            return None


N, M, D = map(int, input().split())
map_field = [list(map(int, input().split())) for _ in range(N)]
max_kill_count = 0
kill_count = 0
for i in range(M):
    for j in range(i+1, M):
        for k in range(j+1, M):
            kill_count = 0
            field = copy.deepcopy(map_field)
            arc_a = Archer(i, D)
            arc_b = Archer(j, D)
            arc_c = Archer(k, D)
            for n in range(N):

                target_a = arc_a.fetch_target(field)
                target_b = arc_b.fetch_target(field)
                target_c = arc_c.fetch_target(field)

                set_target = {target_a, target_b, target_c}
                for s in set_target:
                    if s:
                        field[s[0]][s[1]] = 0
                        kill_count += 1
                for nn in range(N-1, n, -1):
                    field[nn] = field[nn-1]
                for nn in range(n+1):
                    field[nn] = [0]*M

            if kill_count > max_kill_count:
                max_kill_count = kill_count

print(max_kill_count)