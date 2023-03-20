def proportion_by_sport(df, year, sport, gender):
    year_gender_athletes = df.loc[(df['Year'] == year) & (df['Sex'] == gender)]
    fullfiltered_athletes = year_gender_athletes.loc[year_gender_athletes['Sport'] == sport]
    print(fullfiltered_athletes.shape[0] / year_gender_athletes.shape[0])
    
from FileLoader import FileLoader

loader = FileLoader()
data = loader.load('../data/athlete_events.csv')

proportion_by_sport(data, 2004, 'Tennis', 'F')