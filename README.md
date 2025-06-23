# 🩺 Task 1: Data Cleaning and Preprocessing – Medical Appointment No Shows

## 📄 Dataset Used:
**Medical Appointment No Shows** – A dataset from Kaggle containing information about over 100,000 medical appointments in Brazil, including whether patients showed up.

---

## 🧹 Data Cleaning Performed:

### 1. ✅ Handled Missing Values
- Used forward fill (ffill) to fill any missing entries.

### 2. ✅ Removed Duplicate Records
- Duplicate rows were removed using drop_duplicates().

### 3. ✅ Standardized Text Data
- Converted text values in the Gender and No-show columns to lowercase and stripped any whitespace for consistency.

### 4. ✅ Date Conversion
- ScheduledDay converted to datetime and timezone info (+00:00) was removed using .dt.tz_localize(None).
- AppointmentDay was also converted to datetime, and the time portion was removed using .dt.date.

### 5. ✅ Column Name Formatting
- Renamed all column headers to lowercase with underscores (e.g., "AppointmentID" → "appointmentid").

### 6. ✅ Fixed Data Types
- Converted age to integer using astype(int) after handling missing or non-numeric entries.
- Converted patientid and appointmentid to int64 to remove scientific notation and ensure numeric sorting.

### 7. ✅ Sorted the Dataset
- Sorted by appointmentday (earliest date first), then by appointmentid (lowest ID first).

### 8. ✅ Saved the Cleaned Dataset
- Cleaned dataset was saved as KaggleV2-May-2016.csv.csv (note: possibly rename this for clarity).

---

## 🛠 Tools Used:
- Python
- Pandas
- Jupyter Notebook

---

## 📁 Files in the Repository:
- data_cleaning.py: Python script containing the full cleaning logic.
- KaggleV2-May-2016.csv: Original dataset.
-  Cleaned dataset renamed to (cleaned_medical_appointments)
- README.md: Documentation of cleaning steps performed.

---

## ✅ Outcome:
- A fully cleaned dataset ready for further analysis or modeling.
- Gained hands-on experience in handling missing data, date formatting, text standardization, and sorting.

---

## 📌 Task Submission
Submitted as part of the **Data Analyst Internship - Task 1: Data Cleaning & Preprocessing**

