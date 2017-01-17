import pandas as pd
import numpy as np

xlsFile = 'data/input/Subway-Ridership.xlsx'

df = pd.io.excel.read_excel(xlsFile, 'Sheet1')

df_xy = pd.read_csv('data/input/Export_Output.txt')
df_xy = df_xy.rename(columns=lambda x: x.lower())

df_new = pd.read_csv('data/input/subway_stations_new_2017.csv')

df['uid'] = df['station'].str.lower().str.replace('subway','').str.replace('avenue','ave').str.replace('parkway','pkwy').str.replace('highway','hwy').str.replace(' ','').str.replace(',','')
df['uid'] = df['uid'].str.replace('grandcentral-42st4567s','grandcentral-42sts4567').str.replace('smith-9stsfg','smith-9stfg').str.replace('winthopst25','winthropst25').str.replace('116st-columbiau1','116st-columbiauniversity1')
df['uid'] = df['uid'].str.replace('w4st-washingtonsqabcd','west4st-washingtonsqabcdefm').str.replace('beverlyrdq','beverleyrdq').str.replace('beach67sta','beach67st-arvernebytheseaa').str.replace('franklinav-botanicgardens2345s','franklinav2345/botanicgardens')
df['uid'] = df['uid'].str.replace('fthamiltonpkwyd','forthamiltonpkwyd').str.replace('fthamiltonpkwyn','forthamiltonpkwyn').str.replace('4av-9stfg','4avfg/9str').str.replace('33st7','33st-rawsonst7').str.replace('14st-8avacel','14stace/8avl').str.replace('14st-6avfml','14stfm123/6avl')
df['uid'] = df['uid'].str.replace('40st7','40st-loweryst7').str.replace('42st-bryantpkbdfm','42st-bryantpkbdfm/5av7').str.replace('46st7','46st-blissst7').str.replace('5av-57stnqr','5av-59stnqr').str.replace('74-bway7/jacksonhts-rooseveltavefmr','74st-broadway/jacksonheights-rooseveltav7efmr')
df['uid'] = df['uid'].str.replace('fultonstacjz2345','fultonstacjz').str.replace('42st-bryantpkbdfm/5av7/5av7','42st-bryantpkbdfm/5av7').str.replace('southferry1/whitehallstr','southferry1').str.replace('steinwaymr','steinwaystmr').str.replace('timesst-42stnqrs1237','timessq-42stnqrs1237/42stace').str.replace('newutrechtav-62stdn','newutrechtavn/62std').str.replace('metropolitanavgl','lorimerstl/metropolitanavg').str.replace('lexingtonav-59stnqr456','lexingtonavnqr/59st456').str.replace('lexingtonav-53stem/51st6','lexingtonav-53stem').str.replace('jamaicacenter-parsonsavejz','jamaicacenter-parsons-archerejz')
df['uid'] = df['uid'].str.replace('e167stbd','167stbd').str.replace('82st-jacksonheights7','82st-jacksonhts7').str.replace('8st-nyunr','8st-newyorkuniversitynr').str.replace('aqueduct-nconduitava','aqueduct-northconduitava').str.replace('astorpl6','astorplace6').str.replace('atlanticav-barclaysbq2345','atlanticav-barclaysctrbdnqr2345').str.replace('broadway-lafayettestbdfm/bleeckerst6','broadway-lafayettestbdfm').str.replace('brooklynbridge-cityhall-chambersst456jz','brooklynbridge-cityhall456/chambersstjz').str.replace('canalstjnqz6','canalstjnqrz6').str.replace('chambersstac/wtce/parkplace23','chambersstac').str.replace('cityhallr','cityhallnr').str.replace('cortlandtstr','cortlandtstnr').str.replace('courtsqemg7','courtsqegm7').str.replace('courtstr/boroughhall2345','courtstr').str.replace('delanceyst-essexstfmjz','delanceystf/essexstjmz').str.replace('e105stl','east105stl')


print df.head(15)


df_xy['station'] = df_xy['name'] + df_xy['descriptio']

df_xy['uid'] = df_xy['station'].str.lower().str.replace('subway','').str.replace('avenue','ave').str.replace('parkway','pkwy').str.replace('highway','hwy').str.replace(' ','').str.replace(',','').str.split('*').str[0]
df_xy['uid'] = df_xy['uid'].str.replace('grandcentral-42st4567s','grandcentral-42sts4567').str.replace('smith-9stsfg','smith-9stfg').str.replace('winthopst25','winthropst25').str.replace('116st-columbiau1','116st-columbiauniversity1')
df_xy['uid'] = df_xy['uid'].str.replace('w4st-washingtonsqabcd','west4st-washingtonsqabcdefm').str.replace('beverlyrdq','beverleyrdq').str.replace('beach67sta','beach67st-arvernebytheseaa').str.replace('franklinav-botanicgardens2345s','franklinav2345/botanicgardens')
df_xy['uid'] = df_xy['uid'].str.replace('fthamiltonpkwyd','forthamiltonpkwyd').str.replace('fthamiltonpkwyn','forthamiltonpkwyn').str.replace('4av-9stfg','4avfg/9str').str.replace('33st7','33st-rawsonst7').str.replace('14st-8avacel','14stace/8avl').str.replace('14st-6avfml','14stfm123/6avl')
df_xy['uid'] = df_xy['uid'].str.replace('40st7','40st-loweryst7').str.replace('42st-bryantpkbdfm','42st-bryantpkbdfm/5av7').str.replace('46st7','46st-blissst7').str.replace('5av-57stnqr','5av-59stnqr').str.replace('74-bway7/jacksonhts-rooseveltavefmr','74st-broadway/jacksonheights-rooseveltav7efmr')
df_xy['uid'] = df_xy['uid'].str.replace('fultonstacjz2345','fultonstacjz').str.replace('42st-bryantpkbdfm/5av7/5av7','42st-bryantpkbdfm/5av7').str.replace('southferry1/whitehallstr','southferry1').str.replace('steinwaymr','steinwaystmr').str.replace('timesst-42stnqrs1237','timessq-42stnqrs1237/42stace').str.replace('newutrechtav-62stdn','newutrechtavn/62std').str.replace('metropolitanavgl','lorimerstl/metropolitanavg').str.replace('lexingtonav-59stnqr456','lexingtonavnqr/59st456').str.replace('lexingtonav-53stem/51st6','lexingtonav-53stem').str.replace('jamaicacenter-parsonsavejz','jamaicacenter-parsons-archerejz')
df_xy['uid'] = df_xy['uid'].str.replace('e167stbd','167stbd').str.replace('82st-jacksonheights7','82st-jacksonhts7').str.replace('8st-nyunr','8st-newyorkuniversitynr').str.replace('aqueduct-nconduitava','aqueduct-northconduitava').str.replace('astorpl6','astorplace6').str.replace('atlanticav-barclaysbq2345','atlanticav-barclaysctrbdnqr2345').str.replace('broadway-lafayettestbdfm/bleeckerst6','broadway-lafayettestbdfm').str.replace('brooklynbridge-cityhall-chambersst456jz','brooklynbridge-cityhall456/chambersstjz').str.replace('canalstjnqz6','canalstjnqrz6').str.replace('chambersstac/wtce/parkplace23','chambersstac').str.replace('cityhallr','cityhallnr').str.replace('cortlandtstr','cortlandtstnr').str.replace('courtsqemg7','courtsqegm7').str.replace('courtstr/boroughhall2345','courtstr').str.replace('delanceyst-essexstfmjz','delanceystf/essexstjmz').str.replace('e105stl','east105stl')


df_xy['latitude']  = df_xy['point_y']
df_xy['longitude'] = df_xy['point_x']
df_xy = df_xy.drop(['station','point_x','point_y','fid'],axis=1)

print df_xy.head(15)

df = df.merge(df_xy, left_on='uid', right_on='uid', how='left')

df = df.sort('uid',ascending=[1])

df = df.drop(['riders_17'],axis=1)

df['wkd_17_e'] = np.where(df['lexington']==1, (df['wkd_15'] - (df['wkd_15'] * 0.13)), df['wkd_15'])
df['wkd_17_e'] = df.wkd_17_e.round()

df = df.append(df_new)

df.to_csv('data/output/subway_stations_ridership_2010_2015_proj_2017.csv',index=False)

print df.head(50)