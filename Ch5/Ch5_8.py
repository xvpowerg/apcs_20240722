for i in range(1,5):
    for j in range(1,5):
        if i==j:
            continue
        for k in range(1,5):
            if i == k or j == k:
                continue
            for l in range(1,5):
                if i == l or j == l or k == l:
                    continue
                print(f"{i}{j}{k}{l}")
