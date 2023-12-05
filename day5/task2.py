#!/usr/bin/python3
def main():
    maps = read_file("input")[len("seeds: "):]
    seeds, maps = get_seeds(maps)
    seed_to_soil, maps = get_map(maps, "seed-to-soil map:\n", "soil-to")
    soil_to_fertilizer, maps = get_map(maps, "soil-to-fertilizer map:\n", "fertilizer-to")
    fertilizer_to_water, maps = get_map(maps, "fertilizer-to-water map:\n", "water-to")
    water_to_light, maps = get_map(maps, "water-to-light map:\n", "light-to")
    light_to_temperature, maps = get_map(maps, "light-to-temperature map:\n", "temperature-to")
    temperature_to_humidity, maps = get_map(maps, "temperature-to-humidity map:\n", "humidity-to")
    humidity_to_location, maps = get_map(maps, "humidity-to-location map:\n", eof=True)

    location = 0
    while True:
        humidity = get_key(humidity_to_location, location)
        temperature = get_key(temperature_to_humidity, humidity)
        light = get_key(light_to_temperature, temperature)
        water = get_key(water_to_light, light)
        fertilizer = get_key(fertilizer_to_water, water)
        soil = get_key(soil_to_fertilizer, fertilizer)
        seed = get_key(seed_to_soil, soil)

        for start, end in seeds:
            if seed >= start and seed < end+start:
                print(location)
                return

        location += 1

def get_seeds(maps: str):
    next_i = maps.index("seed-to-soil map:\n")
    for i, c in enumerate(maps):
        if c == '\n':
            seeds_str = maps[0:i]
            seeds = list(map(int, seeds_str.split(" ")))
            tseeds = []
            for i in range(0, len(seeds), 2):
                tseeds.append((seeds[i], seeds[i+1]))

            return tseeds, maps[next_i:]

def get_map(maps: str, header: str, next_header: str = "", eof: bool = False):
    next_i = maps.index(next_header) if not eof else len(maps)
    nmap = maps[len(header):next_i]
    result = extract_map(nmap.splitlines())
    return result, maps[next_i:]

def extract_map(lines: list[str]) -> dict:
    result = []
    for entry in lines:
        if len(entry) > 0:
                           # (dst, src, r)
            result.append( tuple(map(int, entry.split(" "))) )

    return result

def get_key(map, value):
    dst, src, r = 0, 1, 2
    for m in map:
        if value >= m[dst] and value < m[dst]+m[r]:
            return m[src] + (value - m[dst])

    return value

def read_file(path: str) -> str:
    with open(path, 'r') as f:
        return f.read()


if __name__ == '__main__':
    main()