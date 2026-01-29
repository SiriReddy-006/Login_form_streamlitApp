import streamlit as st

#Header of the application
st.header("Students Record Management")
st.header("By Siri Reddy Gopu")

#Title of teh application
st.title("Student Management System")

#Subheader of the application
st.subheader("Manage student records with Create, Read, Update, and Delete operations")

#horizontal line
st.markdown("--------------------------------------------------------")

#text method to display information 
st.text("This application allows you to perform CRUD operations on student records using a MySQL database.")


#write method to provide additional details
st.write("hello siri")

#Markdown for formatted text
st.markdown("### Features of application:")
st.markdown("** Bold Text**")
st.markdown("*Italic Text*")
st.markdown("-Item 1\n- Item 2")

st.markdown("<h3 style='color:red'>Done Students</h3>",
unsafe_allow_html=True)
#caption method to add captions
st.caption("This is a caption for the student management system.")

#code method to display code snippets
st.code("""
def add(a,b):
return a + b
""",language="python")


st.latex(r'''
a^2 + b^2 = c^2
''')

#Dividermethod to seperate actions
st.divider()

#button method to create a button 
if st.button("click me"):
    st.write("button clicked!")
    st.success("operation successful!")
    st.balloons()
else:
    st.write("button not clicked yet.")
    st.error("connection error!")
#text input method to get user input
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello,{name}!")   
else:
    st.write("please enter you name")
if name == "":
    st.warning("Name cannot be empty!")
elif not name.isalpha():
    st.error("Invalid input please enter only alphabets(no numbers or symbols).")    
feedback = st.text_area("enter feedback")
st.write("your feedback:",feedback)
#checkbox 
if st.checkbox("I agree to terms and conditions"):
    st.write("Thank you for agreeing!")
st.divider()
#radiobuton
gender = st.radio("select your gender:",("Male","Female","Other"))
st.write(f"you selected:{gender}")
st.divider()
#selectbox 
country = st.selectbox("select your country:",("India","Dubai","USA"))
st.write(f"you selected:{country}")
st.divider()
#multiselect
skills = st.multiselect("select your skills",["python","java","sql"])
st.write("skills:",skills)
st.divider()
#slider method
age = st.slider("select your age:",0,100,25)
st.write("your age:",age)
st.divider()
#file uploader method
uploaded_file = st.file_uploader("choose a file")
if uploaded_file is not None:
    st.success("File uploaded successfully!")
    st.write(f"Filename:{uploaded_file.name}")
st.divider()
#form method to create a form
with st.form("my_form"):
    name=st.text_input("name")
    age=st.number_input("age",0,100)
    submit=st.form_submit_button("submit")
if submit:
    st.write(name,age)
st.divider()
#form submit_button method to create a submit button inside a form 
with st.form("login"):
    user=st.text_input("username")
    pwd=st.text_input("password",type="password")
    login=st.form_submit_button("login")
if login:
    st.success("login successful")
st.divider()
#columns method to create columns
col1,col2,col3 = st.columns(3)
with col1:
    st.header("Column 1")
    st.write("This is column1")
with col2:
    st.header("Column 2")
    st.write("This is column2")
with col3:
    st.header("Column 3")
    st.write("This is column3")
st.divider()
container = st.container()
container.write("This is inside the container")
container.button("click here")
#table method to display data in tabular format
data={
    'Name': ['Anurag', 'Sumit', 'Rohit'],
    'Age': [21, 22, 20],
    'Course': ['B.Tech', 'M.Tech', 'BBA']
}
st.table(data)
st.divider()

#sidebar
st.sidebar.title("Menu")
option = st.sidebar.selectbox(
"Choose page",
["Home", "About", "Contact"]
)
st.sidebar.write(f"You selected: {option}")
st.divider()
#cache
@st.cache_data
def load_data():
    return [1,2,3,4]
data = load_data()
st.write(data)
