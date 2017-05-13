# coding: utf-8

# In[189]:

import sys

import pandas as pd
import numpy as np


# In[172]:

# Use: python gen_checkin_heatmap.py [city name] [output filename.csv]
# Example: python gen_checkin_heatmap.py Phoenix phoenix_checkin_heatmap.csv

business = pd.read_csv('../dataset/yelp_academic_dataset_business.csv')
checkin = pd.read_csv('../dataset/yelp_academic_dataset_checkin.csv')

# "Phoenix"
if sys.argv[1] != 'all':
    business = business.loc[business['city'] == sys.argv[1]]

# In[174]:

business_checkin = pd.merge(business, checkin, on='business_id')[['business_id', 'longitude', 'latitude', 'time']]

# In[191]:

def createDataFrameFromRow(row):
    day_map = {"Mon":0, "Tue":1, "Wed":2, "Thu": 3, "Fri":4, "Sat":5, "Sun":6}
    day_hour_checkin = eval(row['time'])
    day = [day_map[s[:3]] for s in day_hour_checkin]
    hour = [s[4: s.find(':')] for s in day_hour_checkin]
    checkin = sum([int(s[s.find(':')+1:]) for s in day_hour_checkin])
    business_id = [row['business_id']] * len(day)
    #longitude = [row['longitude']] + [''] * (len(day)-1)
    #latitude = [row['latitude']] + [''] * (len(day)-1)
    #return pd.DataFrame(data = {'latitude': latitude, 'longitude': longitude, 'day': day, 'hour': hour, 'checkin':checkin})
    #return pd.DataFrame(data = {'latitude': latitude, 'longitude': longitude, 'day': day, 'hour': hour, 'checkin':checkin})
    return pd.DataFrame(data = {'latitude': row['latitude'], 'longitude': row['longitude'], 'checkin':checkin})


def returnSumOfCheckin(row):
    day_hour_checkin = eval(row['time'])
    return sum([int(s[s.find(':')+1:]) for s in day_hour_checkin])

# In[192]:

#loc_time_checkin = pd.concat([createDataFrameFromRow(row) for _, row in business_checkin.iterrows()]).reset_index()
#loc_time_checkin = pd.concat([createDataFrameFromRow(row) for _, row in business_checkin.iterrows()]).reset_index()
loc_time_checkin = pd.DataFrame.from_records([{'lat': row['latitude'],
                                               'lng': row['longitude'],
                                               'checkin': returnSumOfCheckin(row) }
                                              for _, row in business_checkin.iterrows()])

# In[194]:

#loc_time_checkin = loc_time_checkin.drop('index', axis=1)
print len(loc_time_checkin)

# In[187]:

output_file = open(sys.argv[2], 'w')
output_file.write(pd.DataFrame.to_csv(loc_time_checkin, index=False))
output_file.close()
