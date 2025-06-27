import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def import_and_clean():
    df = pd.read_csv(r'C:\Users\Nitro\Downloads\fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
    lower_bound = df['value'].quantile(0.025)
    upper_bound = df['value'].quantile(0.975)
    df_clean = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]
    return df_clean

def draw_line_plot():
    df = import_and_clean().copy()
    
    plt.figure(figsize=(12,6))
    plt.plot(df.index, df['value'], color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    
    plt.tight_layout()
    plt.savefig('line_plot.png')
    return plt.gcf()

def draw_bar_plot():
    df = import_and_clean().copy()
    df['year'] = df.index.year
    df['month'] = df.index.month_name()
    
    df_grouped = df.groupby(['year', 'month'])['value'].mean().unstack()
    
    months_order = ['January', 'February', 'March', 'April', 'May', 'June',
                    'July', 'August', 'September', 'October', 'November', 'December']
    
    months_order_filtered = [m for m in months_order if m in df_grouped.columns]
    df_grouped = df_grouped[months_order_filtered]
    
    df_grouped.plot(kind='bar', figsize=(12,8))
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    
    plt.tight_layout()
    plt.savefig('bar_plot.png')
    return plt.gcf()


def draw_box_plot():
    df = import_and_clean().copy()
    df.reset_index(inplace=True)
    
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.strftime('%b')
    df['month_num'] = df['date'].dt.month
    
    # Sort by month number for correct month order in plots
    df = df.sort_values('month_num')
    
    fig, axes = plt.subplots(1, 2, figsize=(15,6))
    
    # Year-wise box plot
    sns.boxplot(x='year', y='value', data=df, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    
    # Month-wise box plot
    sns.boxplot(x='month', y='value', data=df, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    
    plt.tight_layout()
    plt.savefig('box_plot.png')
    return plt.gcf()
