import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv'}

allowed_month = ["january", "february", "march", "april", "may", "june", "all"]

allowed_day = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "all"]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    selected_city = None
    selected_month = None
    selected_day = None

    print('Hello! Let\'s explore some US bikeshare data!\n')

    while selected_city is None or selected_month is None or selected_day is None:
        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        if selected_city is None:
            city = input(
                "Please choose on of the following cities:\nChicago\nNew York city\nWashington\n\ncity:").lower()
            if city in CITY_DATA:
                selected_city = city
            else:
                print("\n********************************************************")
                print("**** Please enter one of the cities mentioned above ****")
                print("********************************************************\n")
                continue

        # get user input for month (all, january, february, ... , june)
        if selected_month is None:
            month = input(
                "Please type which month (only from the first half of the year)"
                " you want to analysis or simply type 'all' for all the months: ").lower()
            if month in allowed_month:
                selected_month = month
            else:
                # error code
                print("\n***********************************************************************")
                print("**** Please enter a valid Month or type 'all' for all on the month ****")
                print("***********************************************************************\n")
                continue

        if selected_day is None:
            # get user input for day of week (all, monday, tuesday, ... sunday)
            day = input("please type which day you want to analysis or simply type 'all' for the whole week: ").lower()
            if day in allowed_day:
                selected_day = day
            else:
                print("\n*******************************************************************")
                print("**** Please enter a valid day or type 'all' for the whole week ****")
                print("*******************************************************************\n")
    print('-' * 40)
    return selected_city, selected_month, selected_day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA.get(city))

    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["months"] = df["Start Time"].dt.month
    df["days"] = df["Start Time"].dt.day_name()

    if month != "all":
        df = df[df["months"] == allowed_month.index(month) + 1]
    if day != "all":
        df = df[df["days"] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_month = df["months"].mode()[0] - 1
    print("The Most Common Month is :", allowed_month[most_month].title())

    # display the most common day of week
    most_day = df["days"].mode()[0]
    print("The Most Common Day of The week is :", most_day.title())

    # display the most common start hour
    df["hours"] = df["Start Time"].dt.hour
    most_hour = df["hours"].mode()[0]
    print("The Most Common Hour is :", most_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_start_station = df["Start Station"].mode()
    print("The Most Commonly used Start Station is:", most_start_station[0])

    # display most commonly used end station
    most_end_station = df["End Station"].mode()
    print("The Most Commonly Used End Station is:", most_end_station[0])

    # display most frequent combination of start station and end station trip
    most_combination = df[["Start Station", "End Station"]].value_counts()
    print("The Most Frequent Combination of Start and End Stations is:\n", most_combination.head(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df["Trip Duration"].sum()
    print("The Total Duration of a Trips is:", total_time, "seconds")

    # display mean travel time
    mean_time = df["Trip Duration"].mean()
    print("The Mean Duration of a Trip is:", mean_time, "seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_count = df["User Type"].value_counts()
    print("User Count:\n", user_count, "\n")

    # Display counts of gender
    try:
        gender_count = df["Gender"].value_counts()
        print("Gender Count:\n", gender_count, "\n")
    except Exception:
        print("\nGender Count:")
        print("*****************************************")
        print("**** this Statistic is not available ****")
        print("*****************************************\n")

    # Display earliest, most recent, and most common year of birth
    try:
        print("Birth Year Statistics:")
        early_brith_date = int(df["Birth Year"].min())
        late_brith_date = int(df["Birth Year"].max())
        common_brith_date = int(df["Birth Year"].mode()[0])
        print("Earliest Year of Birth is :", early_brith_date)
        print("The Most Recent Year of Birth is:", late_brith_date)
        print("The Most Common Year of Birth is:", common_brith_date)
    except Exception:
        print("*****************************************")
        print("**** This Statistic is not Available*****")
        print("*****************************************\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40, "\n")


def individual_data(df):
    view_display = None
    start_log = 0
    while view_display is None or view_display == "yes":
        view_display = input("Would you like to view 5 rows of individual trip data? Enter yes or no? \n").lower()
        if view_display == "yes":
            print(df.iloc[start_log:start_log + 5])
            start_log += 5
        elif view_display == "no":
            break
        else:
            view_display = None
            print("\n****************************************")
            print("*** Please answer by yes or no only! ***")
            print("****************************************\n")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        individual_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("\n****************************************")
            print("**** Thank you for using my Program ****")
            print("****************************************\n")
            break


if __name__ == '__main__':
    main()
