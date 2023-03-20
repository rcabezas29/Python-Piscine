def youngest_fellah(df, year):
    ''''''
    year_athletes = df.loc[df['Year'] == year]
    year_athletes = year_athletes.sort_values(by=['Age'])
    f = year_athletes.loc[year_athletes['Sex'] == 'F']
    m = year_athletes.loc[year_athletes['Sex'] == 'M']
    
    print(f.head(1).Age)
    
    return {
        'f': f.iloc[0]['Age'],
        'm': m.iloc[0]['Age'],
    }
    