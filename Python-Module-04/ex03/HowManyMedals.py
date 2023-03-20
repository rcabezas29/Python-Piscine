def how_many_medals(df, name):
    athlete_historic = df.loc[df['Name'] == name]
    ret = dict()
    for _, e in athlete_historic.iterrows():
        year = e["Year"]
        medal = e["Medal"]
        if year not in ret.keys():
            ret.update({year: {"G": 0, "S": 0, "B": 0}})
        if medal == "Gold":
            ret[year]["G"] += 1
        elif medal == "Silver":
            ret[year]["S"] += 1
        elif medal == "Bronze":
            ret[year]["B"] += 1
    return ret
    
from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('../data/athlete_events.csv')
print(how_many_medals(data, 'Kjetil Andr Aamodt'))