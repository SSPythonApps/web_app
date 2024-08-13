import streamlit as st
import FruitList as fl

st.set_page_config(layout="wide")

items = fl.GetFruitList()

def OnItemInput():
    item = st.session_state["kItemInput"]
    fl.AddFruit(item)
    st.session_state["kItemInput"] = ""


st.title('Food Inventory')
st.subheader("By: Shahil Saha")
st.write("<b>Test Method</b>", unsafe_allow_html=True)
st.text_input(label='Enter your favorite fruit', placeholder='eg: Mango', on_change=OnItemInput, key="kItemInput")


with st.container(border= True):
    for index, i in enumerate(items):
        chk = st.checkbox(i, key=i)
        
        if chk:
            items.pop(index)
            fl.ModifyFruitList(items)
            del st.session_state[i]
            st.rerun()

