import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library
from PIL import Image # converting images into arrays
df_san = pd.read_csv('https://cocl.us/sanfran_crime_dataset')

df_sanN = df_san.groupby('PdDistrict',axis = 0).sum()
df_sanN['count'] = df_san['PdDistrict'].value_counts()
df_sanN.drop(['IncidntNum','X','Y','PdId'],axis = 1 ,inplace =True)
df_sanN.reset_index(inplace = True)
df_sanN.rename(columns = {'PdDistrict':'Neighborhood'},inplace =True)
b, c = df_sanN.iloc[0], df_sanN.iloc[1]
df_sanN.iloc[0], df_sanN.iloc[1] = c, b
d, e = df_sanN.iloc[1], df_sanN.iloc[4]
df_sanN.iloc[1], df_sanN.iloc[4] = e, d
f, g = df_sanN.iloc[2], df_sanN.iloc[5]
df_sanN.iloc[2], df_sanN.iloc[5] = g, f
h, i = df_sanN.iloc[3], df_sanN.iloc[7]
df_sanN.iloc[3], df_sanN.iloc[7] = i, h
j, k = df_sanN.iloc[4], df_sanN.iloc[7]
df_sanN.iloc[4], df_sanN.iloc[7] = k, j
l, m = df_sanN.iloc[5], df_sanN.iloc[9]
df_sanN.iloc[5], df_sanN.iloc[9] = m, l
n, o = df_sanN.iloc[7], df_sanN.iloc[8]
df_sanN.iloc[7], df_sanN.iloc[8] = o, n
p, z = df_sanN.iloc[8], df_sanN.iloc[9]
df_sanN.iloc[8], df_sanN.iloc[9] = z, p


df_sanN
!conda install -c conda-forge folium=0.5.0 --yes
import folium

print('Folium installed and imported!')

!wget --quiet https://cocl.us/sanfran_geojson -O sanfrancisco.json
    
print('GeoJSON file downloaded!')

world_geo = r'sanfrancisco.json'
# San Francisco latitude and longitude values
latitude = 37.77
longitude = -122.42

# create a numpy array of length 6 and has linear spacing from the minium total immigration to the maximum total immigration
threshold_scale = np.linspace(df_sanN['count'].min(),
                              df_sanN['count'].max(),
                              6, dtype=int)
threshold_scale = threshold_scale.tolist() # change the numpy array to a list
threshold_scale[-1] = threshold_scale[-1] + 1 # make sure that the last value of the list is greater than the maximum immigration

# let Folium determine the scale.
world_map = folium.Map(location=[latitude,longitude], zoom_start=12)


world_map.choropleth(
    geo_data=world_geo,
    data=df_sanN,
    columns=['Neighborhood', 'count'],
    key_on='feature.properties.DISTRICT',
    threshold_scale=threshold_scale,
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Rate of Crime at Sanfrancisco',
    reset=True
)


world_map
