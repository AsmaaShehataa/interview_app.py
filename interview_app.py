import streamlit as st
import json
import os

# Function to load saved answers from the file
def load_answers():
    if os.path.exists("answers.json"):
        with open("answers.json", "r") as f:
            return json.load(f)
    return {}

# Function to save answers to the file
def save_answers(data):
    with open("answers.json", "w") as f:
        json.dump(data, f)

# Title of the web application
st.title("Python Backend Developer Interview - Questions & Answers")

# Load previously saved answers
answers = load_answers()

# Section for personal information
st.header("Personal Information")
st.session_state.age = st.text_input("How old are you?", value=answers.get('age', ''))
st.session_state.location = st.text_input("Where're you located? (Country – City)", value=answers.get('location', ''))
st.session_state.salary_current = st.text_input("Current Monthly Salary", value=answers.get('salary_current', ''))
st.session_state.salary_expected = st.text_input("Expected Monthly Salary in SAR.", value=answers.get('salary_expected', ''))
st.session_state.notice_period = st.text_input("How much is your notice period? (consider this is a full-time job)", value=answers.get('notice_period', ''))

# Section for education and profile
st.header("Education and Profile")
st.session_state.education = st.text_input("Please mention your education.", value=answers.get('education', ''))
st.session_state.linkedin_profile = st.text_input("Kindly mention your LinkedIn profile", value=answers.get('linkedin_profile', ''))

# Section for technical skills and certifications
st.header("Technical Skills & Certifications")
st.session_state.technical_certificates = st.text_input("Do you hold any Technical Certificates? if yes, please mention", value=answers.get('technical_certificates', ''))
st.session_state.experience_python_cloud = st.text_input("How many years of experience with Python in a cloudy environment?", value=answers.get('experience_python_cloud', ''))
st.session_state.cloud_services = st.text_input("Do you have Strong understanding of cloud services (AWS or Azure)?", value=answers.get('cloud_services', ''))

# Section for additional experience and skills
st.header("Experience & Skills")
st.session_state.django_flask = st.text_input("How many years of experience with Django or Flask?", value=answers.get('django_flask', ''))
st.session_state.cloud_infrastructure = st.text_input("How many years of experience with cloud infrastructure (preferably AWS or Azure)?", value=answers.get('cloud_infrastructure', ''))
st.session_state.databases = st.text_input("Do you have Strong knowledge of relational (PostgreSQL, MySQL) and NoSQL databases (MongoDB, Cassandra)?", value=answers.get('databases', ''))
st.session_state.docker_kubernetes = st.text_input("Do you have Experience with Docker for containerization and Kubernetes for orchestration?", value=answers.get('docker_kubernetes', ''))
st.session_state.api_experience = st.text_input("Do you have Proficiency in building and optimizing RESTful or gRPC APIs?", value=answers.get('api_experience', ''))
st.session_state.message_brokers = st.text_input("Are you Familiar with message brokers and event streaming (e.g., Kafka, RabbitMQ)?", value=answers.get('message_brokers', ''))
st.session_state.security_best_practices = st.text_input("Do you have Strong understanding of security best practices in backend development?", value=answers.get('security_best_practices', ''))
st.session_state.oauth_jwt = st.text_input("Are you Familiar with OAuth2, JWT, and secure communication methods?", value=answers.get('oauth_jwt', ''))
st.session_state.iot_protocols = st.text_input("Do you have Experience with IoT protocols such as MQTT, CoAP, or AMQP?", value=answers.get('iot_protocols', ''))
st.session_state.iot_scaling = st.text_input("Do you have experience building and scaling IoT platforms?", value=answers.get('iot_scaling', ''))
st.session_state.iot_services = st.text_input("Do you have Experience with cloud-based IoT services like AWS IoT Core or Azure IoT Hub?", value=answers.get('iot_services', ''))
st.session_state.time_series_databases = st.text_input("Do you have Knowledge of time-series databases for handling IoT telemetry data?", value=answers.get('time_series_databases', ''))
st.session_state.serverless_architecture = st.text_input("Do you have Strong grasp of serverless architectures and event-driven systems?", value=answers.get('serverless_architecture', ''))

# Submit button
if st.button("Submit"):
    # Gather all answers into a dictionary
    answers_data = {
        'age': st.session_state.age,
        'location': st.session_state.location,
        'salary_current': st.session_state.salary_current,
        'salary_expected': st.session_state.salary_expected,
        'notice_period': st.session_state.notice_period,
        'education': st.session_state.education,
        'linkedin_profile': st.session_state.linkedin_profile,
        'technical_certificates': st.session_state.technical_certificates,
        'experience_python_cloud': st.session_state.experience_python_cloud,
        'cloud_services': st.session_state.cloud_services,
        'django_flask': st.session_state.django_flask,
        'cloud_infrastructure': st.session_state.cloud_infrastructure,
        'databases': st.session_state.databases,
        'docker_kubernetes': st.session_state.docker_kubernetes,
        'api_experience': st.session_state.api_experience,
        'message_brokers': st.session_state.message_brokers,
        'security_best_practices': st.session_state.security_best_practices,
        'oauth_jwt': st.session_state.oauth_jwt,
        'iot_protocols': st.session_state.iot_protocols,
        'iot_scaling': st.session_state.iot_scaling,
        'iot_services': st.session_state.iot_services,
        'time_series_databases': st.session_state.time_series_databases,
        'serverless_architecture': st.session_state.serverless_architecture,
    }
    
    # Save the answers to a file
    save_answers(answers_data)

    # Display the collected responses
    st.subheader("Your Responses:")
    for question, answer in answers_data.items():
        st.write(f"**{question.replace('_', ' ').title()}**: {answer}")

