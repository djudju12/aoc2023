package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type seed struct {
	s int
	r int
}

type nmap struct {
	dst int
	src int
	r   int
}

func main() {
	ba, err := os.ReadFile("input")
	if err != nil {
		panic(err)
	}

	maps := string(ba)[len("seeds: "):]

	seeds, maps := getSeeds(maps)
	seedToSoil, maps := getMap(maps, "seed-to-soil map:\n", "soil-to", false)
	soilToFertilizer, maps := getMap(maps, "soil-to-fertilizer map:\n", "fertilizer-to", false)
	fertilizerToWater, maps := getMap(maps, "fertilizer-to-water map:\n", "water-to", false)
	waterToLight, maps := getMap(maps, "water-to-light map:\n", "light-to", false)
	lightToTemperature, maps := getMap(maps, "light-to-temperature map:\n", "temperature-to", false)
	temperatureToHumidity, maps := getMap(maps, "temperature-to-humidity map:\n", "humidity-to", false)
	humidityToLocation, maps := getMap(maps, "humidity-to-location map:\n", "", true)

	location := 0
	for {
		humidity := getKey(humidityToLocation, location)
		temperature := getKey(temperatureToHumidity, humidity)
		light := getKey(lightToTemperature, temperature)
		water := getKey(waterToLight, light)
		fertilizer := getKey(fertilizerToWater, water)
		soil := getKey(soilToFertilizer, fertilizer)
		nseed := getKey(seedToSoil, soil)

		for _, seed := range seeds {
			if nseed >= seed.s && nseed < seed.r+seed.s {
				fmt.Println(location)
				return
			}

		}
		location += 1
	}
}

func getSeeds(maps string) ([]seed, string) {
	next_i := strings.Index(maps, "seed-to-soil map:\n")
	seeds := []seed{}
	for i, c := range maps {
		if c == '\n' {
			seeds_str := strings.Fields(maps[:i])
			for i := 0; i < len(seeds_str)-1; i += 2 {
				s, _ := strconv.Atoi(string(seeds_str[i]))
				r, _ := strconv.Atoi(string(seeds_str[i+1]))
				seeds = append(seeds, seed{s, r})
			}
			break
		}
	}

	return seeds, maps[next_i:]
}

func getMap(maps string, header string, nextHeader string, eof bool) ([]nmap, string) {
	next := len(maps)
	if !eof {
		next = strings.Index(maps, nextHeader)
	}

	var result []nmap
	for _, entry := range strings.Split(maps[len(header):next], "\n") {
		if entry != "" {
			dstSrcR := strings.Fields(entry)
			dst, err := strconv.Atoi(dstSrcR[0])
			if err != nil {
				log.Fatalf("cannot convert %s", dstSrcR[0])
			}
			src, err := strconv.Atoi(dstSrcR[1])
			if err != nil {
				log.Fatalf("cannot convert %s", dstSrcR[1])
			}
			r, err := strconv.Atoi(dstSrcR[2])
			if err != nil {
				log.Fatalf("cannot convert %s", dstSrcR[2])
			}
			result = append(result, nmap{dst, src, r})
		}
	}

	return result, maps[next:]
}

func getKey(maps []nmap, value int) int {
	for _, m := range maps {
		if value >= m.dst && value < m.dst+m.r {
			return m.src + (value - m.dst)
		}
	}

	return value
}
