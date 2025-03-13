import streamlit as st # for the web interface
import random # for randomizing the questions
import time # for the timer

# Title of the Application
st.title("📝 Quizzy Checkup")

# Define quiz questions, options, and answer in the form of a list of dictionaries
questions = [
    {
       "question": "What is the capital of Pakistan?",
        "options":["Karachi", "Lahore","Peshawar","Islamamad"],
        "answer":"Islamabad",
    },
    {
        "question":"Who is the founder of Pakistan?",
        "options":[
            "Quaid-e-Azam Mohammad Ali Jinnah",
            "Liaquat Ali Khan",
            "Benazir Bhutoo",
            "Allama Iqbal",
        ],
        "answer":"Quaid-e-Azam Mohammad Ali Jinnah"
    },
    {
        "question":"What is the national languafge of Pakistan?",
        "options":[
            "Urdu",
            "Sindhi",
            "French",
            "Arabic",
        ],
        "answer":"Urdu"
    },
    {
        "question": "Which is the highest mountain in Pakistan?",
        "options": [
            "Nanga Parbat",
            "K2",
            "Mount Everest",
            "Rakaposhi"
        ],
        "answer": "K2"
    },
    {
        "question": "Which city is known as the 'City of Lights' in Pakistan?",
        "options": [
            "Lahore",
            "Islamabad",
            "Karachi",
            "Quetta"
        ],
        "answer": "Karachi"
    },
    {
        "question": "What is the currency of Pakistan?",
        "options": [
            "Rupee",
            "Taka",
            "Dinar",
            "Rial"
        ],
        "answer": "Rupee"
    },
    {
        "question": "Which is the largest province of Pakistan by area?",
        "options": [
            "Sindh",
            "Punjab",
            "Balochistan",
            "Khyber Pakhtunkhwa"
        ],
        "answer": "Balochistan"
    },
    {
        "question": "Which is the national bird of Pakistan?",
        "options": [
            "Chukar Partridge",
            "Peacock",
            "Eagle",
            "Falcon"
        ],
        "answer": "Chukar Partridge"
    },
    {
        "question": "When did Pakistan become an independent country?",
        "options": [
            "14 August 1947",
            "23 March 1940",
            "15 August 1947",
            "26 January 1950"
        ],
        "answer": "14 August 1947"
    },
    {
        "question": "Which ocean borders Pakistan to the south?",
        "options": [
            "Atlantic Ocean",
            "Pacific Ocean",
            "Indian Ocean",
            "Arctic Ocean"
        ],
        "answer": "Indian Ocean"
    },
    {
        "question": "Who wrote the national anthem of Pakistan?",
        "options": [
            "Allama Iqbal",
            "Hafeez Jalandhari",
            "Faiz Ahmed Faiz",
            "Josh Malihabadi"
        ],
        "answer": "Hafeez Jalandhari"
    },
]
# Initialize a random question if none exists in the session state
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

# Get the current question from session state
question = st.session_state.current_question

# Display the question
st.subheader(question["question"])

# Create radio buttons for the options
selected_option = st.radio("Choose your answer", question["options"], key="answer")

# Submit button the check the answer
if st.button("Submit Answer"):
    # check if the answer is correct
    if selected_option == question["answer"]:
        st.success("✅ Correct!")
        st.balloons()
    else:
        st.error("❌ Incorrect! the correct answer is " + question["answer"])
  
    # Wait for 3 seconds before showing the next question
    time.sleep(5)

    # Select a new random question
    st.session_state.current_question = random.choice(questions)

    # Rerun the app to display the next question    
    st.rerun()

