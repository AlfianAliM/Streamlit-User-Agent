import streamlit as st
from user_agents import parse

def main():
    st.title("User Agent Analyzer")
    
    # Input UA
    user_agent_input = st.text_input("Input User Agent:", "")
    
    if st.button("Analysis"):
        if user_agent_input:
            user_agent = parse(user_agent_input)
            # Device info
            st.subheader("Analysis Results:")
            st.write(f"**Device:** {user_agent.device.family}")
            st.write(f"**OS:** {user_agent.os.family} {user_agent.os.version_string}")
            st.write(f"**Browser:** {user_agent.browser.family} {user_agent.browser.version_string}")
            st.write(f"**Is mobile?** {'Yes' if user_agent.is_mobile else 'No'}")
            st.write(f"**Is tablet?** {'Yes' if user_agent.is_tablet else 'No'}")
            st.write(f"**Is PC?** {'Yes' if user_agent.is_pc else 'No'}")
        else:
            st.warning("Please enter user agent.")

if __name__ == "__main__":
    main()
