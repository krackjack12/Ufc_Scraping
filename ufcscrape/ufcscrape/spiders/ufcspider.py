import scrapy
import json
from datetime import datetime

class UfcspiderSpider(scrapy.Spider):
    name = "ufcspider"
    allowed_domains = ["www.ufc.com"]
    start_urls = ["https://www.ufc.com/rankings"]
    
    # 1 for Ranking page and 2 for Athelete page

    def parse(self, response, operation=1):
        if operation == 1:
            view_content = response.css("div.view-grouping")  # gives the outer div element which contains all ranking information
            view_group_content = view_content.css("div.view-grouping-content")  # gives inside elements for each divison 

            print(len(view_group_content))  # 13 divisons - output verified 

            fighter_info = view_group_content.css("div.info")  # div element which contains division name and top fighter name 

            # Getting all divisons names in the ufc ranking page 
            fighter_divisons_name = fighter_info.css("h4::text") # divison name stored in h4 tag, also contains top players athelete page link
            
            divisons = []
            for i in fighter_divisons_name:  # Getting all divisions name
                #print(i.get())
                divisons.append(i.get())

            # Getting top ranked fighter in each divison
            top_fighter_name = fighter_info.css("h5 a::text")

            top_fighters = []
            for i in top_fighter_name:  # Getting top fighters in each division
                #print(i.get())
                top_fighters.append(i.get())

            # Get top 15 ranked fighters in each division  
            fighter_division_table = view_group_content.css("tbody") # table element for every divison
            
            #fighter_division = fighter_division_table[0]  # for loop for this

            fighter_data = []  # stores data of divison on rankings page - dict of each divison with data
            counter = 0
            division_data = []
            for fighter_division in fighter_division_table:
                fighter_row = fighter_division.css("tr")
                fighter_name = fighter_row.css("tr a::text")

                top15_division = []
                for i in fighter_name:
                    #print(i.get())
                    top15_division.append(i.get())
                
                division_data.append(top15_division)

                # Dictonary item for each divison
                division_info = {"Divison name:":divisons[counter],"Top fighter name:":top_fighters[counter],"Ranked fighters in division":division_data[counter]}
                fighter_data.append(division_info)  # appending data

                counter+=1 # counter increment

            print(fighter_data)

            #Adding time stamp for each update 
            current_time = datetime.now()

            timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
            
            # Writing output to text file spider_output.jsonl
            with open("/Users/krishjoshi/Desktop/Projects/UFC_Scraping/ufcscrape/ufcscrape/spiders/spider_output.jsonl","a") as file:
                file.write(f"Timestamp of update: {timestamp} \n")
                for item in fighter_data:
                    json_str = json.dumps(item,ensure_ascii=False)
                    file.write(json_str + "\n")
            file.close()

        elif operation==2:
            pass