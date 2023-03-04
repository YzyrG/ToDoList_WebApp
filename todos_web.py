"""
To_Do_List Web style
"""

import streamlit as st  # streamlit 是开源的web前端框架
import todos_functions

# 修改page名称+增加page icon
st.set_page_config(page_title="ToDoListApp | ZYR", page_icon= "🧀")

todos = todos_functions.get_todos()


def add_todo():
    todo_new = st.session_state['new_todo'] + '\n'  # st.session_state是字典，'new_todo'是它的一个key
    todos.append(todo_new)
    todos_functions.put_todos(todos)
    st.session_state['new_todo'] = ""  # 新增一个todo后清空input输入框


# 标题部分
st.title("My Todo App")
st.subheader("This is my todo app!")
st.write("You can manage your todos in this app :)")

# 显示待勾选todo
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)  # 未勾选时，key: checkbox对应的value: false
    #  complete已勾选todo
    if checkbox:
        todos .pop(index)  # 从todos list中删去已勾选的todo
        todos_functions.put_todos(todos)
        del st.session_state[todo]  # 同时删除session_state中对应的键值
        st.experimental_rerun()
st.text_input(label="", placeholder="Enter a new todo.",
              on_change=add_todo, key="new_todo")

# st.session_state  # 测试用
