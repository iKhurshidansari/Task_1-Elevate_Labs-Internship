# 🩺 Task 1: Data Cleaning and Preprocessing – Medical Appointment No Shows

## 📄 Dataset Used:
**Medical Appointment No Shows** – A dataset from Kaggle containing information about over 100,000 medical appointments in Brazil, including whether patients showed up.

---

## 🧹 Data Cleaning Performed:

1. **Removed Duplicates**
   - Duplicate rows were dropped using `df.drop_duplicates()`.

2. **Handled Missing Values**
   - Forward filled missing values using `df.ffill()`.

3. **Standardized Text Columns**
   - Converted `Gender` and `No-show` columns to lowercase and stripped spaces for uniformity.

4. **Converted Date Columns**
   - `ScheduledDay` and `AppointmentDay` converted to `datetime` format.
   - Timezone removed from `ScheduledDay` using `.dt.tz_localize(None)`.
   - Time portion removed from `AppointmentDay` using `.dt.date`.

5. **Cleaned Column Headers**
   - Renamed all columns to lowercase with underscores using:
     ```python
     df.columns = df.columns.str.lower().str.replace(" ", "_")
     ```

6. **Fixed Data Types**
   - `age`, `patientid`, and `appointmentid` converted to appropriate `int64` or `str` formats as needed.
   - Large integers like `patientid` and `appointmentid` were formatted to remove scientific notation.

7. **Sorted Data**
   - Final dataset was sorted first by `appointment_day`, then by `appointment_id` using:
     ```python
     df.sort_values(by=['appointment_day', 'appointment_id'], ascending=[True, True])
     ```

---

## 🛠 Tools Used:
- Python
- Pandas
- Jupyter Notebook

---

## 📁 Files Included:
- `medical-appointment-no-shows.ipynb` → Full notebook with data cleaning steps.
- `cleaned_dataset.csv` → Final cleaned version of the dataset.
- `README.md` → This summary of the task.

---

## ✅ Outcome:
- A fully cleaned dataset ready for further analysis or modeling.
- Gained hands-on experience in handling missing data, date formatting, text standardization, and sorting.

---

## 📌 Task Submission
Submitted as part of the **Data Analyst Internship - Task 1: Data Cleaning & Preprocessing**

