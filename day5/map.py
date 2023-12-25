
lines = open("./input.txt").read().splitlines()
lines = list(filter(lambda x: x, lines))


seeds = lines[0].split(":")[1].strip().split(" ")
seeds_part_2 = [(int(seeds[i]), int(seeds[i +1]) + int(seeds[i])) for i in range(0, len(seeds)-1, 2)]
print(seeds_part_2)
maps = lines[1:]
low_location = None

hash_map = {}
current_map = maps[0]
key_a = current_map.split("-")[0]
key_b = current_map.split("-")[2]
for map in maps:
    if not map[0].isnumeric():
        current_map = map
        current_map = current_map.split(" ")[0]
        key_a = current_map.split("-")[0]
        key_b = current_map.split("-")[2]
        hash_map[current_map] = {
            key_a: [],
            key_b: []
        }
        continue

    destination, source, _range = map.split(" ")
    destination = int(destination)
    source = int(source)
    _range = int(_range)

    hash_map[current_map][key_a].append((source, source + _range))
    hash_map[current_map][key_b].append((destination, destination + _range))

current_lookup = None
locations = []
for x in seeds_part_2:
    print(x)
    for seed in range(*x):
        current_lookup = seed
        for key, val in hash_map.items():
            key_a = key.split("-")[0]
            key_b = key.split("-")[2]
            for i in range(len(val[key_a])):
                if int(current_lookup) in range(*val[key_a][i]):
                    index = range(*val[key_a][i]).index(int(current_lookup))
                    current_lookup = range(*val[key_b][i])[index]
                    break
        locations.append(current_lookup)


print(min(locations))
