def solution(N, A):
    counters = [0] * N  
    max_counter = 0  
    last_update = 0  

    for X in A:
        if 1 <= X <= N
            if counters[X-1] < last_update:
                counters[X-1] = last_update + 1
            else:
                counters[X-1] += 1
            max_counter = max(max_counter, counters[X-1])
        elif X == N + 1
            last_update = max_counter
    for i in range(N):
        if counters[i] < last_update:
            counters[i] = last_update

    return counters
