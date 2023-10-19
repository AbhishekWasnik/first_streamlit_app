import streamlit
streamlit.title('My parents new healthy diner')
streamlit.header("BREAKFAST")
streamlit.text("🥣 Omega 3 and Blueberry Oatmeal")
streamlit.text("🥗 Kale,Spinach & Rock Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocado Toast")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Display the table on the page by name.
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table 
streamlit.dataframe(fruits_to_show)


#New Section to display fruityvice API response
streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json)


