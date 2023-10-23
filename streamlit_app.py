import streamlit
import pandas 
import requests
import snowflake.connector
from urllib.error import URLError


#import streamlit
streamlit.title('My parents new healthy diner')
streamlit.header("BREAKFAST")
streamlit.text("🥣 Omega 3 and Blueberry Oatmeal")
streamlit.text("🥗 Kale,Spinach & Rock Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocado Toast")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
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

#Create a function 
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"fruit_choice")
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized


#New Section to display fruityvice API response
streamlit.header("Fruityvice Fruit Advice!")
try: 
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    streamlit.write('The user entered ', fruit_choice)
    if not fruit_choice:
        streamlit.error("Please select a fruit to get info.")
    else:
        back_from_function =get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
        
except URLError as e:
    streamlit.error()    

# Dont run anythimg past here while we trobleshoot 
streamlit.stop()


streamlit.header("The fruit load list contains:")
#Snowflake-related functions 
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("SELECT * FROM fruit_load_list")
         return my_cur.fetchall()
# Add button to load a fruit 
if streamlit.button('Get fruit load list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)

#Allow the end userto add fruit to list
def insert_row_snaowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamlit')"
        return 'Thanks for adding!'+ new_fruit

add_my_fruit=streamlit.text_input('What fruit would you like to add?')
if streamlkit.button('Add a fruit to list'):
       my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
        back_from_function=insert_row_snaowflake(add_my_fruit)
        streamlit.text(back_from_function)

















