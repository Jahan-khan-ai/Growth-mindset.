import streamlit as st

# set up our App
st.set_page_config(page_title="groth mindset challange",layout='centered')


# st.markdown("<style>.stapp{background-color:; /* */}</style>",unsafe_allow_html=True)


# Topic with HTML
st.markdown("<h1 style='text-align: center; color: white;background:green;'>🎯Growth Mindset Challenge!<br></h1>",unsafe_allow_html=True)



st.subheader('Hi I am your Host :rainbow["MUNAWAR JAHAN"]')

# input user name
name=st.text_input("***Your Good Name ?***")

st.button("Enter")

if name:
    # st.title("groth mindset challange")
    st.markdown(f'''<h2 style=' color: blue ; background: skyblue;'>✋😃{name} Welcome 😊<br>
        to Growth Mindset Challenge </h2>''', unsafe_allow_html=True)


    if st.markdown:
        # Defination
        st.header("*What is a Growth Mindset?*")
        st.write(""" :green-background[
        A growth mindset is the belief that your abilities and intelligence can be developed through hard work, perseverance, and learning from your mistakes. 
        This concept was popularized by psychologist Carol Dweck, and it challenges the notion that our skills are fixed from the start. 
        Instead, it reminds us that every challenge is an opportunity to learn and improve.
        ]""")

        # Fixed vs Growth Mindset
        st.subheader("Fixed Mindset vs Growth Mindset")
        st.write("""
        - **Fixed Mindset:** Abilities are innate, and failure is seen as a weakness.
        - **Growth Mindset:** Abilities can be developed through effort and experience, and failure is seen as a learning opportunity.
         """)

        # Image
        
        # st.image("D:\st_project\960x1.jpg", caption="Fixed vs Growth Mindset")


        #video
        st.header("watch & Learn More About Growth Mindset👩‍💻")
        st.video("https://www.youtube.com/watch?v=5XjJdAM_PRs")

        #Audio
        # st.header("Listen to a Motivational Audio🎧")
        # st.audio ("d:\st_project\Fixed Mindset Vs Growth Mindset Examples In Hindi Urdu.mp3") #autoplay=True)
    
        # Interactive Quiz
        st.header("Test Your Mindset")
        st.write("Answer the following questions to understand your mindset.")

        # Quastion
        q1 = st.radio("1. When you face a difficult task, how do you react?", 
                    ["I give up.", "I work hard and try to solve it.","I didn't think about this"])
        q2 = st.radio("2. What is your view on failure?", 
                    ["Failure means I am incapable.", "Failure is an opportunity to learn and improve.","I didn't think about this"])

        
            # Quiez
        if st.button("See Results"):
            score =0

            if q1 == "I give up.":
                score +=1
            if q2 == "Failure means I am incapable.":
                score +=1


            if q1 == "I work hard and try to solve it.":
                score +=4
            if q2 == "Failure is an opportunity to learn and improve.":
                score +=4

            
            if q1 == "I didn't think about this":
                score +=3
            if q2 == "I didn't think about this":
                score +=3
            

            #show answer
        
            if score ==8:
                st.success("Your mindset is a Growth Mindset! 🎉")
            
            elif score ==6:
                st.warning("you'r telling a lie.😡")
            
            elif score ==2:
                st.warning('''Your mindset is a Fixed Mindset.☹️ 
                Try adopting a Growth Mindset.🤗''')
            
            else:
                st.error("your answer isn't 'correct'🚫")

 
                    # if st.warning:
                        # suggestion & resources
                st.header("How to Adopt a Growth Mindset?")
                st.write("""
                - Embrace challenges.
                - Learn from mistakes.
                - Believe in effort.
                - Learn from others.  """)

                        
                st.header("Benefits of a Growth Mindset")
                st.write("The following graph shows the benefits of a Growth Mindset over time.")

                    # tABLE
                import pandas as pd
                data = pd.DataFrame({
                'Year': [2018, 2019, 2020, 2021, 2022],
                'Success Rate (%)': [60, 65, 70, 75, 80]
                            })

                    # gharph
                st.bar_chart(data.set_index('Year'))
            
                    
                st.write("Thank you for using the Growth Mindset Challenge App! 🚀")

    st.caption("Feedback")
    sentiment_mapping = ["one", "two", "three", "four", "five"]
    selected = st.feedback("stars")
    if selected is not None:
        st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")

