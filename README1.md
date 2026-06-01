# Task 1: Data Cleaning and Preprocessing

## Objective

The objective of this task is to clean and prepare a raw dataset by handling missing values, removing duplicates, standardizing data formats, and ensuring the dataset is ready for further analysis.

## Dataset

**Dataset Name:** Customer Personality Analysis
**File Used:** marketing_campaign.csv
**Source:** Kaggle

## Tools Used

* Python 3.13
* Pandas Library

## Steps Performed

### 1. Data Loading

The dataset was loaded into Python using the Pandas library.

### 2. Missing Value Detection

Missing values were identified using the `isnull().sum()` function.

### 3. Missing Value Handling

The dataset contained 23 missing values in the Income column. These missing values were replaced with the mean value of the Income column.

### 4. Duplicate Removal

Duplicate records were identified and removed using the `drop_duplicates()` function.

### 5. Column Name Standardization

Column names were cleaned by:

* Converting all names to lowercase
* Removing extra spaces
* Using a consistent naming format

### 6. Data Validation

The dataset was checked again to ensure that all missing values had been handled successfully.

### 7. Saving the Cleaned Dataset

The cleaned dataset was saved as:

`cleaned_marketing_campaign.csv`

## Results

### Original Dataset

* Rows: 2240
* Columns: 29

### Missing Values Found

* Income: 23 missing values

### Missing Values After Cleaning

* All columns: 0 missing values

## Output Files

1. marketing_campaign.csv (Original Dataset)
2. cleaned_marketing_campaign.csv (Cleaned Dataset)
3. task1.py (Python Cleaning Script)

## Conclusion

The Customer Personality Analysis dataset was successfully cleaned and prepared for further analysis. Missing values were handled, duplicate records were removed, and column names were standardized. The resulting dataset is accurate, consistent, and suitable for data analysis and visualization tasks.
