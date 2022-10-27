import pandas
import requests
import snowflake.connector
import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# list of fruits from csv
my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

# let the user choose their fruit
fruit_selected = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruit_selected]

# display fruit df 
streamlit.dataframe(fruits_to_show)

# adding user input for fruityvice api request
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered ', fruit_choice)

# display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')

fruityvice_response = requests.get('https://fruityvice.com/api/fruit/' + fruit_choice)
# streamlit.text(fruityvice_response.json()) # write json data on the screen

# take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# output it the on the screen as a table
streamlit.dataframe(fruityvice_normalized)

# snowflake connector details
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
# my_data_row = my_cur.fetchone() # fetch one row
my_data_row = my_cur.fetchall() # fetch all rows
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)