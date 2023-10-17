import pandas as pd
import time

try:
    import pandas
except ImportError:
    print("Pandas is not installed. You can install it by running:")
    print("pip install pandas")

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June']
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    
    city = input("Would you like to see data for Chicago, New York City, or Washington? ").lower()
    
    while city not in CITY_DATA:
        city = input("Invalid city name. Please choose from the provided options: ").lower()
    
    filter_choice = input("Would you like to filter the data by month, day, or not at all? ").lower()
    
    if filter_choice == 'month':
        month = input("Which month? (January, February, March, April, May, June) ").title()
        while month not in MONTHS:
            month = input("Invalid month. Please choose a valid month: ").title()
    else:
        month = 'all'
    
    if filter_choice == 'day':
        day = input("Which day? (Monday, Tuesday, ..., Sunday) ").title()
        while day not in DAYS:
            day = input("Invalid day. Please choose a valid day: ").title()
    else:
        day = 'all'
    
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.strftime('%B')
    df['day_of_week'] = df['Start Time'].dt.strftime('%A')
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day]
    
    return df

def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    common_month = df['month'].mode()[0]
    common_day = df['day_of_week'].mode()[0]
    common_hour = df['hour'].mode()[0]
    
    print("Most common month:", common_month)
    print("Most common day of week:", common_day)
    print("Most common start hour:", common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    common_start_station = df['Start Station'].mode()[0]
    common_end_station = df['End Station'].mode()[0]
    print("Most common start station:", common_start_station)
    print("Most common end station:", common_end_station)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    total_travel_time = df['Trip Duration'].sum()
    mean_travel_time = df['Trip Duration'].mean()
    print("Total travel time:", total_travel_time)
    print("Mean travel time:", mean_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    user_types = df['User Type'].value_counts()
    print("Counts of user types:\n", user_types)
    
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of gender:\n", gender_counts)
    else:
        print("\nGender data is not available for this city.")
    
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print("\nEarliest birth year:", int(earliest_birth_year))
        print("Most recent birth year:", int(recent_birth_year))
        print("Most common birth year:", int(common_birth_year))
    else:
        print("\nBirth year data is not available for this city.")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    i = 0
    while True:
        show_data = input("Would you like to see 5 lines of raw data? (yes/no) ").lower()
        if show_data == 'yes':
            print(df.iloc[i:i+5])
            i += 5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




