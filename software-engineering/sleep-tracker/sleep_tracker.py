import streamlit as st

# Define the app's features
def sleep_tracker():
    st.title("Sleep Tracker")

    # Set up user authentication
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "user" and password == "password":
            st.success("Logged in as {}".format(username))
        else:
            st.error("Invalid username or password")

    # Set sleep goals
    sleep_goal = st.slider("Sleep goal (hours)", min_value=0, max_value=24, step=1, value=8)

    # Track sleep duration
    sleep_duration = st.slider("Sleep duration (hours)", min_value=0, max_value=24, step=4,value=1)

    # Monitor sleep quality
    sleep_quality = st.slider("Sleep quality (1-10)", min_value=1, max_value=10, step=1)

    # Implement sleep analysis
    sleep_efficiency = sleep_duration / sleep_goal
    st.write("Sleep efficiency: {:.2f}%".format(sleep_efficiency * 100))

    # Build a dashboard
    st.subheader("Sleep data")
    st.write("Sleep goal: {} hours".format(sleep_goal))
    st.write("Sleep duration: {:.2f} hours".format(sleep_duration))
    st.write("Sleep quality: {}".format(sleep_quality))

# Run the app
sleep_tracker()
