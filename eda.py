from h2o_wave import Q, main, app, ui,site,data
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import random

def load_data():
    data = pd.read_csv('California_Fire_Incidents.csv')
    return data

df = load_data()

page = site['/eda']


card = page.add('header', ui.header_card(
    box='1 1 5 2',
    title='EDA California Fire Incidents',
    subtitle='made by Team Pegasus',
    icon='ExploreData',
))


# plotting data
df_point =  df.loc[:1500,['AcresBurned','CalFireIncident','Status']]
# df_point = pd.DataFrame(data,columns=['AcresBurned','CalFireIncident'])
v = page.add('point_plot', ui.plot_card(
    box='1 3 5 4',#col row width height
    title='Point Plot',
    data=data(fields=df_point.columns.tolist(),rows=df_point.values.tolist()),
    plot=ui.plot([
        ui.mark(type='point', 
        x='=AcresBurned', y='=CalFireIncident',color='Status'
         )
    ])
))

df_point_sized =  df.loc[:1500,['ArchiveYear','AcresBurned','CalFireIncident']]
v = page.add('point_plot_sized', ui.plot_card(
    box='6 3 4 4',
    title='Point Plot Sized',
    data=data(fields=df_point_sized.columns.tolist(),rows=df_point_sized.values.tolist()),
    plot=ui.plot([
        ui.mark(type='point', 
        x='=ArchiveYear', y='=AcresBurned',size='=CalFireIncident')
    ])
))


df_bar=  df.loc[:1500,['ArchiveYear','AcresBurned','Counties']]
v = page.add('bar_plot', ui.plot_card(
    box='1 7 9 4',
    title='Bar Plot',
    data=data(fields=df_bar.columns.tolist(),rows=df_bar.values.tolist()),
    plot=ui.plot(marks=[
        ui.mark(type='interval', 
        x='=ArchiveYear', y='=AcresBurned',
        color='=Counties')
    ])
))

# df_bar_stacked=  df.loc[:1500,['ArchiveYear','AcresBurned','Counties']]
# print(df_bar_stacked)
# v = page.add('df_bar_stacked', ui.plot_card(
#     box='1 11 9 4',
#     title='Stacked Bar Plot',
#     data=data(fields=df_bar_stacked.columns.tolist(),rows=df_bar_stacked.values.tolist()),
#     plot=ui.plot(marks=[
#         ui.mark(type='interval', 
#         x='=ArchiveYear', y='=AcresBurned',
#         color='=Counties', stack='auto')
#     ])
# ))

# df_line=  df.loc[:1630,['ArchiveYear','AcresBurned']]
# v = page.add('df_line', ui.plot_card(
#     box='1 11 9 4',
#     title='Line Plot',
#     data=data(fields=df_line.columns.tolist(),rows=df_line.values.tolist()),
#     plot=ui.plot(marks=[
#         ui.mark(type='line', 
#         x='=ArchiveYear', y='=AcresBurned', curve='smooth')
#     ])
# ))

df_area=  df.loc[:1630,['ArchiveYear','AcresBurned']]
v = page.add('df_area', ui.plot_card(
    box='1 11 9 4',
    title=' Line with Area Plot',
    data=data(fields=df_area.columns.tolist(),rows=df_area.values.tolist()),
    plot=ui.plot(marks=[
        ui.mark(type='area',
        x='=ArchiveYear', y='=AcresBurned',
        ),
        ui.mark(type='line', x='=ArchiveYear', y='=AcresBurned', curve='smooth')
    ])
))

# df_b=  df.loc[:200,['AMT_INCOME_TOTAL','NAME_HOUSING_TYPE']]
# v = page.add('df_b', ui.plot_card(
#     box='1 15 5 4',
#     title='Bar Plot',
#     data=data(fields=df_b.columns.tolist(),rows=df_b.values.tolist()),
#     plot=ui.plot([
#         ui.mark(type='interval', 
#         x='=NAME_HOUSING_TYPE', y='=AMT_INCOME_TOTAL' ) 
#     ])
# ))

# df_line_step =  df.loc[:100,['SK_ID_CURR','NAME_INCOME_TYPE','AMT_INCOME_TOTAL']]
# v = page.add('df_heatmap', ui.plot_card(
#     box='6 15 4 4',
#     title='Line Step Plot',
#     data=data(fields=df_line_step.columns.tolist(),rows=df_line_step.values.tolist()),
#     plot=ui.plot([
#         ui.mark(type='path', 
#         x='=SK_ID_CURR', y='=AMT_INCOME_TOTAL', curve='step' ) 
#     ])
# ))


page.save()

 