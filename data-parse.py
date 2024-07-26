from bs4 import BeautifulSoup
import pandas as pd

# Load the HTML file
with open('C:\\Users\\lefeh\\Downloads\\takeout-20240615T113123Z-001\\Takeout\\My Activity\\Search\\MyActivity.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Extract data
activities = []
for item in soup.find_all('div', class_='outer-cell'):
    content_cell = item.find('div', class_='content-cell')
    
    if content_cell:
        time_elem = content_cell.find('span', class_='metadata')
        activity_elem = content_cell.find('a')
        
        if time_elem and activity_elem:
            time = time_elem.text
            activity = activity_elem.text
            activities.append((time, activity))

# Create a DataFrame
df = pd.DataFrame(activities, columns=['Time', 'Activity'])

# Convert Time to datetime
df['Time'] = pd.to_datetime(df['Time'], errors='coerce')

# Drop rows with invalid dates
df.dropna(subset=['Time'], inplace=True)

# Save to CSV for further analysis if needed
df.to_csv('activities.csv', index=False)

print(df.head())