import streamlit as st
import time
import datetime

st.title("Scheduler")

scheduled_time = st.time_input("Enter scheduled time:")
task_name = st.text_input("Enter task name:")

if scheduled_time and task_name:
    st.write("Task scheduled at:", scheduled_time)
    st.write("Task name:", task_name)

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == scheduled_time.strftime("%H:%M:%S"):
            st.write("Running task:", task_name)
            # Add code to execute task here
            break
        else:
            st.write("Waiting for scheduled time...")
            time.sleep(1)