import streamlit as st

def main():
    st.title("Home Network Risk Assessment")

    st.header("1. What Kind of Data Do You Use?")
    data_use = st.radio("Select one:", 
                        ["Sensitive Data (like financial or personal info)", 
                         "Just Surfing and Watching Shows"])

    st.header("2. How Many Devices Are Connected?")
    device_count = st.radio("Select one:", 
                            ["More than 5 devices", 
                             "5 or fewer devices"])

    st.header("3. How Do You Use Your Network?")
    network_use = st.radio("Select one:", 
                           ["Lots of online shopping, working from home, or dealing with private info", 
                            "Some shopping or checking emails", 
                            "Mostly just browsing or streaming"])

    st.header("4. What Kinds of Devices Are Connected?")
    device_type = st.radio("Select one:", 
                           ["Things like smart home gadgets or IoT devices", 
                            "Just computers, phones, and tablets", 
                            "Only one type of device (all computers or all tablets)"])

    st.header("5. Who Else Uses Your Network?")
    network_users = st.radio("Select one:", 
                             ["Many guests or people outside your family use it", 
                              "Sometimes guests use it", 
                              "Only your family uses it and no one else"])

    st.header("6. Have You Had Problems Before?")
    past_problems = st.radio("Select one:", 
                             ["Hacking or viruses before", 
                              "Some junk mail or ads popping up", 
                              "Never had any problems"])

    st.header("7. What Security Do You Already Have?")
    existing_security = st.radio("Select one:", 
                                 ["No security stuff like antivirus or firewalls", 
                                  "Some basic security like antivirus software", 
                                  "Really good security already"])

    st.header("8. How Careful Are You Online?")
    online_behaviour = st.radio("Select one:", 
                                ["Often download things from unknown places or risky clicks", 
                                 "Careful, but sometimes make mistakes", 
                                 "Very careful and never do risky stuff"])

    if st.button("Calculate Risk Level"):
        risk_score = calculate_risk_score(data_use, device_count, network_use, device_type, network_users, past_problems, existing_security, online_behaviour)
        st.subheader(f"Your Total Risk Level Score: {risk_score}")
        if risk_score >= 6:
            st.warning("High risk. You need strong security.")
        elif risk_score >= 3:
            st.warning("Moderate risk. Time to improve your security.")
        else:
            st.success("Basic risk. Simple security might be enough, but keep checking to stay safe.")

def calculate_risk_score(data_use, device_count, network_use, device_type, network_users, past_problems, existing_security, online_behaviour):
    risk_level = {
        "Sensitive Data (like financial or personal info)": 1,
        "Just Surfing and Watching Shows": 0,
        "More than 5 devices": 1,
        "5 or fewer devices": 0,
        "Lots of online shopping, working from home, or dealing with private info": 1,
        "Some shopping or checking emails": 0.5,
        "Mostly just browsing or streaming": 0,
        "Things like smart home gadgets or IoT devices": 1,
        "Just computers, phones, and tablets": 0.5,
        "Only one type of device (all computers or all tablets)": 0,
        "Many guests or people outside your family use it": 1,
        "Sometimes guests use it": 0.5,
        "Only your family uses it and no one else": 0,
        "Hacking or viruses before": 1,
        "Some junk mail or ads popping up": 0.5,
        "Never had any problems": 0,
        "No security stuff like antivirus or firewalls": 1,
        "Some basic security like antivirus software": 0.5,
        "Really good security already": 0,
        "Often download things from unknown places or risky clicks": 1,
        "Careful, but sometimes make mistakes": 0.5,
        "Very careful and never do risky stuff": 0
    }
    
    total_score = (
        risk_level[data_use] +
        risk_level[device_count] +
        risk_level[network_use] +
        risk_level[device_type] +
        risk_level[network_users] +
        risk_level[past_problems] +
        risk_level[existing_security] +
        risk_level[online_behaviour]
    )
    
    return total_score

if __name__ == "__main__":
    main()
