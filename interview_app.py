import streamlit as st

# Title of the web application
st.title("Python Backend Developer Interview - Questions & Answers")

# Initialize session state variables if not already initialized
if 'age' not in st.session_state:
    st.session_state.age = ""

if 'location' not in st.session_state:
    st.session_state.location = ""

if 'salary_current' not in st.session_state:
    st.session_state.salary_current = ""

if 'salary_expected' not in st.session_state:
    st.session_state.salary_expected = ""

if 'notice_period' not in st.session_state:
    st.session_state.notice_period = ""

if 'education' not in st.session_state:
    st.session_state.education = ""

if 'linkedin_profile' not in st.session_state:
    st.session_state.linkedin_profile = ""

if 'technical_certificates' not in st.session_state:
    st.session_state.technical_certificates = ""

if 'experience_python_cloud' not in st.session_state:
    st.session_state.experience_python_cloud = ""

if 'cloud_services' not in st.session_state:
    st.session_state.cloud_services = ""

if 'django_flask' not in st.session_state:
    st.session_state.django_flask = ""

if 'cloud_infrastructure' not in st.session_state:
    st.session_state.cloud_infrastructure = ""

if 'databases' not in st.session_state:
    st.session_state.databases = ""

if 'docker_kubernetes' not in st.session_state:
    st.session_state.docker_kubernetes = ""

if 'api_experience' not in st.session_state:
    st.session_state.api_experience = ""

if 'message_brokers' not in st.session_state:
    st.session_state.message_brokers = ""

if 'security_best_practices' not in st.session_state:
    st.session_state.security_best_practices = ""

if 'oauth_jwt' not in st.session_state:
    st.session_state.oauth_jwt = ""

if 'iot_protocols' not in st.session_state:
    st.session_state.iot_protocols = ""

if 'iot_scaling' not in st.session_state:
    st.session_state.iot_scaling = ""

if 'iot_services' not in st.session_state:
    st.session_state.iot_services = ""

if 'time_series_databases' not in st.session_state:
    st.session_state.time_series_databases = ""

if 'serverless_architecture' not in st.session_state:
    st.session_state.serverless_architecture = ""

# Section for personal information
st.header("Personal Information")
st.session_state.age = st.text_input("How old are you?", value=st.session_state.age)
st.session_state.location = st.text_input("Where're you located? (Country – City)", value=st.session_state.location)
st.session_state.salary_current = st.text_input("Current Monthly Salary", value=st.session_state.salary_current)
st.session_state.salary_expected = st.text_input("Expected Monthly Salary in SAR.", value=st.session_state.salary_expected)
st.session_state.notice_period = st.text_input("How much is your notice period? (consider this is a full-time job)", value=st.session_state.notice_period)

# Section for education and profile
st.header("Education and Profile")
st.session_state.education = st.text_input("Please mention your education.", value=st.session_state.education)
st.session_state.linkedin_profile = st.text_input("Kindly mention your LinkedIn profile", value=st.session_state.linkedin_profile)

# Section for technical skills and certifications
st.header("Technical Skills & Certifications")
st.session_state.technical_certificates = st.text_input("Do you hold any Technical Certificates? if yes, please mention", value=st.session_state.technical_certificates)
st.session_state.experience_python_cloud = st.text_input("How many years of experience with Python in a cloudy environment?", value=st.session_state.experience_python_cloud)
st.session_state.cloud_services = st.text_input("Do you have Strong understanding of cloud services (AWS or Azure)?", value=st.session_state.cloud_services)

# Section for additional experience and skills
st.header("Experience & Skills")
st.session_state.django_flask = st.text_input("How many years of experience with Django or Flask?", value=st.session_state.django_flask)
st.session_state.cloud_infrastructure = st.text_input("How many years of experience with cloud infrastructure (preferably AWS or Azure)?", value=st.session_state.cloud_infrastructure)
st.session_state.databases = st.text_input("Do you have Strong knowledge of relational (PostgreSQL, MySQL) and NoSQL databases (MongoDB, Cassandra)?", value=st.session_state.databases)
st.session_state.docker_kubernetes = st.text_input("Do you have Experience with Docker for containerization and Kubernetes for orchestration?", value=st.session_state.docker_kubernetes)
st.session_state.api_experience = st.text_input("Do you have Proficiency in building and optimizing RESTful or gRPC APIs?", value=st.session_state.api_experience)
st.session_state.message_brokers = st.text_input("Are you Familiar with message brokers and event streaming (e.g., Kafka, RabbitMQ)?", value=st.session_state.message_brokers)
st.session_state.security_best_practices = st.text_input("Do you have Strong understanding of security best practices in backend development?", value=st.session_state.security_best_practices)
st.session_state.oauth_jwt = st.text_input("Are you Familiar with OAuth2, JWT, and secure communication methods?", value=st.session_state.oauth_jwt)
st.session_state.iot_protocols = st.text_input("Do you have Experience with IoT protocols such as MQTT, CoAP, or AMQP?", value=st.session_state.iot_protocols)
st.session_state.iot_scaling = st.text_input("Do you have experience building and scaling IoT platforms?", value=st.session_state.iot_scaling)
st.session_state.iot_services = st.text_input("Do you have Experience with cloud-based IoT services like AWS IoT Core or Azure IoT Hub?", value=st.session_state.iot_services)
st.session_state.time_series_databases = st.text_input("Do you have Knowledge of time-series databases for handling IoT telemetry data?", value=st.session_state.time_series_databases)
st.session_state.serverless_architecture = st.text_input("Do you have Strong grasp of serverless architectures and event-driven systems?", value=st.session_state.serverless_architecture)

# Submit button
if st.button("Submit"):
    # Display collected responses with better spacing and new lines
    st.subheader("Your Responses:")

    # Use Markdown with custom HTML to add spacing between questions and answers
    st.markdown(f"**How old are you?**<br>{st.session_state.age}", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)  # Adds 0.5cm spacing between each Q&A

    st.markdown(f"**Where're you located? (Country – City)**<br>{st.session_state.location}", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"**Current Monthly Salary**<br>{st.session_state.salary_current}", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"**Expected Monthly Salary in SAR**<br>{st.session_state.salary_expected}", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"**How much is your notice period?**<br>{st.session_state.notice_period}", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"**Education**<br>{st.session_state.education}", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"**LinkedIn Profile**<br>{st.session_state.linkedin_profile}", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"**Technical Certifications**<br>{st.session_state.technical_certificates}", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"**Years of experience with Python in a cloudy environment**<br>{st.session_state.experience_python_cloud}", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"**Cloud Services (AWS or Azure)**<br>{st.session_state.cloud_services}", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"**Years of experience with Django or Flask**<br>{st.session_state.django_flask}", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"**Years of experience with cloud infrastructure**<br>{st.session_state.cloud_infrastructure}", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"**Knowledge of relational and NoSQL databases**<br>{st.session_state.databases}", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"**Experience with Docker and Kubernetes**<br>{st.session_state.docker_kubernetes}", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"**Proficiency in building and optimizing APIs**<br>{st.session_state.api_experience}", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"**Familiarity with message brokers and event streaming**<br>{st.session_state.message_brokers}", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"**Security best practices in backend development**<br>{st.session_state.security_best_practices}", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"**Familiarity with OAuth2, JWT, and secure communication methods**<br>{st.session_state.oauth_jwt}", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"**Experience with IoT protocols**<br>{st.session_state.iot_protocols}", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"**Experience with scaling IoT platforms**<br>{st.session_state.iot_scaling}", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"**Experience with IoT cloud services**<br>{st.session_state.iot_services}", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"**Knowledge of time-series databases for IoT**<br>{st.session_state.time_series_databases}", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"**Grasp of serverless architectures and event-driven systems**<br>{st.session_state.serverless_architecture}", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

