import streamlit as st
import pandas

st.title('The Best Company')
st.write('Lorem ipsum dolor sit amet, '
             'consectetuer adipiscing elit. '
             'Aenean commodo ligula eget dolor. Aenean massa. '
             'Cum sociis natoque penatibus et magnis dis '
             'parturient montes, nascetur ridiculus mus. '
             'Donec quam felis, ultricies nec, pellentesque eu, '
             'pretium quis, sem. Nulla consequat massa quis enim. '
             'Donec pede justo, fringilla vel, aliquet nec, '
             'vulputate eget, arcu. In enim justo, rhoncus ut, '
             'imperdiet a, venenatis vitae, justo.')
st.subheader('Our Team')


col1, col2, col3 = st.columns(3)

df = pandas.read_csv('pages/employees.csv', sep=",")


def display_employees(row_local):
    full_name = row_local['first name'].title() + ' ' + row_local['last name'].title();
    st.subheader(full_name)
    st.write(row_local['role'])
    st.image(f"images/employees/{row_local['image']}")


with col1:
    for index, row in df[:4].iterrows():
        display_employees(row)


with col2:
    for index, row in df[4:8].iterrows():
        display_employees(row)


with col3:
    for index, row in df[8:].iterrows():
        display_employees(row)

# first name,last name,role,image