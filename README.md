# Wuzzuf Job Market Analysis | Python Web Scraping, Data Preparation & Power BI

An end-to-end job-market analytics project built around job listings collected from **Wuzzuf**. The project uses Python to collect job-posting details across multiple career categories, prepares the collected information in Excel, and provides a dataset for exploring hiring patterns, employer demand, locations, career levels, work arrangements, and required skills.

The objective is to turn unstructured job-board listings into an analysis-ready dataset that can help job seekers understand where opportunities are concentrated and which skills appear most frequently in employer requirements.

> **Dataset snapshot:** The figures below describe the supplied cleaned workbook, not live Wuzzuf listings. Job-board content changes over time, and the workbook does not include a verified collection date.

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

1. **Collect:** Python sends HTTP requests to Wuzzuf job-search pages for configured job categories.
2. **Parse:** BeautifulSoup extracts job titles, job URLs, company names and URLs, locations, job types, career levels, skills, and workplace arrangements.
3. **Structure:** pandas organizes the extracted information into tabular data.
4. **Avoid duplicate appends:** The scraper checks existing CSV files and appends only rows whose job URLs are not already present.
5. **Prepare:** The supplied Excel workbook separates job-level information from the job-to-skill records.
6. **Analyze:** The cleaned dataset can be explored in Power BI to identify patterns in job demand and requirements.

## Technology stack

- **Python** — scraping workflow and data processing
- **Requests** — HTTP requests to job-search pages
- **BeautifulSoup** — HTML parsing and field extraction
- **pandas** — tabular data preparation and CSV/Excel handling
- **Excel** — cleaned, structured dataset
- **Power BI** — interactive job-market reporting (`wuzzuf_dashboard.pbix`)

## Repository files

| File | Description |
|---|---|
| `wuzzuf.py` | Python scraper for Wuzzuf job-search listings |
| `wuzzuf_data_cleaning.xlsx` | Cleaned workbook containing job-level data and a separate skills table |
| `wuzzuf_dashboard.pbix` | Power BI dashboard file |

## Dataset structure

The Excel workbook contains two sheets:

### `Wuzzuf_data`

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

## How to run the scraper

### 1. Install dependencies

```bash
pip install requests beautifulsoup4 pandas
```

### 2. Configure the output directory

Open `wuzzuf.py` and update the `file_path` assignment to a directory on your machine. The supplied script currently contains a Windows-specific absolute path, so it must be changed before running on another computer.

### 3. Run

```bash
python wuzzuf.py
```

The script iterates through its configured categories, determines the number of result pages, extracts listing information, and writes category-level CSV files. Existing files are read so that postings with URLs already collected are not appended again.

### 4. Open the analysis files

Use `wuzzuf_data_cleaning.xlsx` for the prepared tables and open `wuzzuf_dashboard.pbix` in Power BI Desktop to explore the dashboard.

## Important implementation notes and limitations

- **Website structure can change:** The scraper relies on Wuzzuf HTML element classes. Changes to the website may require updates to the BeautifulSoup selectors.
- **Pagination assumption:** The script assumes 15 job listings per result page when calculating the number of pages.
- **Output path:** The output directory is hard-coded and must be configured locally before execution.
- **Category consistency:** The categories in the supplied cleaned workbook are not an exact match to the category list in the supplied scraper. Reconcile category names and collection scope before attempting to reproduce the workbook from a fresh scrape.
- **Snapshot, not a live feed:** The Excel figures are a snapshot of the supplied data. They should not be interpreted as current vacancy counts or a complete census of the labor market.
- **Missing values and labels:** Some workplace values are `Not specified`, and skill labels may include spelling, capitalization, or naming variants. Skill normalization and further validation can improve comparisons.
- **Responsible collection:** Before running the scraper, review Wuzzuf's current terms, applicable access rules, and `robots.txt`. Use reasonable request rates and do not treat publicly viewable pages as permission to ignore site policies.

## Potential business value

The dataset provides a practical foundation for:

- **Job seekers:** identifying high-volume locations, common career levels, and frequently requested skills.
- **Career development:** prioritizing skills that recur across collected vacancies, while checking relevance to a target role.
- **Recruitment and HR analysis:** comparing job categories, employer activity, and work arrangements within the collected sample.
- **Market reporting:** monitoring how the composition of collected listings changes when the scraping and cleaning process is rerun consistently over time.

The results describe patterns in the collected Wuzzuf listings; they do not by themselves establish hiring outcomes, salary levels, or causal effects on employment.

## Future improvements

- Replace hard-coded paths with command-line arguments or configuration settings.
- Add request timeouts, retries, status-code checks, and structured logging.
- Add robust parsing and validation for missing or changed HTML fields.
- Normalize skill labels and job-category names.
- Record collection timestamps to enable trend analysis across snapshots.
- Add automated data-quality checks and reproducible cleaning steps.
- Capture additional fields, such as salary, only when reliably available and permitted.

## Disclaimer

This project is intended for educational and analytical purposes. Wuzzuf is the source of the job listings; this project is not affiliated with or endorsed by Wuzzuf. Respect the website's terms and applicable laws when accessing or processing its content.
