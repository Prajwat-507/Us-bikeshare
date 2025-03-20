import pandas as pd
import numpy as np
import time
from datetime import timedelta

import seaborn as sns
import matplotlib.pyplot as plt

import streamlit as st
from streamlit_option_menu import option_menu

# Data
cleaned_city_data = {'chicago': 'data/chicago_cleaned.csv',
      'new york city': 'data/new_york_city_cleaned.csv',
      'washington': 'data/washington_cleaned.csv'}

# df = pd.read_csv(CLEANED_CITY_DATA['chicago'])
# print(df.head(5))


# Web Ui header
st.header("US Bikeshare Statistics and Insights", divider="gray")

# Side Bar
with st.sidebar:
     selected = option_menu(
          menu_title = "Main menu",
          options = ["Show Stats", "Get Visual Insight", "See Raw Data", "About"],
          default_index=0,
    )
     

# 1- Get Filters
def get_filters():

    # Set title
    st.title("US Bikeshare Data Explorer")

    st.markdown("### Select Filters to Explore the Dataset:")

    # City selection
    city = st.selectbox(
        "Select a city:",
        ['Chicago', 'New York City', 'Washington']
    ).lower()

    if city == 'Select a city':
        st.warning("Please select a city to proceed.")
        st.stop()  # stops further execution until a city is selected
    else:
        city = city.lower()


    # Month selection
    month = st.selectbox(
        "Select a month:",
        ['All', 'January', 'February', 'March', 'April', 'May', 'June']
    ).lower()

    # Day selection
    day = st.selectbox(
        "Select a day of the week:",
        ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    ).lower()

    return city, month, day


# 2- Load Data
def load_data(city, month, day):

    # Set a spinner with 3 sec delay
    with st.spinner("🔄 Loading data... Please wait..."):
        time.sleep(3)
         
        # Load data based on city
        df = pd.read_csv(cleaned_city_data[city])
        select_df = df
        
        # load data based on month & day
        if(month!='all'):
            select_df = df[df['Month'].isin([month])]

        if(day!='all'):
            select_df = select_df[select_df['Day'].isin([day])]
        
        return select_df

# 3- Time Stats
def time_stats(df):

    # Set subheader
    st.subheader("🕒 Calculating Time Statistics")

    # Set a spinner with 1 sec delay
    with st.spinner('\nCalculating The Most Frequent Times of Travel...\n'):
        time.sleep(1)

        # display the most common month
        common_month = df['Month'].value_counts().idxmax()
        
        
        # display the most common day of week
        common_week = df['Day'].value_counts().idxmax()
        
        # display the most common start hour
        common_starthr = df['Start time'].value_counts().idxmax()

        # display most common end hour
        common_endhr = df['End time'].value_counts().idxmax()


        hours, minutes, seconds = common_starthr.split(':')
        e_hours, e_minutes, e_seconds = common_endhr.split(':')
        
        formatted_time = f"{hours}hr" + \
                    (f" {minutes}min" if int(minutes) > 0 else "") + \
                    (f" {seconds}sec" if int(seconds) > 0 else "")
        
        e_formatted_time = f"{e_hours}hr" + \
                 (f" {e_minutes}min" if int(e_minutes) > 0 else "") + \
                 (f" {e_seconds}sec" if int(e_seconds) > 0 else "")
        
        # print(f"Most Common Month        : {common_month.title()}")
        # print(f"Most Common Day of Week  : {common_week.title()}")
        # print(f"Most Common Start Hour   : {formatted_time}")

        st.write(f"📅 **Most Common Month:** {common_month.title()}")
        st.write(f"📆 **Most Common Day of Week:** {common_week.title()}")
        st.write(f"⏰ **Most Common Start Hour:** {formatted_time}")
        st.write(f"⏰ **Most Common End Hour:** {e_formatted_time}")

# Station Stats
def station_stats(df):

    # Set subheader
    st.subheader("📊 Calculating Station Statistics")

    # Set a spinner with 1 sec delay
    with st.spinner("⏳ Calculating The Most Popular Stations and Trips..."):
        time.sleep(1)

        # display most commonly used start station
        common_startSt = df['Start Station'].value_counts().idxmax()

        # display most commonly used end station
        common_EndSt = df['End Station'].value_counts().idxmax()

        # display most frequent combination of start station and end station trip
        common_trip = df[['Start Station', 'End Station']].value_counts().idxmax()

        # Show results
        st.write(f"🛫 **Most Common Start Station**: {common_startSt}")
        st.write(f"🛬 **Most Common End Station**: {common_EndSt}")
        st.write(f"🔁 **Most Frequent Trip Combination**: {common_trip[0]} ➡️ {common_trip[1]}")


# trip_duration_stats
def trip_duration_stats(df):

    #Set subheader
    st.subheader("🕒 Trip Duration Statistics")

    # Set a spinner with 1 sec delay
    with st.spinner("⏳ Calculating Trip Durations..."):
        time.sleep(1)

       # Total and average duration
        total_duration = df['Trip Duration'].sum()
        mean_duration = df['Trip Duration'].mean()

        # Min and max durations
        min_duration = df['Trip Duration'].min()
        max_duration = df['Trip Duration'].max()

        # Average duration by user type
        avg_trip_user_type = df.groupby('User Type')['Trip Duration'].mean()

        # Display results
        st.write(f"🕰 **Total Travel Time:** {format_duration(total_duration)}")
        st.write(f"⚖️**Average Travel Time:** {format_duration(mean_duration)}")
        st.write(f"➗**Minimum Travel Time:** {format_duration(min_duration)}")
        st.write(f"➗**Maximum Travel Time:** {format_duration(max_duration)}")
        if 'Subscriber' in avg_trip_user_type:
            st.write(f"⚖️**Average Trip by Subscriber** : {format_duration(avg_trip_user_type['Subscriber'])}")
        if 'Customer' in avg_trip_user_type:
            st.write(f"⚖️**Average Trip by Customer**   : {format_duration(avg_trip_user_type['Customer'])}")


# Helper function to format duration in seconds into 'dd days hh hr ss min'
def format_duration(seconds):
    #Using timedelta function to convert seconds into days format
    duration = timedelta(seconds=int(seconds))
    days = duration.days
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60

    time_str = (f"{days} days" if days > 0 else "") + \
               (f" {hours:.0f} hr" if hours > 0 else "") + \
               (f" {minutes:.0f} min" if minutes > 0 else "")
    
    return time_str.strip()


#User Stats
def user_stats(df):
    # Set subheader
    st.subheader("👤 User Statistics")

    # Set a spinner with 1 sec delay
    with st.spinner("🔍 Calculating User Statistics..."):
        time.sleep(1)

        # Display counts of user types
        user_types = df['User Type'].value_counts()

        if user_types.empty:
            st.warning("⚠️ No user type data available.")
        else:
            st.write("**User Types:**")
            st.write(f"• Subscriber: {user_types.values[0] if len(user_types) > 0 else 'No Data'}")
            st.write(f"• Customer: {user_types.values[1] if len(user_types) > 1 else 'No Data'}")

        # Display counts of gender
        if 'Gender' in df.columns:
            gender_count = df['Gender'].value_counts()
            st.write("**Gender Distribution:**")
            st.write(gender_count)
        else:
            st.warning("⚠️ Gender data is not available in this dataset.")

        # Display earliest, most recent, and most common year of birth
        if 'Birth Year' in df.columns and not df['Birth Year'].isnull().all():
            earliest_yob = int(df['Birth Year'].min())
            most_recent_yob = int(df['Birth Year'].max())
            most_common_yob = int(df['Birth Year'].mode()[0])
            # Display avg age
            avg_age = df['Age'].mean()

            st.write("**Birth Year Statistics:**")
            st.write(f"👶 Earliest Year of Birth:    {earliest_yob}")
            st.write(f"🧒 Most Recent Year of Birth: {most_recent_yob}")
            st.write(f"👴 Most Common Year of Birth: {most_common_yob}")
            st.write(f"🎂 Average age: {avg_age:.0f}")
        else:
            st.warning("⚠️ Birth Year statistics are not available in this dataset.")



# Visual Insight for data

def showStats(city, month, day):
    df = load_data(city, month, day)

    st.markdown(f"### 📊 Showing Statistical Insights for:")
    st.markdown(f"**City:** {city.title()}  |  **Month:** {month.title()}  |  **Day:** {day.title()}")

    st.markdown("---")
    
    # Plot top N busiest stations on that day
    top_stations = df[['Start Station', 'End Station']].value_counts().head(10)
    station_labels = [f"{start} → {end}" for start, end in top_stations.index]

    fig1, ax1 = plt.subplots()
    sns.barplot(x=top_stations.values, y=station_labels, palette='viridis', ax=ax1)
    ax1.set_title('Top 10 Most Frequent Station Pairs')
    ax1.set_xlabel('Trip Count')
    ax1.set_ylabel('Station Pair')
    st.pyplot(fig1)

    st.markdown("---")

    # Trip duration vs User type
    fig2, ax2 = plt.subplots()
    sns.barplot(x='User Type', y='Trip Duration', data=df, palette='viridis', ax=ax2)
    ax2.set_title('How Much Time Do Subscribers Spend Riding vs Customers?')
    ax2.set_xlabel('User Type')
    ax2.set_ylabel('Trip Duration (sec)')
    st.pyplot(fig2)

    st.markdown("---")

def showStatsDay(city, month, day):
    df = load_data(city, month, day)

    st.markdown(f"### 📊 Showing Statistical Insights for:")
    st.markdown(f"**City:** `{city.title()}` &nbsp;&nbsp; | &nbsp;&nbsp; **Month:** `{month.title()}` &nbsp;&nbsp; | &nbsp;&nbsp; **Day:** `{day.title()}`")
    st.markdown("---")

    # Plot: Trip Duration vs Day
    fig1, ax1 = plt.subplots()
    sns.barplot(x=df['Day'], y=df['Trip Duration'], palette='viridis', ax=ax1)
    ax1.set_title('Usage According to Day')
    ax1.set_xlabel('Day')
    ax1.set_ylabel('Trip Duration (sec)')
    st.pyplot(fig1)

    # Plot: Grouped Bar Plot - User Type vs Day
    fig2, ax2 = plt.subplots()
    sns.countplot(data=df, x='Day', hue='User Type', ax=ax2)
    ax2.set_title('User Type vs Day')
    ax2.set_xlabel('Day of the Week')
    ax2.set_ylabel('Number of Trips')
    ax2.legend(title='User Type')
    ax2.tick_params(axis='x', rotation=0)
    st.pyplot(fig2)

    st.markdown("---")


def showStatsMonth(city, month, day):
    df = load_data(city, month, day)

    st.markdown(f"### 📊 Showing Statistical Insights for:")
    st.markdown(f"**City:** `{city.title()}` &nbsp;&nbsp; | &nbsp;&nbsp; **Month:** `{month.title()}` &nbsp;&nbsp; | &nbsp;&nbsp; **Day:** `{day.title()}`")
    st.markdown("---")

    # Plot 1: Trip Count per Month (Seasonal Patterns)
    fig1, ax1 = plt.subplots()
    sns.countplot(data=df, x='Month', ax=ax1)
    ax1.set_title('Seasonal Patterns Trips per Month')
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Trip Count')
    ax1.tick_params(axis='x', rotation=0)
    st.pyplot(fig1)

    # Plot 2: User Type Trends Over Months
    fig2, ax2 = plt.subplots()
    sns.countplot(data=df, x='Month', hue='User Type', ax=ax2)
    ax2.set_title('User Type Trends Over Months')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Trip Count')
    ax2.legend(title='User Type')
    ax2.tick_params(axis='x', rotation=0)
    st.pyplot(fig2)

    st.markdown("---")

if selected == "Show Stats":
    city,month,day=get_filters()

    if st.button("🚀 Show Statistics"):
        df = load_data(city, month, day)
        st.success("Data Loaded Successfully!")
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

if selected == "Get Visual Insight":
    city,month,day=get_filters()

    if st.button("📊 Show Visual Insights"):
        if day == 'all' and month == 'all':
            st.warning("Please select either a city or a month or both — not all for both.")
        else:
            if day != 'all' and month != 'all':
                showStats(city, month, day)
            elif day == 'all' and month != 'all':
                showStatsDay(city, month, day)
            elif day != 'all' and month == 'all':
                showStatsMonth(city, month, day)
            else:
                st.warning("**Available data is insufficient**")
    

if selected == "See Raw Data":
    city,month,day=get_filters()
    df = load_data(city, month, day)

    num_rows = st.number_input("Enter the number of rows you want to see", min_value=1, max_value=len(df), value=5, step=1)
    if st.button("📊 Show Raw Data"):
        st.write(df.head(num_rows))

if selected == "About":
    st.title("US Bikeshare Data Explorer")

    st.markdown("Over the past decade, bicycle-sharing systems have been growing in number and "
    "popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. "
    "This allows people to borrow a bike from point A and return it at point B, "
    "though they can also return it to the same location if they'd like to "
    "just go for a ride. Regardless, each bike can serve several users per day.Thanks to the rise in information technologies, "
    "it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also "
    "provide a wealth of data that can be used to explore how these bike-sharing systems are used.")

    st.markdown("""
        ## 📋 How to Use This Web App

        Welcome to the Bike Share Data Analysis App! Follow these steps to explore bike share usage patterns:

        ---

        ### 1️⃣ **View City Statistics**

        - Select **"Show Stats"** from the sidebar or menu.
        - Enter the following details:
        - **City**: Choose from Chicago, New York City, or Washington.
        - **Month**: Select a specific month (e.g., January, February, etc.) or choose "All".
        - **Day**: Select a specific day of the week or choose "All".
        - Click **Submit** to view:
        ##### ✅ Most Common Travel Times:
        - Most common **Month**
        - Most common **Day of the Week**
        - Most common **Hour of the Day**
        - Most common **End Hour**

        ##### ✅ Popular Stations and Trips:
        - Most common **Start Station**
        - Most common **End Station**
        - Most common **Trip** (Start Station ➝ End Station)
                
        ##### ✅ Trip Duration Statistics:
        - Total Travel Time
        - Average Travel Time
        - Minimum Travel Time
        - Maximum Travel Time
        - Average Trip Duration by **Subscribers**
        - Average Trip Duration by **Customers**

        ##### ✅ User Demographics:
        - Count of each **User Type** (Subscriber / Customer)
        - Count of **Gender** (only available for **Chicago & NYC**)
        - **Birth Year Insights** (only available for **Chicago & NYC**):
        - Earliest Year of Birth
        - Most Recent Year of Birth
        - Most Common Year of Birth
        - **Average Age**

        

        ### 2️⃣ **Visualize Statistics**

        - Select **"Visualize Stats"** from the sidebar/menu.
        - Choose how you'd like to visualize the data:
        - **Month & Day combination**
        - **Day only**
        - **Month only**
        - Select the appropriate filters.
        - View the charts and graphs generated for better insights.

        ---

        ### 3️⃣ **See Raw Data**

        - Select **"See Raw Data"** from the menu.
        - Choose your city, month, and day filters (like before).
        - Enter how many rows of raw data you want to see using the input box.
        - The selected number of rows will be displayed for you to explore individual records.

        ---

        ### 4️⃣ **Explore Freely**

        - You can go back and forth between the sections from the sidebar.
        - Change filters anytime to get different insights or explore another city.
        - Try different combinations to compare usage patterns.

        ---

        ### 🔍 Tip:
        Use the raw data view to get a feel of what the original data looks like, and then switch to visualization to make better sense of trends and patterns.

        Happy Exploring! 🚴‍♂️📊
        """)
        





