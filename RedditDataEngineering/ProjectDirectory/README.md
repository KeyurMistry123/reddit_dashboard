# Reddit Data Engineering Project

This project demonstrates a complete end-to-end data engineering pipeline using Reddit data. It covers extraction from the Reddit API, ETL orchestration with Apache Airflow, storage in PostgreSQL, optional upload to AWS S3, and data cleaning for analytics or visualization (e.g., with Power BI).

## Features & Architecture
- **Extraction:** Fetches hot posts from the r/Python subreddit using the Reddit API (via PRAW).
- **Orchestration:** Uses Apache Airflow (Dockerized) to schedule and manage ETL tasks.
- **Database:** Stores raw Reddit post data in a local PostgreSQL database.
- **Cloud Storage (Optional):** Uploads extracted data to AWS S3 (if configured).
- **Data Cleaning:** Cleans and enriches the data for downstream analytics.
- **Visualization:** Data can be visualized in Power BI or other BI tools.

## Project Structure
- `dags/` - Airflow DAGs for orchestrating the ETL pipeline
- `scripts/` - Python scripts for extraction, loading, and S3 upload
- `data/` - Local storage for raw and cleaned CSV data
- `config/` - Configuration files (API credentials, S3 bucket, etc.)
- `data_cleaner.py` - Script to clean and enrich the extracted Reddit data

## Setup & Prerequisites
1. **Install Docker Desktop** (for running Airflow and PostgreSQL containers)
2. **Clone this repository** and navigate to the `ProjectDirectory` folder:
   ```sh
   git clone <repo-url>
   cd ProjectDirectory
   ```
3. **Configure Reddit API credentials:**
   - Edit `config/config.json` and fill in your Reddit API credentials and (optionally) your S3 bucket name:
     ```json
     {
       "reddit_client_id": "<your_client_id>",
       "reddit_client_secret": "<your_client_secret>",
       "reddit_user_agent": "<your_user_agent>",
       "s3_bucket": "<your_s3_bucket>"
     }
     ```
   - [Create a Reddit app](https://www.reddit.com/prefs/apps) to get these credentials.
4. **(Optional) AWS S3 Setup:**
   - If you want to upload data to S3, ensure your AWS credentials are available in `~/.aws/credentials` or via environment variables. No access keys are stored in the codebase.

## How to Run the Pipeline
1. **Start the services:**
   ```sh
   docker-compose up
   ```
   This will start Airflow (webserver & scheduler) and PostgreSQL.
2. **Access Airflow UI:**
   - Open [http://localhost:8080](http://localhost:8080) in your browser.
   - Trigger the `reddit_etl` DAG to run the pipeline.
3. **Data Cleaning (optional):**
   - After extraction, run the data cleaner to generate an enriched CSV:
     ```sh
     python data_cleaner.py
     ```
   - Output: `data/reddit_posts_cleaned.csv` with columns: `id, title, score, created_datetime, created_date, title_word_count`
4. **Visualization:**
   - Use Power BI or any BI tool to connect to the cleaned CSV or PostgreSQL for analytics.

## Scripts Overview
- `scripts/extract_reddit.py` - Extracts hot posts from r/Python and saves to CSV
- `scripts/load_to_postgres.py` - Loads extracted data into PostgreSQL
- `scripts/upload_to_s3.py` - Uploads CSV to S3 (if configured)
- `data_cleaner.py` - Cleans and enriches the raw Reddit data

## Requirements
- All dependencies are managed via Docker and `requirements.txt`:
  - apache-airflow==2.8.0
  - psycopg2-binary==2.9.3
  - praw==7.7.1
  - pandas==1.5.3
  - boto3==1.34.84

## Notes
- No AWS access keys or secrets are stored in the codebase. Use standard AWS credential management.
- The pipeline is modular and can be extended for other subreddits or data sources.
- For any issues, please open an issue or discussion in the repository. 