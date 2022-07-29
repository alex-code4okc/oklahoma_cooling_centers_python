import folium
import pandas

m = folium.Map(location=[35.4823241,-97.7593895], zoom_start=7)

cc_df =pandas.read_csv('./heat_centers_2022_OK.tsv',sep='\t', header=0)

for name, days, google_link, latlon in zip(cc_df['Name'], cc_df['Days'], cc_df['Google Link'], cc_df['Lat,long']):
    lat, lon = latlon.split(',')
    latF = float(lat)
    lonF = float(lon)
    folium.Marker([latF,lonF], popup=f'<div><a href={google_link}>{name}</a><p>{days}</p></div>', tooltip=name).add_to(m)

m.save('docs/index.html')