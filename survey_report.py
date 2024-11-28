import streamlit
import streamlit as sg

import psycopg2 as psg

sg.title(" Honda customer Survey ")

customer_name=sg.text_input("Enter your Name here",key="NameBox")

Namebox_res=sg.session_state["NameBox"]

query1=sg.write("What is the overall rating for your recent Survey")
options=["Good","Average","Poor"]
label_options=sg.radio("Choose the rating below",options,key="options1")

query1_res=sg.session_state["options1"]


query2=sg.write("How's is the Expert knowledge on Explaining issues? ")

sg.radio("Choose the rating below",options,key="options2")

query2_res=sg.session_state["options2"]

query3=sg.write("how is the cleanliness of the your Vechicle")

sg.radio("Choose the rating below",options,key="options3")

query3_res=sg.session_state["options3"]

query4=sg.write("how likely you recommend service to your relatives?")
sg.select_slider("Choose the Slider to rate the service",[1,2,3,4,5],key="slider_value")

slider_value_res=sg.session_state["slider_value"]

sg.text_input("Any suggestions/Recommendations please write it here",key="Suggestion_box")
Suggestion_box_res=sg.session_state['Suggestion_box']

sg.button("Submit",key="submit_button")
button_clicked=sg.session_state["submit_button"]

sg.session_state

def submit_survey(Namebox_res,query1,query2,query3,query4,slider_value_res,Suggestion_box_res):
    connection = psg.connect(host='localhost', user='postgres', password='admin',database='python_practice')
    curosr = connection.cursor()
    curosr.execute("insert into public.honda_survey (customer_name,query1_rating,query2_rating,"
                   "query3_rating,query4_rating,recommend_rating,feedback) "
                   "values (%s,%s,%s,%s,%s,%s,%s)",(Namebox_res,query1,query2,query3,query4,slider_value_res,Suggestion_box_res))
    connection.commit()
    curosr.close()
    connection.close()
    sg.write("Submitted Successfully..Thanks for your valuable time")
    sg.session_state.clear()
    print("completed")



if button_clicked:
    submit_survey(Namebox_res,query1,query2,query3,query4,slider_value_res,Suggestion_box_res)
    print("button pressed")

