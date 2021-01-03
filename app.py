import streamlit as st
import time
# Text/Title
st.title("Streamlit Tutorials")

# Header/Subheader
st.header("This is a header")
st.subheader("This is a subheader")

# Text
st.text("Hello Streamlit")

# Markdown
st.markdown("### This is a Markdown")

# Error/Colorful Text
st.success("Successful")
st.info("Information!")
st.warning("This is a warning")
st.error("This is an error Danger")
st.exception("NameError('name three not defined')")

# Get Help Info About Python
st.help(range)

# Writing Text/Super Fxn
st.write("Text with write")
st.write(range(10))

# Image
from PIL import Image
img = Image.open("example.jpeg")
st.image(img,width=300, caption="Sample Image")

# Audio
audio_file = open("samplemusic.mp3", "rb").read()
st.audio(audio_file, format='audio/mp3', start_time=0)


# Videos
vid_file = open("corona.mp4", "rb").read()
# vid_bytes = vid_file.read()
st.video(vid_file)



# Widget
# Checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding Widget")

# Radio button
status = st.radio("What is your status", ("Active","Inactive"))

if status == 'Active':
    st.success("You are Active")
else:
    st.warning("Inactive, Activate")

# SelectBox
occupation = st.selectbox("Your Occupation",["Programmer","Doctor",
                    "lawer", "Teacher"])
st.write("You selected this occupation: ", occupation)

# MultiSelect
location = st.multiselect("Where do you work?", ("London","New York","Accra", "Kiev","Nepal"))
st.write("You selected", len(location), "locations")

# Slider
level = st.slider("What is your level", 1,5)

# Buttons
st.button("Simple Button")

if st.button("About"):
    st.text("Streamlit is Cool")

# Text input
firstname = st.text_input("Enter Your Firstname", "Type Here..")
if st.button("Submit"):
    result = firstname.title()
    st.success(result)

# Text Area
message = st.text_area("Enter Your message","Type Here..")
if st.button("Submit2"):
    result1 = message.title()
    st.success(result1)

# Date Input
import datetime
today = st.date_input("Today is", datetime.datetime.now())

# Time
the_time = st.time_input("The time is", datetime.datetime.now())

# Displaying JSON
st.text("Display JSON")
st.json({'name':"Jessy", 'gender':"male", 'age':"25"})

# Display Raw code
st.text("Display Raw Code")
st.code("import numpy as np")

# Display Raw code
with st.echo():
    # This will also show as a comment
    import pandas as pd
    df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    })

# Progress Bar
import time
my_bar = st.progress(0)
for p in range(100):
    my_bar.progress(p+1)
    time.sleep(0.1)

# Spinner
with st.spinner("Wating .."):
    time.sleep(2)
st.success("Finished!")

# Balloons
st.balloons()

# SIDEBARS
st.sidebar.header("About")
st.sidebar.text("This is Streamlit Tut")

# Functions
@st.cache
def run_fxn():
    return range(10)
st.write(run_fxn())

# Plot
#st.pyplot()

# DataFrames
st.dataframe(df)

# Tables
st.table(df)



