# Financial-Data-Analysis-and-Pipeline-using-PySpark-on-Databricks

## Overview

This project is about analyzing financial data using PySpark on Databricks. I started working on it right after learning PySpark and Databricks on DataCamp. The data we used is in a file called Fraudulent_E-Commerce_Transaction_Data.csv. First, we put this file into an S3 bucket, then we used Apache Spark on Databricks to analyze it. The project includes steps like bringing in the data, working with it, and automating the analysis.

During this project, I had some trouble reading the data. No matter what I tried, I kept getting empty values, which made it hard to do the analysis. What's interesting is, when I tried reading the data with pandas and Excel, everything was fine. This difference caused a big problem in moving forward with my analysis.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Prerequisites

Before you begin, ensure you have the following:

- AWS account with S3 access
- Databricks account
- Python 3.7 or later
- `boto3` library
- `dotenv` library

## Setup Instructions

### Step 1: Clone the Repository

Clone this repository to your local machine using:

```bash
git clone https://github.com/yourusername/Financial-Data-Analysis-and-Pipeline-using-PySpark-on-Databricks.git
cd Financial-Data-Analysis-and-Pipeline-using-PySpark-on-Databricks
```

### Step 2: Set Up Environment Variables

Create a .env file in the root directory and add your AWS credentials:

```bash
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
```

### Step 3: Install Required Libraries

Install the required Python libraries using pip:

```bash
pip install boto3 python-dotenv
```

### Step 4: Upload Dataset to S3

Run the s3_bucket.py script to upload the dataset to your S3 bucket:

```bash
python3 s3_bucket.py
```

### Step 5: Connect to Databricks

Use the Databricks CLI or the web interface to create a new notebook.

## Usage

1. Upload the dataset to your S3 bucket using the s3_bucket.py script.
2. Connect to Databricks and create a new notebook.
3. Use the provided PySpark code to read and analyze the dataset.

## Project Structure

```bash
Financial-Data-Analysis-and-Pipeline-using-PySpark-on-Databricks/
├── Dataset/
│   └── Fraudulent_E-Commerce_Transaction_Data.csv
├── .env
├── .gitattributes
├── .gitignore
├── README.md
├── financial_analysis.ipynb
├── requirement.txt
├── s3_bucket.py
└── vscode/
```

## Contributing

Contributions are welcome. Please fork the repository and create a pull request with your changes.