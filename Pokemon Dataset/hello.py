from preswald import text, plotly, connect, get_df, table,sidebar, slider, query
import pandas as pd
import plotly.express as px

text("# Pokemon App")

sidebar()

# Load the CSV
connect()
df = get_df('pokemon_csv')
table(df)

# Execute SQL query to filter pokemons based on Base Stat Total
sql = "SELECT Name, Attack, Health, Form, FROM pokemon_csv WHERE Attack >= 100"
filtered_df = query(sql, 'pokemon_csv')
text("# Pokemon Analysis App")
table(filtered_df, title="Attack Data")

attackMinimum = slider("Minimum Attack", min_val=100.0, max_val=200.0, default=100.0)
healthMinimum = slider("Health Attack", min_val=30.0, max_val=200.0, default=30.0)



# Generated plot
# Creating a scatter plot from the filtered_df
fig = px.scatter(filtered_df, x="Health", y="Attack", color="Form", 
                 title="Pokemon Attack and Health Analysis", labels={"Health": "Health Points", "Attack": "Attack Value"})
plotly(fig)


