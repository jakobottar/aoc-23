from multiprocessing import Pool


class range_dict:
    def __init__(self):
        self.dict = dict()
        self.starts = []

    def set(self, key, value):
        """key should be a tuple (start, length)"""

        self.dict[key[0]] = (key[1], value)
        self.starts.append(key[0])
        self.starts.sort()

    def get(self, key):
        start = -1
        for s in self.starts:
            if s > key:
                break
            start = s

        try:
            length, value = self.dict[start]
        except KeyError:
            # if key is smaller than any start, return key
            return key

        if key < start + length:
            return value + (key - start)
        else:
            return key


class Almanac:
    def __init__(self, lineblock):
        self.mapping = range_dict()
        self.parse(lineblock)

    def parse(self, lineblock):
        for line in lineblock:
            dest, src, length = [int(x) for x in line.split(" ")]
            self.mapping.set((src, length), dest)

    def __getitem__(self, key):
        return self.mapping.get(key)


if __name__ == "__main__":
    FILENAME = "input.txt"

    # parse input:
    with open(FILENAME, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines()]

    # first line contains seed nums
    seed_nums = [int(x) for x in lines[0][7:].split(" ")]  # if x.isdigit()]

    # remove first three lines
    lines = lines[3:]

    # next block contains seed-to-soil maps
    seed_to_soil = Almanac(lines[0 : lines.index("")])
    lines = lines[lines.index("") + 2 :]

    # then soil-to-fertilizer maps
    soil_to_fertilizer = Almanac(lines[0 : lines.index("")])
    lines = lines[lines.index("") + 2 :]

    # fertilizer-to-water maps
    fertilizer_to_water = Almanac(lines[0 : lines.index("")])
    lines = lines[lines.index("") + 2 :]

    # water-to-light maps
    water_to_light = Almanac(lines[0 : lines.index("")])
    lines = lines[lines.index("") + 2 :]

    # light-to-temp maps
    light_to_temp = Almanac(lines[0 : lines.index("")])
    lines = lines[lines.index("") + 2 :]

    # temp-to-humidity maps
    temp_to_humidity = Almanac(lines[0 : lines.index("")])
    lines = lines[lines.index("") + 2 :]

    # humidity-to-location maps
    humidity_to_location = Almanac(lines)

    def get_location(seed_num):
        soil_num = seed_to_soil[seed_num]
        fertilizer_num = soil_to_fertilizer[soil_num]
        water_num = fertilizer_to_water[fertilizer_num]
        light_num = water_to_light[water_num]
        temp_num = light_to_temp[light_num]
        humidity_num = temp_to_humidity[temp_num]
        location_num = humidity_to_location[humidity_num]
        # print(f"{seed_num} -> {soil_num} -> {fertilizer_num} -> {water_num} -> {light_num} -> {temp_num} -> {humidity_num} -> {location_num}")
        return location_num

    print(f"part 1: {min(map(get_location, seed_nums))}")

    # part 2

    # expand pairs of seed_nums into ranges
    seed_ranges = list(zip(*[iter(seed_nums)] * 2))

    def get_location_p2(seed_range):
        s, l = seed_range
        return min(map(get_location, range(s, s+l)))

    with Pool(processes=len(seed_ranges)) as pool:
        print(f"part 2: {min(pool.map(get_location_p2, seed_ranges))}")
