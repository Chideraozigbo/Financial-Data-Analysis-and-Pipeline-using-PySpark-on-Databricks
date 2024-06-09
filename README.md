# Financial-Data-Analysis-and-Pipeline-using-PySpark-on-Databricks

## Overview

This project demonstrates a data pipeline for financial data analysis using PySpark on Databricks. The dataset used is `Fraudulent_E-Commerce_Transaction_Data.csv`, which is uploaded to an S3 bucket and then analyzed using Apache Spark on Databricks. The pipeline includes data ingestion, processing, and analysis automation.

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
│   ├── Fraudulent_E-Commerce_Transaction_Data.csv
├── s3_bucket.py
├── .env
├── README.md
```

## Contributing

Contributions are welcome. Please fork the repository and create a pull request with your changes.