import requests
import pandas as pd

# API credentials
app_id = "3180d5a9"
app_key = "bb5bbc6812c3541e95e49aa8b0ef7c07"

jobs = []

# Loop through multiple pages (500 jobs approx)
for page in range(1, 11):  # 10 pages × 50 results = ~500 jobs

    url = f"https://api.adzuna.com/v1/api/jobs/ca/search/{page}?app_id={app_id}&app_key={app_key}&results_per_page=50&what=data"

    response = requests.get(url)
    data = response.json()

    for job in data["results"]:

        company = job.get("company", {})
        location = job.get("location", {})
        category = job.get("category", {})

        jobs.append({
            "title": job.get("title", "Unknown"),
            "company": company.get("display_name", "Unknown"),
            "location": location.get("display_name", "Unknown"),
            "created": job.get("created", "Unknown"),
            "category": category.get("label", "Unknown"),
            "salary_min": job.get("salary_min"),
            "salary_max": job.get("salary_max")
        })

# Create DataFrame
df = pd.DataFrame(jobs)

# Save CSV
df.to_csv("live_jobs.csv", index=False)

print("CSV updated successfully with ~500 rows")