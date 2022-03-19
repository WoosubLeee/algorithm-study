# # 1
# def solution(jobs):
#     jobs = sorted(jobs, key=lambda x: (x[0], x[1]))
#     heap = [0]*(len(jobs)+1)
#     end = 0
#
#     current_time = 0
#     total_time = 0
#
#     job_index = 0
#     while job_index < len(jobs) or end:
#         while job_index < len(jobs) and (jobs[job_index][0] <= current_time or end == 0):
#             job = jobs[job_index]
#             if end == 0 and job[0] > current_time:
#                 current_time = job[0]
#             heap_push(job, heap, end)
#             end += 1
#             job_index += 1
#
#         current_job = heap_pop(heap, end)
#         end -= 1
#
#         current_time += current_job[1]
#         total_time += (current_time - current_job[0])
#
#     return total_time // len(jobs)
#
#
# def heap_push(job, heap, end):
#     end += 1
#     heap[end] = job
#
#     position = end
#     while position > 1 and heap[position][1] < heap[position // 2][1]:
#         heap[position], heap[position // 2] = heap[position // 2], heap[position]
#         position //= 2
#
#
# def heap_pop(heap, end):
#     top = heap[1]
#     heap[1], heap[end] = heap[end], 0
#
#     end -= 1
#     position = 1
#     while True:
#         shortest = position
#         if 2*position <= end and heap[shortest][1] > heap[2*position][1]:
#             shortest = 2*position
#         if 2*position + 1 <= end and heap[shortest][1] > heap[2*position + 1][1]:
#             shortest = 2*position + 1
#
#         if shortest == position:
#             return top
#         heap[position], heap[shortest] = heap[shortest], heap[position]
#         position = shortest


# 2
import heapq


def solution(jobs):
    jobs = sorted([(job[1], job[0]) for job in jobs], key=lambda x: (x[1], x[0]), reverse=True)
    size = len(jobs)

    heap = []
    current_time, total_time = 0, 0
    while jobs or heap:
        while jobs and jobs[-1][1] <= current_time:
            heapq.heappush(heap, jobs.pop())

        if heap:
            current_job = heapq.heappop(heap)
        else:
            current_job = jobs.pop()
            current_time = current_job[1]

        current_time += current_job[0]
        total_time += (current_time - current_job[1])

    return total_time // size


jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))