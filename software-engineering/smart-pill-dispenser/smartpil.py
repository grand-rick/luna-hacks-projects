import streamlit as st
import time
from datetime import datetime, timedelta
import threading

st.set_page_config(page_title="Smart Pill Dispenser", page_icon="💊")

st.title("Smart Pill Dispenser")

# Define pill inventory and schedule
pill_names = ["Pill A", "Pill B", "Pill C"]
pill_quantities = [10, 20, 30]
pill_schedule = {
    "Pill A": [datetime.now() + timedelta(minutes=30)],
    "Pill B": [datetime.now() + timedelta(hours=2)],
    "Pill C": [datetime.now() + timedelta(days=1)]
}

# Define function for dispensing pills
def dispense_pills(pill_name, quantity):
    st.write("Dispensing...")
    time.sleep(2)
    st.write(f"{quantity} {pill_name}(s) dispensed!")
    pill_quantities[pill_names.index(pill_name)] -= quantity
    pill_schedule[pill_name].pop(0)

# Define function for checking pill schedule
def check_schedule():
    while True:
        for pill_name, schedule in pill_schedule.items():
            if schedule and datetime.now() >= schedule[0]:
                st.write(f"It's time to take {pill_name}!")
                threading.Thread(target=send_notification, args=(pill_name,)).start()
        time.sleep(60)

# Define function for sending notifications
def send_notification(pill_name):
    st.experimental_rerun()
    st.write(f"Sent notification to take {pill_name}!")

# Start thread for checking pill schedule
threading.Thread(target=check_schedule).start()

# Define user interface
selected_pill = st.selectbox("Select a pill:", pill_names)

st.write(f"Selected pill: {selected_pill}")

quantity = st.slider("Select quantity:", 0, max(pill_quantities))

st.write(f"Selected quantity: {quantity}")

if st.button("Dispense"):
    if quantity > pill_quantities[pill_names.index(selected_pill)]:
        st.write("Error: Not enough pills in inventory!")
    else:
        pill_schedule[selected_pill].append(datetime.now() + timedelta(minutes=30*quantity))
        threading.Thread(target=dispense_pills, args=(selected_pill, quantity)).start()

# Display pill inventory
st.write("Current inventory:")
for i in range(len(pill_names)):
    st.write(f"{pill_names[i]}: {pill_quantities[i]}")

# Display pill schedule
st.write("Upcoming doses:")
for pill_name, schedule in pill_schedule.items():
    if schedule:
        st.write(f"{pill_name}: {', '.join([t.strftime('%Y-%m-%d %H:%M:%S') for t in schedule])}")
    else:
        st.write(f"{pill_name}: No upcoming doses")
