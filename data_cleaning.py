import pandas as pd

# Load the dataset
df = pd.read_csv("KaggleV2-May-2016.csv")  # Replace with your actual file name if different

# 1. Handle missing values
df.ffill(inplace=True)  # Forward fill any missing values

# 2. Remove duplicates
df.drop_duplicates(inplace=True)

# 3. Standardize text values
df['Gender'] = df['Gender'].str.lower().str.strip()
df['No-show'] = df['No-show'].str.lower().str.strip()

# 4. Convert date columns to datetime
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
df['ScheduledDay'] = df['ScheduledDay'].dt.tz_localize(None)  # Remove timezone info

df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])
df['AppointmentDay'] = df['AppointmentDay'].dt.date  # Remove time, keep only date

# 5. Clean column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# 6. Fix data types
df['age'] = pd.to_numeric(df['age'], errors='coerce').fillna(0).astype(int)
df['patientid'] = df['patientid'].astype('int64')
df['appointmentid'] = df['appointmentid'].astype('int64')

# 7. Sort by appointment day and appointment ID
df = df.sort_values(by=['appointmentday', 'appointmentid'], ascending=[True, True])
df.reset_index(drop=True, inplace=True)

# 8. Save the cleaned dataset
df.to_csv("KaggleV2-May-2016.csv.csv", index=False)

print("✅ Data cleaning completed. Cleaned dataset saved as 'KaggleV2-May-2016.csv'.")
