import streamlit as st
import functions as fn

todos = fn.get_todos()


def add_todo():
    todo_add = st.session_state["new_todo"] + "\n"
    todos.append(todo_add)
    fn.write_todos(todos)
    st.session_state.new_todo = ""


def remove_todo():
    todo_remove = st.session_state[""]


st.title('My Todo App')
st.subheader('This is my todo app')
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.capitalize(), key=todo)
    if checkbox:
        todos.pop(index)
        fn.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
    #fn.get_todos()

st.text_input(label="Enter Todo", placeholder="Add new todo...", on_change=add_todo, key="new_todo")
