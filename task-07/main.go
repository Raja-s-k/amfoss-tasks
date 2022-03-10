package main

import (
	"encoding/csv"
	"log"
	"os"

	"github.com/gocolly/colly"
)

func main() {

	fName := "data.csv"
	file, err := os.Create(fName)
	if err != nil {
		log.Fatalf("Could not create file, err: %q", err)
		return
	}
	defer file.Close()

	writer := csv.NewWriter(file)

	defer writer.Flush()

	c := colly.NewCollector(
		colly.AllowedDomains("forbes.com"),
	)

	c.OnHTML(".base ng-scope", func(e *colly.HTMLElement) {
		//links := e.ChildAttrs("ng-href", "a")
		//fmt.Println(links)
		writer.Write([]string{
			e.ChildText("div.ng-scope"),
		})

	})

	c.Visit("https://www.forbes.com/real-time-billionaires/#24b3862a3d78")
	log.Printf("done")
	log.Println(c)

}
