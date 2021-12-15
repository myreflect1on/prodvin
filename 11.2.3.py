d = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}
m = []
for i in input():
    for j, k in d.items():
        if i in k:
            m.append(j)
print(sum(m))
