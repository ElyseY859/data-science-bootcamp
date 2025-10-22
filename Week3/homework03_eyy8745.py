import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

url = 'Brooklyn_Bridge_Automated_Pedestrian_Counts_Demonstration_Project_20251021.csv'
df = pd.read_csv(url)

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

df['hour_beginning'] = pd.to_datetime(df['hour_beginning'], errors='coerce')

df['pedestrians'] = df['pedestrians'].astype(str).str.replace(',', '', regex=True).astype(float)

df_2019 = df[df['hour_beginning'].dt.year == 2019].copy()

df_weekdays = df_2019[df_2019['hour_beginning'].dt.dayofweek < 5].copy()

df_weekdays['day_of_week'] = df_weekdays['hour_beginning'].dt.day_name()
weekday_counts = df_weekdays.groupby('day_of_week')['pedestrians'].mean()
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

plt.figure(figsize=(8,5))
plt.plot(weekday_order, weekday_counts[weekday_order], marker='o', color='navy')
plt.title('Average Pedestrian Counts on Brooklyn Bridge (Weekdays, 2019)')
plt.xlabel('Day of the Week')
plt.ylabel('Average Pedestrian Count')
plt.grid(True)
plt.show()

df_2019['temperature'] = pd.to_numeric(df_2019['temperature'], errors='coerce')
df_2019['precipitation'] = pd.to_numeric(df_2019['precipitation'], errors='coerce')

weather_avg = df_2019.groupby('weather_summary')['pedestrians'].mean().sort_values(ascending=False)
print("\nAverage Pedestrian Count by Weather Summary:")
print(weather_avg)

numeric_cols = ['pedestrians', 'temperature', 'precipitation']
corr = df_2019[numeric_cols].corr()

plt.figure(figsize=(6,5))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix: Weather vs Pedestrian Counts (2019)')
plt.show()

def categorize_time(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'

df_2019['hour'] = df_2019['hour_beginning'].dt.hour
df_2019['time_of_day'] = df_2019['hour'].apply(categorize_time)

time_of_day_avg = (
    df_2019.groupby('time_of_day')['pedestrians']
    .mean()
    .reindex(['Morning', 'Afternoon', 'Evening', 'Night'])
)

plt.figure(figsize=(8,5))
time_of_day_avg.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Average Pedestrian Activity by Time of Day (2019)')
plt.xlabel('Time of Day')
plt.ylabel('Average Pedestrian Count')
plt.show()
