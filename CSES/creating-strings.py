alphas = sorted(input())
results = []


def find_all_permutations(to_permute, cur_permutation=""):
    if 0 == len(to_permute):
        results.append(cur_permutation)
        return
    used_alpha_sets = set()
    for i in range(len(to_permute)):
        if to_permute[i] in used_alpha_sets:
            continue
        used_alpha_sets.add(to_permute[i])
        next_permute = to_permute[:i] + to_permute[i+1:]
        find_all_permutations(next_permute, cur_permutation + to_permute[i])


find_all_permutations(alphas)
print(len(results))
for item in results:
    print(item)

