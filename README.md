#  Job Market Analysis 2025 | Python Web Scraping, Data Preparation & Power BI

An end-to-end job-market analytics project built around job listings collected from **Job Posting website**. The project uses Python to collect job-posting details across multiple career categories, prepares the collected information in Excel, and provides a dataset for exploring hiring patterns, employer demand, locations, career levels, work arrangements, and required skills.

The objective is to turn unstructured job-board listings into an analysis-ready dataset that can help job seekers understand where opportunities are concentrated and which skills appear most frequently in employer requirements.

> **Dataset snapshot:** The figures below describe the supplied cleaned workbook, not live listings. Job-board content changes over time, and the workbook does not include a verified collection date.

## Project impact at a glance

| Measure | Result |
|---|---:|
| Job postings in the cleaned dataset | **8,835** |
| Job-skill records | **54,681** |
| Distinct non-empty skill labels | **6,852** |
| Unique companies represented | **2,756** |
| Countries represented | **33** |
| Cities represented | **100** |
| Duplicate job URLs in the job table | **0** |

These numbers show the analytical scale of the project: thousands of postings can be explored together with tens of thousands of skill associations, across a broad set of employers and locations.

## Key findings from the supplied dataset

- **Geographic concentration:** Egypt accounts for **7,420 postings (84.0%)**. Cairo alone accounts for **4,724 postings (53.5%)**, making it the largest city in the dataset.
- **Full-time demand:** **8,519 postings (96.4%)** are classified as Full Time.
- **Experience requirements:** **4,950 postings (56.0%)** target Experienced candidates, while **2,365 (26.8%)** are Entry Level and **1,168 (13.2%)** are Manager roles.
- **Work arrangement:** **6,632 postings (75.1%)** are On-site. The dataset also contains **592 Hybrid (6.7%)** and **448 Remote (5.1%)** postings. Work arrangement is not specified for **1,163 postings (13.2%)**.
- **Skill information:** The skills table contains **54,681 job-skill rows**, equivalent to approximately **6.2 skill records per job** on average.
- **Employer coverage:** The dataset contains **2,756 distinct company names**, providing a basis for employer-level comparisons.

Percentages are calculated against the 8,835 job-posting rows and rounded to one decimal place. Categories such as `Not specified` are retained where present in the source data.

## Questions this project can help investigate

1. Which job categories account for the largest share of collected vacancies?
2. Which cities and countries have the highest number of listings?
3. What proportion of vacancies are full-time, part-time, internship, freelance, or shift-based?
4. Which career levels are most frequently requested?
5. How common are on-site, hybrid, and remote opportunities?
6. Which skills occur most often across job postings?
7. Which companies appear most frequently in the collected listings?

## Workflow

1. **Collect:** Python sends HTTP requests to job-search pages for configured job categories.
2. **Parse:** BeautifulSoup extracts job titles, job URLs, company names and URLs, locations, job types, career levels, skills, and workplace arrangements.
3. **Structure:** pandas organizes the extracted information into tabular data.
4. **Avoid duplicate appends:** The scraper checks existing CSV files and appends only rows whose job URLs are not already present.
5. **Prepare:** The Excel workbook separates job-level information from the job-to-skill records.
6. **Analyze:** The cleaned dataset can be explored in Power BI to identify patterns in job demand and requirements.

## Technology stack

- **Python** — scraping workflow and data processing
- **Requests** — HTTP requests to job-search pages
- **BeautifulSoup** — HTML parsing and field extraction
- **pandas** — tabular data preparation and CSV/Excel handling
- **Excel** — cleaned, structured dataset
- **Power BI** — interactive job-market reporting (`jobPosting_dashboard.pbix`)

## Repository files

| File | Description |
|---|---|
| `jobPosting.py` | Python scraper for job-search listings |
| `jobPosting_dashboard.pbix` | Power BI dashboard file |

## Dataset structure


### `jobPosting_data`

One row per job posting, with 8,835 rows and these fields:

| Column | Description |
|---|---|
| `job_category` | Search/job category associated with the listing |
| `job_titles` | Job title |
| `jobs_link` | Job-posting URL; used as the duplicate-check key |
| `companies` | Company name |
| `companies_links` | Company profile URL, where available |
| `City` | Listing city |
| `Country` | Listing country |
| `jobs_type` | Employment type |
| `Career_Level` | Career/experience level |
| `workplaces` | Workplace arrangement |

### `skills`

A separate job-to-skill table with 54,681 rows and two fields:

| Column | Description |
|---|---|
| `jobs_link` | Job URL used to associate the skill with a posting |
| `skills_list` | Skill label extracted for that posting |

The two sheets can be related using `jobs_link`. This structure supports skill-frequency analysis without storing multiple skills in a single job-level cell.


## Potential business value

The dataset provides a practical foundation for:

- **Job seekers:** identifying high-volume locations, common career levels, and frequently requested skills.
- **Career development:** prioritizing skills that recur across collected vacancies, while checking relevance to a target role.
- **Recruitment and HR analysis:** comparing job categories, employer activity, and work arrangements within the collected sample.
- **Market reporting:** monitoring how the composition of collected listings changes when the scraping and cleaning process is rerun consistently over time.

The results describe patterns in the collected listings; they do not by themselves establish hiring outcomes, salary levels, or causal effects on employment.

