import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    persons = df.size

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    male_mask = df['sex'] == 'Male'    
    average_age_men = round(df.loc[male_mask, 'age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_mask = df['education'] == 'Bachelors'
    percentage_bachelors = round((df[bachelors_mask].size / persons) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    advanced_edu_mask = (df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')
    salary_mask = df['salary'] == '>50K'

    higher_education = df.loc[advanced_edu_mask].size
    lower_education = persons - higher_education

    # percentage with salary >50K
    higher_education_rich = round((df.loc[advanced_edu_mask  & salary_mask].size / higher_education) * 100, 1)
    lower_education_rich = round((df.loc[salary_mask & ~advanced_edu_mask].size / lower_education) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_work_mask = df['hours-per-week'] == min_work_hours
    num_min_workers = df[min_work_mask].size

    rich_percentage = round((df[min_work_mask & salary_mask].size / num_min_workers) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    
    df_country_count_rich = df[salary_mask]['native-country'].value_counts()
    df_country_count = df['native-country'].value_counts()

    highest_earning_country = (df_country_count_rich / df_country_count).idxmax()
    highest_earning_country_percentage = round((df_country_count_rich / df_country_count) * 100, 1).max()

    # Identify the most popular occupation for those who earn >50K in India.
    india_mask = df['native-country'] == 'India'
    top_IN_occupation = df[(india_mask & salary_mask)].value_counts(subset='occupation').idxmax()


    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
