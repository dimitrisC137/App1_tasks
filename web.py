import streamlit as st
import functions

tasks = functions.read_txt()


def add_task():
    new_task = st.session_state["new_task"] + "\n"
    tasks.append(new_task)
    functions.write_txt(tasks)


st.title("Task App")
st.subheader("This is today's task list.")
st.write("")

for index, task in enumerate(tasks):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        tasks.pop(index)
        functions.write_txt(tasks)
        del st.session_state[task]
        st.experimental_rerun()


st.text_input(label="", placeholder=" Add a new task ...",
              on_change=add_task, key='new_task')
