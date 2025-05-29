import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Navixy Tracker Management", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .reportview-container .main .block-container {
        max-width: 800px;
        padding-top: 2rem;
        padding-right: 1rem;
        padding-left: 1rem;
        padding-bottom: 2rem;
    }
    .stButton>button {
        background-color: #007bff;
        color: white;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state variables
if 'server' not in st.session_state:
    st.session_state.server = None
if 'admin_hash' not in st.session_state:
    st.session_state.admin_hash = None
if 'tracker_choice' not in st.session_state:
    st.session_state.tracker_choice = None
if 'subpaas_hash' not in st.session_state:
    st.session_state.subpaas_hash = None
if 'selected_tracker_ids' not in st.session_state:
    st.session_state.selected_tracker_ids = []

# Function to show messages
def show_message(message, message_type):
    if message_type == "success":
        st.success(message)
    elif message_type == "error":
        st.error(message)
    elif message_type == "info":
        st.info(message)

# Server selection
st.title("Navixy Tracker Management")
st.header("Select your server")
server = st.radio("Server", ('EU Server', 'US Server'))
if server:
    st.session_state.server = server
    show_message(f"Server set to {server}", "success")

# Admin Hash Section
if st.session_state.server:
    st.header("Enter Admin Panel Hash")
    admin_hash = st.text_input("Admin Panel Hash", type="password")
    if st.button("Submit Hash"):
        if admin_hash:
            st.session_state.admin_hash = admin_hash
            show_message("Admin Hash set successfully!", "success")
        else:
            show_message("Please enter a valid Admin Panel Hash.", "error")

# Tracker Choice Section
if st.session_state.admin_hash:
    st.header("How do you want to select trackers?")
    tracker_choice = st.radio("Tracker Choice", ('Pre-selected list (SubPAAS)', 'Manually input object IDs', 'Trackers for one panel'))
    if tracker_choice:
        st.session_state.tracker_choice = tracker_choice

# SubPAAS Selection Section
if st.session_state.tracker_choice == 'Pre-selected list (SubPAAS)':
    st.header("Select a SubPAAS")
    subpaas_list = ["SubPAAS 1", "SubPAAS 2", "SubPAAS 3"]  # Example list
    subpaas = st.selectbox("SubPAAS List", subpaas_list)
    if st.button("Select SubPAAS"):
        st.session_state.subpaas_hash = subpaas
        show_message(f"Selected SubPAAS: {subpaas}", "success")

# Manual Input Section
if st.session_state.tracker_choice == 'Manually input object IDs':
    st.header("Enter Object IDs (comma separated)")
    manual_object_ids = st.text_input("Object IDs", placeholder="e.g., 123,456,789")
    if manual_object_ids:
        st.session_state.selected_tracker_ids = manual_object_ids.split(',')

# Clone Section
if st.session_state.selected_tracker_ids:
    st.header("Enter User ID to clone trackers to")
    clone_user_id = st.text_input("User ID")
    if st.button("Clone Trackers"):
        if clone_user_id:
            show_message(f"Trackers cloned successfully to User ID: {clone_user_id}", "success")
        else:
            show_message("Please enter a valid User ID.", "error")
