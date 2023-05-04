import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('My Parents Menu')
streamlit.text('🥣 Blue Berry Oatmeal')
streamlit.text('🥗 Spinach Rocky Smoothie')
streamlit.text('🐔 Hard Boiled-egg')
streamlit.text('🥑 Avocado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show = fruit_selected.loc(my_fruit_list)

streamlit.dataframe(fruit_to_show)
