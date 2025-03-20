# Us-bikeshare
This project is an interactive **Streamlit web application** that explores US Bikeshare system data from **three major cities** — **Chicago**, **New York City**, and **Washington**. It allows users to filter and analyze bikeshare trends using multiple visual and statistical tools.

This repo also contains source **notebook** file.

## Project Structure
- 📁 US-Bikeshare-Project
  - 📒 notebook/       Contains jupiter source file for this project.
  - 📁 data/           Contains cleaned data only which is used for web app.
    - chicago_cleaned.csv
    - new_york_city_cleaned.csv
    - washington_cleaned.csv
- 🖥️ app.py            The main start file for the project
- ⚙️ requirements.txt

## How to Run the App

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/US-Bikeshare-Project.git
2. **Run These commands**
   ```bash
   cd US-Bikeshare-Project
   pip install -r requirements.txt
   streamlit run app.py

## Tech Stack
   **Pandas**
   **Numpy**
   **Seaborn**
   **Matplotlib**
   **Streamlit**

## About
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

### Statistics Computed

#### 1 Popular times of travel (i.e., occurs most often in the start time)
most common month
most common day of week
most common hour of day
most common end hour
most common start hour

#### 2 Popular stations and trip
most common start station
most common end station
most common trip from start to end (i.e., most frequent combination of start station and end station)

#### 3 Trip duration
total travel time
average travel time
average trip by user subscriber
average trip by customer

#### 4 User info
counts of each user type
counts of each gender (only available for NYC and Chicago)
earliest, most recent, most common year of birth (only available for NYC and Chicago)
average age (only available for NYC and Chicago)

### Link to web app
[Click here to open the US Bikeshare Stats Web App 🚴‍♂️](https://us-bikeshare-stats-p507.streamlit.app/)

### Output Screen shots

#### Output 1:
![ss_op_1](https://github.com/user-attachments/assets/719766a8-17ff-495b-805a-67edb547d209)
#### Output 2:
![ss_op_2](https://github.com/user-attachments/assets/923e0247-fcbb-4ccf-8775-68727a0a5fca)
#### Output 3:
![ss_op_3](https://github.com/user-attachments/assets/ae68f933-854a-40a1-81bf-0a117b03d9f2)
#### Output 4:
![ss_op_4](https://github.com/user-attachments/assets/b3ac568b-a203-4023-82e6-e931b1d217c4)
#### Output 5:
![ss_op_5](https://github.com/user-attachments/assets/01701d67-898a-4815-bca4-d4e6601797f2)


   

 

