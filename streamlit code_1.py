

# import streamlit as st
# st.title("Hello, Edukron!")
# st.write("this is a simple streamlit app")

# import streamlit as st
# name= st.text_input("Enter your name")
# age= st.number_input("Enter your age:", min_value=1,max_value=100,step=1)

# if st.button("submit"):
#     st.write(f" hello {name}, you are {age} years old")

# import streamlit as st
# number= st.slider("pick a number",1,100,25)
# st.write(f"you selected a number {number}")


# import streamlit as st
# import pandas as pd
# import numpy as np

# df= pd.DataFrame(np.random.randn(10,2), columns= ["x","y"])

# st.write("Random DataFrame:")
# st.dataframe(df)


# import streamlit as st

# if st.checkbox("show message"):
#     st.write("you checked the box")

# gender= st.radio("select Gender", ("male","female","other"))
# st.write(f"you selected: {gender}")

# option= st.selectbox("choose an option",[ "option1 ","option 2","option 3"])
# st.write(f"you choose:{option}")


# import streamlit as st
# import time

# progress= st.progress(0)
# for i in range(100):
#     time.sleep(0.05)
#     progress.progress(i+1)


# import streamlit as st

# hobbies= st.multiselect("choose your hobbies", ["reading","sports","coding","travelling"])
# st.write(f"you selected: {hobbies}")

# import streamlit as st

# st.metric(label="revenue", value="$12000", delta= "+5%")
# st.metric(label="users", value="$1200",delta= "-2%")

# import streamlit as st
# from datetime import time

# t= st.time_input("pick a time")
# st.write(f"selected time: {t}")


import streamlit as st

tab1,tab2= st.tabs(["Tab1","Tab2"])

with tab1:
    st.write("content for tab 1")

with tab2:
    st.write("content for tab 2")
