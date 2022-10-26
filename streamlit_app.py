import streamlit
import pandas

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
streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index))

# display fruit df 
streamlit.dataframe(my_fruit_list)

