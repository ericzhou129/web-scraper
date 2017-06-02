# Df clean up 
# getting rid of the $ in unit prices
df['item unit price'] = df['item unit price'].str.replace('$', '')

# getting rid of CAD in unit prices
df['item unit price'] = df['item unit price'].str.replace('CAD', '')

# 
df['date'] = df['date'].str.replace('/', '-')

df['date'] = df['date'].str.replace('01-', '1-')
df['date'] = df['date'].str.replace('02-', '2-')
df['date'] = df['date'].str.replace('03-', '3-')
df['date'] = df['date'].str.replace('04-', '4-')
df['date'] = df['date'].str.replace('05-', '5-')
df['date'] = df['date'].str.replace('06-', '6-')
df['date'] = df['date'].str.replace('07-', '7-')
df['date'] = df['date'].str.replace('08-', '8-')
df['date'] = df['date'].str.replace('09-', '9-')


# convert unit price to numeric (int, float?)
df['item unit price'] = df['item unit price'].apply(pd.to_numeric)



# column multiplication
df['item_total'] = df['item unit price'] * df['item amount']



# group by date and type
grouped_df = df.groupby(['date', 'type']).sum()
