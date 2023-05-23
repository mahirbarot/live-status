import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time

cred = credentials.Certificate(r"C:\Users\mahir\Desktop\ai_end\mini_project\serviceAccount.json")

# Initialize the Firebase app
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://smartdustbin-nuv-default-rtdb.firebaseio.com/'
# })

st.set_page_config(
        page_title="mini project",
        page_icon="house_buildings",
        layout='centered',
    )



# Reference to the root of the database
ref = db.reference('/arduino_data')

placeholder = st.empty()
Title=st.empty()
Title2=st.empty()
imgg=st.empty()



# Streamlit app code
def main():
    # Auto-update data every 5 seconds
    while True:
        st.empty()
        dustbins = ref.child('value').get()

        if dustbins is None:
            st.write('No data available.')
        else:
            if dustbins != 'too close!!':
                
                num=int(dustbins[:-2])
                if num>=15:
                    Title2.header("Dustbin is at safe levels")
                    imgg.image('6.png',width=380)
                elif(num<=15):
                    Title2.header("Dustbin is almost full")
                    imgg.image('8.png',width=380)
                    
                    
                placeholder.text(num)
                
            

            st.empty()  
            time.sleep(4) 
             


if __name__ == '__main__':
    main()




# placeholder = st.empty()
# >>>
# >>> # Replace the placeholder with some text:
# >>> placeholder.text("Hello")
# >>>
# >>> # Replace the text with a chart:
# >>> placeholder.line_chart({"data": [1, 5, 2, 6]})
# >>>
# >>> # Replace the chart with several elements:
# >>> with placeholder.container():
# ...     st.write("This is one element")
# ...     st.write("This is another")