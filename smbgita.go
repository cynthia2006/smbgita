package main

import (
	"encoding/json"
	"fmt"
	"math/rand/v2"
	"os"
	"path"
)

func main() {
	numShlokas := [...]int{47, 72, 43, 42, 29, 47, 30, 28, 34, 42, 55, 20, 35, 27, 20, 24, 28, 78}

	var shloka struct {
		Sanskrit    string
		Iast        string
		Translation string
	}

	chapterIndex := rand.IntN(len(numShlokas))
	shlokaIndex := rand.IntN(numShlokas[chapterIndex])
	shlokaFilePath := path.Join("data", fmt.Sprintf("%d/%d.json", chapterIndex, shlokaIndex))

	shlokaData, err := os.ReadFile(shlokaFilePath)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Failed to open %s: %v\n", shlokaFilePath, err)
		return
	}

	json.Unmarshal(shlokaData, &shloka)

	fmt.Printf("%s\n\n%s\n", shloka.Iast, shloka.Translation)
}
