def dynamicArray(n, queries):
    sequences = [[] for _ in range(n)]
    last_answer = 0
    for q in queries:
        if q[0] == 1:
            idx = (q[1] ^ last_answer) % n
            sequences[idx].append(q[2])
            continue

        if q[0] == 2:
            idx = (q[1] ^ last_answer) % n
            last_answer = sequences[idx][q[2] % len(sequences[idx])]
            print(last_answer)

dynamicArray(2, [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]])

