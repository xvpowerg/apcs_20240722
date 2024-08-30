for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            for l in range(1,5):
                if j != i and k != j and k != i and l != k and l != j and l != i:
                    print(f"{i}{j}{k}{l}")
