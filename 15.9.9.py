countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
print(*[f'{x[0]} is the capital of {x[1]}, population equal {x[2]} people.' for x in list(zip(capitals, countries, population))], sep='\n')