import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set page title
st.set_page_config(page_title="Streamlit Test App", page_icon="🧪")

# Main title
st.title("Streamlit Test Application")

# Add some text
st.write("Welcome to this sample Streamlit app. Let's explore some features!")

# Create a sidebar
st.sidebar.header("Sidebar Options")
option = st.sidebar.selectbox("Choose a section:", ["Data Display", "Chart", "Widget Demo"])

if option == "Data Display":
    st.header("Data Display Section")
    
    # Create a sample dataframe
    df = pd.DataFrame({
        'Column 1': [1, 2, 3, 4, 5],
        'Column 2': [10, 20, 30, 40, 50],
        'Column 3': [100, 200, 300, 400, 500]
    })
    
    st.subheader("Sample DataFrame")
    st.dataframe(df)
    
    st.subheader("Sample Table")
    st.table(df)

elif option == "Chart":
    st.header("Chart Section")
    
    # Generate sample data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # Create a line plot
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Sample Sine Wave')
    
    st.pyplot(fig)

else:
    st.header("Widget Demo Section")
    
    # Text input
    user_input = st.text_input("Enter your name:", "")
    if user_input:
        st.write(f"Hello, {user_input}!")
    
    # Slider
    age = st.slider("Select your age:", 0, 100, 25)
    st.write(f"You selected: {age} years old")
    
    # Checkbox
    if st.checkbox("Show additional info"):
        st.info("This is additional information that appears when the checkbox is selected.")
    
    # Button
    if st.button("Click me!"):
        st.balloons()

# Add a footer
st.markdown("---")
st.markdown("Created with ❤️ using Streamlit")
