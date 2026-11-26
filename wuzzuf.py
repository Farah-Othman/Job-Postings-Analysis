# import libraries
import requests 
import os
from bs4 import BeautifulSoup as bs
import pandas as pd
import urllib.parse
import math
import time

#  job categories
job_categories = [
    "Sales",
    "Retail",
    "IT",
    "Software Development",
    "Customer Service",
    "Support",
    "Marketing",
    "PR",
    "Advertising",
    "Operations",
    "Management",
    "Engineering Mechanical",
    "Engineering Electrical",
    "Administration",
    "Engineering Construction",
    "Engineering Civil",
    "Architecture"

]

# loop over each category 
for job_category in job_categories:
    #declare lists to save information
    job_titles,jobs_link,companies,companies_links,locations,jobs_type,Career_Level,skills_list,workplaces = [],[],[],[],[],[],[],[],[]
    #edit job category to fit in link
    parse_job_category = urllib.parse.quote(job_category)
    #get no of pages to loop over all jobs
    url = #f"https://jobPosting.net/search/jobs/?q={parse_job_category}"
    response = requests.get(url)
    soup = bs(response.content,'html.parser')
    jobs_count = soup.find("li", class_ ="css-18k4nsw").text.strip()
    count_list = jobs_count.split(" ")
    count = float( count_list[len(count_list)-1])
    count /= float(15) # as each page contains 15 job 
    count = math.ceil(count) # rounds up number  
    # loop over all jobs in all pages
    for index in range(count):
        index = str(index)
        url = #f"https://jobPosting.net/search/jobs/?q={parse_job_category}&start={index}"
        #get page content
        response = requests.get(url)
        soup = bs(response.content,'html.parser')
        #get div contents
        containers = soup.find_all("div", class_ ="css-ghe2tq e1v1l3u10")

        for container in containers:
            job_title = container.find("h2",class_="css-193uk2c")
            job_titles.append(job_title.text.strip())

            job_link = container.find("a",class_="css-o171kl")
            jobs_link.append(job_link.get('href'))  

            company = container.find("a",class_="css-ipsyv7")
            companies.append(company.text.strip())

            company_link = container.find("a",class_="css-ipsyv7")
            companies_links.append(company_link.get('href')) 

            location = container.find("span",class_="css-16x61xq")
            locations.append(location.text.strip())

            job_type = container.find("span",class_="css-uc9rga eoyjyou0")
            jobs_type.append(job_type.text.strip())

            Careers_Level = container.find_all("a",class_="css-o171kl")
            Career_Level.append(Careers_Level[1].text.strip())

            skills_container = container.find_all("a" , class_ = "css-5x9pm1")
            skills = []
            for skill in skills_container:
                skills.append(skill.text.strip())
            skills_list.append(skills)

            workplace = container.find("span",class_="css-uofntu eoyjyou0")
            if workplace:
                workplaces.append(workplace.text.strip())
            else:
                workplaces.append("Not specified")

    # check if files exists before and prevent adding duplicates
    df = pd.DataFrame({'job_titles':job_titles,'jobs_link':jobs_link,'companies':companies,'companies_links':companies_links,'locations':locations,'jobs_type':jobs_type,'Career_Level':Career_Level,'skills_list':skills_list,'workplaces':workplaces})

    file_path=f"C:/Documents/jobPosting_scraping/jobPosting_data/{job_category}_jobs.csv"

    if not os.path.exists(file_path):
        df.to_csv(file_path,index=False,encoding='utf-8-sig')

    else:
        df_old=pd.read_csv(file_path,encoding='utf-8-sig')
        df_new=df[~df['jobs_link'].isin(df_old['jobs_link'])]

        if not df_new.empty:
            df_new.to_csv(file_path,index=False,encoding='utf-8-sig',mode='a',header=False)
    
    print("successful")




