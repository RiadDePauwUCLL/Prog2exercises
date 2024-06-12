# Get only completed bookings.
df1 = df[df['booking_complete'] == 1].groupby('booking_origin')

# Get 5 countries with most bookings.
df2 = df1.count().sort_values(by='booking_complete', ascending=False).reset_index()
top_5_countries = df2.loc[0:4, 'booking_origin'].to_list() # <----------- labels
booking_count = df2.loc[0:4, 'booking_complete'].to_list() # <----------- y-axis

# Get average purchase leads of those top 5 countries.
df3 = df1['purchase_lead'].mean().reset_index()
purchase_leads = [] # <------------- x-axis
for country in top_5_countries:
    series = df3[df3['booking_origin'] == country].reset_index()
    purchase_lead = series['purchase_lead'][0]
    purchase_leads.append(purchase_lead)

# Create the bar chart.
plt.bar(purchase_leads, booking_count, width=3.5)
plt.xlabel('Purchase lead [day]')
plt.ylabel('Booking count []')

# Add labels to each column.
for i in range(len(country)):
    # plt.text(x, y, text, ...)
    plt.text(purchase_leads[i], booking_count[i], top_5_countries[i], ha='center', va='bottom')
