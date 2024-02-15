# Scraping Website using Scrapy 

## Setting up virtual environment

#### python3 -m venv venv -> to create the virtual environment
#### source venv/bin/activate -> activate the virtual environment 

## Scrapy File Details

#### spider.py contains python script for web crawling 
#### items.py describes what all information is to be scraped
#### pipelines.py stores/upload items to a database
#### middlewares.py configures the web scraper and its working

## Generating spider 

#### scrapy genspider spidername url

## Using terminal for testing before real time scraping

#### Switch shell to ipython for better experience
#### scrapy shell - to open ipython shell

## Testing in shell : Study website's structure, decide what all data is to scraped, explore website source

#### fetch("url")  - preliminary step to fetch website's entire source
#### response.css("element")  - filter specific element from code , .get() at end to get html tags
#### variable.css("element::text")  - example to get text from a specific element like <p>, <h> 

## Crawling website for data

#### After testing and spider script is complete and verified in the shell, we can now scrape data from website
#### scrapy crawl ufcspider
#### Save results to a file

## Update coming : Adding data directly to database using item and pipeline files