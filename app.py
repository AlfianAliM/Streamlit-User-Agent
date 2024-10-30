import streamlit as st
from user_agents import parse
import pandas as pd

st.title("User Agent Analyzer")

user_agent_input = st.text_input("Enter User Agent String:")

if user_agent_input:
    user_agent = parse(user_agent_input)

    st.header("Simplified Readout")
    st.write(f"**Software & Platform:** {user_agent.browser.family} {user_agent.browser.version_string} on {user_agent.os.family} ({user_agent.os.version_string})")
    st.write(f"**Detected Addons:** {user_agent.device.family}")
    st.write("---")

    st.header("Software Capabilities")
    st.write("**Browser:**", user_agent.browser.family)
    st.write("**Browser Version:**", user_agent.browser.version_string)
    st.write("**Mobile:**", user_agent.is_mobile)
    st.write("**Tablet:**", user_agent.is_tablet)
    st.write("**Touch Screen:**", user_agent.is_touch_capable)
    st.write("**Bot:**", user_agent.is_bot)
    st.write("---")

    st.header("Operating System Information")
    st.write("**Operating System:**", user_agent.os.family)
    st.write("**Operating System Version:**", user_agent.os.version_string)
    st.write("**OS Name Code:**", user_agent.os.family.lower())
    st.write("**OS Flavour:**", user_agent.os.version_string if user_agent.os.version_string else "---")
    st.write("---")

    st.header("Miscellaneous Information")
    st.write("**Operating Platform:**", user_agent.device.family)
    st.write("**Platform Code:**", user_agent.device.family.lower())
    st.write("**Platform Vendor Name:**", user_agent.device.brand if user_agent.device.brand else "---")
    st.write("---")

    st.header("Extra Info Table")
    extra_info_data = {
        "System Build": "N/A", 
        "Software Name": user_agent.browser.family,
        "Software Name Code": user_agent.browser.family.lower(),
        "Software Version": user_agent.browser.version_string,
        "Software Version (full)": "N/A",  
        "Layout Engine Name": "N/A",  
        "Layout Engine Version": "N/A",  
        "Software Type": "browser -> in-app-browser" if user_agent.is_bot else "browser",
        "Hardware Type": "mobile" if user_agent.is_mobile else "desktop",
    }

    st.write(pd.DataFrame.from_dict(extra_info_data, orient='index', columns=['Details']))
