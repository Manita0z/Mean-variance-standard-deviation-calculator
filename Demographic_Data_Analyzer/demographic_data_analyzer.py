import pandas as pd

def calculate_demographic_data(print_data=True):
    # Load data
    df = pd.read_csv(r'C:\Users\Nitro\Downloads\adult.data.csv')

    # 1. Count each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's
    bachelors_percentage = round((df['education'] == 'Bachelors').sum() / len(df) * 100, 1)

    # 4. Advanced education
    higher_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_edu_rich = df[higher_edu]['salary'].eq('>50K').mean()
    lower_edu_rich = df[~higher_edu]['salary'].eq('>50K').mean()

    higher_education_rich = round(higher_edu_rich * 100, 1)
    lower_education_rich = round(lower_edu_rich * 100, 1)

    # 5. Min hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # 6. Rich percentage among min-hour workers
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(num_min_workers['salary'].eq('>50K').mean() * 100, 1)

    # 7. Country with highest % of >50K earners
    country_salary = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack()['>50K']
    highest_earning_country = country_salary.idxmax()
    highest_earning_country_percentage = round(country_salary.max() * 100, 1)

    # 8. Top occupation in India among >50K earners
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", bachelors_percentage)
        print("Percentage with higher education that earn >50K:", higher_education_rich)
        print("Percentage without higher education that earn >50K:", lower_education_rich)
        print("Min work time:", min_work_hours, "hours/week")
        print("Percentage of rich among min workers:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
        print("Top occupation in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': bachelors_percentage,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
