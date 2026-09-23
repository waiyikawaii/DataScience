import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r'D:\Finlatics\DsResearch\DsResearch\Banking\banking_data.csv')

'Q1: What is the distribution of age among the clients?'
age=df['age']

#print descriptive statistics
print(age.describe())

#create canvas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

#histogram
ax1.hist(age, bins=20, color='#97B3AE', edgecolor='black', alpha=0.85)
ax1.set_ylabel('Number of Bank Clients')
ax1.set_xlabel('Age of Bank Clients')
ax1.set_title('Distribution of Age')
plt.grid(which='major', linestyle=':', linewidth=0.5, color='black')

#boxplot
box=ax2.boxplot(age, vert=False, showmeans=True, meanline=True,patch_artist=True,medianprops={'linewidth': 2, 'color': 'purple'},
                meanprops={'linewidth': 2, 'color': 'red'},boxprops=dict(facecolor='#97B3AE', color='black'),
                whiskerprops=dict(color='black'), capprops=dict(color='black'))
ax2.set_title('Boxplot of Age')
ax2.set_xlabel('Age of Bank Clients')

#automatically adjust the spacing between subplots and elements within a figure to minimize overlap
plt.tight_layout()
plt.show()

'Q2: How does the job type vary among the clients?'
sns.countplot(y='job', data=df, color='#D2E0D3',edgecolor='black',order=df['job'].value_counts().index)
plt.xlabel('Number of Bank Clients')
plt.ylabel('Job Type')
plt.title('Distribution of Job Type')
plt.show()

'Q3: What is the marital status distribution of the clients?'
#bar chart
ax=sns.countplot(x='marital', data=df, color='#F0DDD6', edgecolor='black', order=df['marital'].value_counts().index)

#add the numerical labels for each category
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', 
                (p.get_x()+p.get_width()/2., p.get_height()),
                ha='center',va='bottom',fontsize=10)

plt.xlabel('Marital Status')
plt.ylabel('Number of Bank Clients')
plt.title('Distribution of Marital Status')
plt.show()

#descriptive statistics
marital_counts = df['marital'].value_counts()
print("Distribution of Marital Status")
print(marital_counts)
print("\nProportion (%):")
print(round(marital_counts/len(df)*100,2))

'Q4: What is the level of education among the clients?'
#bar chart
order_list = ['primary', 'secondary', 'tertiary', 'unknown']
ax = sns.countplot(x='education', data=df,color='#9b72fe', edgecolor='black', order=order_list)

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x()+p.get_width()/2., p.get_height()), 
                ha='center', va='bottom', fontsize=10)

plt.xlabel('Level of Education')
plt.ylabel('Number of Bank Clients')
plt.title('Distribution of Level of Education')
plt.show()

#descriptive statistics
edu_counts = df['education'].value_counts()
print("Distribution of Level of Education:")
print(edu_counts)
print("\nProportion (%):")
print(round(edu_counts/len(df)*100,2))

'Q5: What proportion of clients have credit in default?'
#descriptive statistics
counts = df['default'].value_counts()
proportions = counts / len(df) * 100

print("Credit in Default - Counts:")
print(counts)
print("\nProportion (%):")
print(round(proportions, 2))

#bar chart
order_list = ['yes', 'no']
ax = sns.countplot(x='default', data=df,color='#D6CBBF', edgecolor='black', order=order_list)

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x()+p.get_width()/2., p.get_height()), 
                ha='center', va='bottom', fontsize=10)

plt.xlabel('Credit in Default')
plt.ylabel('Number of Bank Clients')
plt.title('Distribution of Credit in Default')
plt.show()

'Q6: What is the distribution of average yearly balance among the clients?'
balance=df['balance']

#print descriptive statistics
print(balance.describe())

#boxplot
plt.boxplot(balance, vert=False, showmeans=True, meanline=True,patch_artist=True,medianprops={'linewidth': 2, 'color': 'purple'},
           meanprops={'linewidth': 2, 'color': 'red'},boxprops=dict(facecolor='#B8DDF7', color='black'),
           whiskerprops=dict(color='black'), capprops=dict(color='black'))
plt.title('Boxplot of Yearly Balance')
plt.xlabel('Average Yearly Balance (€)')

plt.show()

'Q7: How many clients have housing loans?'
#descriptive statistics
housing_counts = df['housing'].value_counts()
housing_proportions = housing_counts / len(df) * 100

print("Housing Loans - Counts:")
print(housing_counts)
print("\nProportion (%):")
print(round(housing_proportions, 2))

#bar chart
order_list = ['yes', 'no']
ax=sns.countplot(x='housing', data=df,color='#A7BFE3', edgecolor='black', order=order_list)

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x()+p.get_width()/2., p.get_height()), 
                ha='center', va='bottom', fontsize=10)

plt.xlabel('Housing Loans')
plt.ylabel('Number of Bank Clients')
plt.title('Distribution of Housing Loans')
plt.show()

'Q8: How many clients have personal loans?'
#descriptive statistics
personal_counts = df['loan'].value_counts()
personal_proportions = personal_counts / len(df) * 100

print("Personal Loans - Counts:")
print(personal_counts)
print("\nProportion (%):")
print(round(personal_proportions, 2))

#bar chart
order_list = ['yes', 'no']
ax=sns.countplot(x='loan', data=df,color='#60CDF6', edgecolor='black', order=order_list)

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x()+p.get_width()/2., p.get_height()), 
                ha='center', va='bottom', fontsize=10)

plt.xlabel('Personal Loans')
plt.ylabel('Number of Bank Clients')
plt.title('Distribution of Personal Loans')
plt.show()

'Q9: What are the communication types used for contacting clients during the campaign?'
#descriptive statistics
counts = df['contact'].value_counts()
proportions = counts / len(df) * 100

print("Communication Types - Counts:")
print(counts)
print("\nProportion (%):")
print(round(proportions, 2))

#bar chart
order_list = ['unknown', 'telephone', 'cellular']
ax=sns.countplot(x='contact', data=df,color='#22B1C2', edgecolor='black', order=order_list)

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x()+p.get_width()/2., p.get_height()), 
                ha='center', va='bottom', fontsize=10)

plt.xlabel('Communication Types')
plt.ylabel('Number of Bank Clients')
plt.title('Distribution of Communication Types')
plt.show()

'Q10: What is the distribution of the last contact day of the month?'
print("Last Contact Day - Statistics:")
print(df['day'].describe())

day_counts = df['day'].value_counts().sort_index()
print("\nCounts per specific day:")
print(day_counts)

plt.figure(figsize=(14, 5))

ax = sns.countplot(x='day', data=df, color='#2C91BF', edgecolor='black')

plt.xlabel('Day of the Month (Last Contact)')
plt.ylabel('Number of Bank Clients')
plt.title('Distribution of Last Contact Day of the Month')

plt.tight_layout()
plt.show()

'Q11: How does the last contact month vary among the clients?'
month_counts = df['month'].value_counts()
month_props = month_counts / len(df) * 100

print("Last Contact Month - Counts:")
print(month_counts)
print("\nProportion (%):")
print(round(month_props, 2))

full_year_order = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

print("\nMonths in correct chronological order:", full_year_order)

plt.figure(figsize=(10, 5))
ax = sns.countplot(x='month', data=df, color='#CBE5BE', edgecolor='black', order=full_year_order)

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', 
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom', fontsize=10)

plt.xlabel('Last Contact Month')
plt.ylabel('Number of Bank Clients')
plt.title('Distribution of Last Contact Month', fontsize=14)

plt.tight_layout()
plt.show()

'Q12: What is the distribution of the duration of the last contact?'
duration=df['duration']
print(duration.describe())

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

#histogram
ax1.hist(duration, bins=20, color='#D1CFE7', edgecolor='black', alpha=0.85)
ax1.set_ylabel('Number of Bank Clients')
ax1.set_xlabel('Duration of the Last Contact (seconds)')
ax1.set_title('Distribution of the Last Contact')
plt.grid(which='major', linestyle=':', linewidth=0.5, color='black')

#boxplot
box=ax2.boxplot(duration, vert=False, showmeans=True, meanline=True,patch_artist=True,medianprops={'linewidth': 2, 'color': 'purple'},
                meanprops={'linewidth': 2, 'color': 'red'},boxprops=dict(facecolor='#D1CFE7', color='black'),
                whiskerprops=dict(color='black'), capprops=dict(color='black'))
ax2.set_title('Boxplot of Duration')
ax2.set_xlabel('Duration (seconds)')

#automatically adjust the spacing between subplots and elements within a figure to minimize overlap
plt.tight_layout()
plt.show()

'Q13: How many contacts were performed during the campaign for each client?'
campaign = df['campaign']

print("Campaign Contacts - Statistics:")
print(campaign.describe())

counts = df['campaign'].value_counts().sort_index()

result_df = pd.DataFrame({'campaign': counts.index,'Number_of_Clients': counts.values})

print(result_df)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

bins = np.arange(0.5, campaign.max() + 1.5, 1)

ax1.hist(campaign, bins=bins, color='pink', edgecolor='black', alpha=0.85)
ax1.set_ylabel('Number of Bank Clients')
ax1.set_xlabel('Number of Contacts during Campaign')
ax1.set_title('Distribution of Campaign Contacts')
ax1.grid(axis='y', linestyle=':', linewidth=0.5, alpha=0.7)

ax2.boxplot(campaign, vert=False, showmeans=True, meanline=True,
            patch_artist=True,
            medianprops={'linewidth': 2, 'color': 'purple'},
            meanprops={'linewidth': 2, 'color': 'red'},
            boxprops=dict(facecolor='pink', color='black'),
            whiskerprops=dict(color='black'),
            capprops=dict(color='black'))
ax2.set_title('Boxplot of Campaign Contacts')
ax2.set_xlabel('Number of Contacts')

plt.tight_layout()
plt.show()

'Q14: What is the distribution of the number of days passed since the client was last contacted from a previous campaign?'
pdays = df['pdays']

never_contacted = (pdays == -1).sum()
ever_contacted = (pdays >= 0).sum()

print(f"Number of clients NEVER contacted before: {never_contacted}")
print(f"Number of clients contacted before: {ever_contacted}")
print("\n" + "="*50)

pdays_filtered = pdays[pdays >= 0]

print("Statistics for clients who WERE previously contacted (pdays >= 0):")
print(pdays_filtered.describe())

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

ax1.hist(pdays_filtered, bins=20, color='#F9D7E7', edgecolor='black', alpha=0.85)
ax1.set_ylabel('Number of Bank Clients')
ax1.set_xlabel('Days Passed Since Last Contact')
ax1.set_title('Distribution of Days Passed')
ax1.grid(axis='y', linestyle=':', linewidth=0.5, alpha=0.7)

ax2.boxplot(pdays_filtered, vert=False, showmeans=True, meanline=True,
            patch_artist=True,
            medianprops={'linewidth': 2, 'color': 'purple'},
            meanprops={'linewidth': 2, 'color': 'red'},
            boxprops=dict(facecolor='#F9D7E7', color='black'),
            whiskerprops=dict(color='black'),
            capprops=dict(color='black'))
ax2.set_title('Boxplot of Days Passed')
ax2.set_xlabel('Days Passed')

plt.tight_layout()
plt.show()

'Q15: How many contacts were performed before the current campaign for each client?'
previous = df['previous']

print("Statistics for Previous Campaign Contacts:")
print(previous.describe())

print("\nCounts per specific previous contact number:")
print(previous.value_counts().sort_index())

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

bins = np.arange(-0.5, previous.max() + 1.5, 1)
ax1.hist(previous, bins=bins, color='#DC166B', edgecolor='black', alpha=0.85)
ax1.set_ylabel('Number of Bank Clients')
ax1.set_xlabel('Number of Contacts BEFORE this Campaign')
ax1.set_title('Distribution of Previous Contacts')
ax1.grid(axis='y', linestyle=':', linewidth=0.5, alpha=0.7)

ax2.boxplot(previous, vert=False, showmeans=True, meanline=True,
            patch_artist=True,
            medianprops={'linewidth': 2, 'color': 'purple'},
            meanprops={'linewidth': 2, 'color': 'red'},
            boxprops=dict(facecolor='#DC166B', color='black'),
            whiskerprops=dict(color='black'),
            capprops=dict(color='black'))
ax2.set_title('Boxplot of Previous Contacts')
ax2.set_xlabel('Number of Previous Contacts')

plt.tight_layout()
plt.show()

'Q16: What were the outcomes of the previous marketing campaigns?'
#descriptive statistics
o= df['poutcome'].value_counts()
oproportions=o/len(df)*100

print("Outcome of the Previous Marketing Campaign:")
print(o)
print("\nProportion (%):")
print(round(oproportions,2))

#bar chart
order_list = ['unknown', 'other', 'failure', 'success']
ax=sns.countplot(x='poutcome', data=df,color='#FFF5A0', edgecolor='black', order=order_list)

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x()+p.get_width()/2., p.get_height()), 
                ha='center', va='bottom', fontsize=10)

plt.xlabel('Outcome of the Previous Marketing Campaign')
plt.ylabel('Number of Bank Clients')
plt.title('Outcome of the Previous Marketing Campaign')
plt.show()

'Q17: What is the distribution of clients who subscribed to a term deposit vs. those who did not?'
#descriptive statistics
y= df['y'].value_counts()
yproportions=y/len(df)*100

print("Distribution of Term Deposit Subscription (y):")
print(y)
print("\nProportion (%):")
print(round(yproportions,2))

#bar chart
order_list = ['yes', 'no']
ax=sns.countplot(x='y', data=df,color='#F79824', edgecolor='black', order=order_list)

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x()+p.get_width()/2., p.get_height()), 
                ha='center', va='bottom', fontsize=10)

print("Distribution of Term Deposit Subscription (y):")
plt.xlabel('Subscribed to Term Deposit')
plt.ylabel('Number of Bank Clients')
plt.title('Distribution of Clients by Term Deposit Subscription')
plt.show()

'Q18: Are there any correlations between different attributes and the likelihood of subscribing to a term deposit?'
df['y_num'] = (df['y'] == 'yes') * 1

numeric_df = df.select_dtypes(include=['int64', 'float64'])

corr_matrix = numeric_df.corr()

print("Correlation of each feature with the target variable (y_num):")
print(corr_matrix['y_num'].sort_values(ascending=False))

plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap='PuBuGn', fmt='.2f', 
            linewidths=0.5, square=True)
plt.title('Correlation Matrix of Banking Dataset Features', fontsize=14)
plt.tight_layout()
plt.show()