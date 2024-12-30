import streamlit as st

def main():
    st.title("Home Network Risk Assessment")
    st.write("""
    This assessment helps you gauge how secure your home network might be, based on how
    you use it and what security measures you have in place.
    """)

    st.header("1. What Kind of Data Do You Use?")
    data_use = st.radio("Select one:", 
                        ["Sensitive Data (like financial or personal info)", 
                         "I'm Just Surfing and Watching Shows"])

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
                           ["Things like smart home gadgets (cameras, thermostats, IoT)", 
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
                                  "Really good security already (firewall, antivirus, secure router settings)"])

    st.header("8. How Careful Are You Online?")
    online_behaviour = st.radio("Select one:", 
                                ["Often download things from unknown places or click risky links", 
                                 "Careful, but sometimes make mistakes", 
                                 "Very careful and never do risky stuff"])

    # NEW QUESTIONS
    st.header("9. Do You Keep Your Software/Devices Updated?")
    updates = st.radio("Select one:", 
                       ["I rarely update my devices or I disable auto-updates", 
                        "I sometimes update but not consistently", 
                        "I always install updates ASAP or have auto-updates enabled"])

    st.header("10. Do You Use Strong Wi-Fi Encryption?")
    wifi_encryption = st.radio("Select one:", 
                               ["I use outdated security or I'm not sure (e.g., WEP or no password)", 
                                "I use WPA2 but the password might be weak", 
                                "I use WPA2 or WPA3 with a strong, unique password"])

    if st.button("Calculate Risk Level"):
        # Incorporate new questions into the risk calculation
        risk_score = calculate_risk_score(
            data_use, device_count, network_use, device_type, network_users, 
            past_problems, existing_security, online_behaviour, updates, wifi_encryption
        )
        st.subheader(f"Your Total Risk Level Score: {risk_score}")
        
        if risk_score >= 8:
            st.error("High Risk: You should improve your security measures immediately!")
        elif risk_score >= 4:
            st.warning("Moderate Risk: You have some security in place, but there’s room for improvement.")
        else:
            st.success("Low Risk: Your basic security seems okay, but stay vigilant!")

        # Provide a recommendations section based on the final score
        recommendations = get_recommendations(risk_score)
        if recommendations:
            st.markdown("### Recommended Next Steps")
            for rec in recommendations:
                st.markdown(f"- {rec}")

def calculate_risk_score(data_use, device_count, network_use, device_type, network_users, 
                         past_problems, existing_security, online_behaviour, updates, wifi_encryption):
    # Updated risk dictionary with new questions
    risk_level = {
        # Data usage
        "Sensitive Data (like financial or personal info)": 1,
        "I'm Just Surfing and Watching Shows": 0,

        # Device count
        "More than 5 devices": 1,
        "5 or fewer devices": 0,

        # Network use
        "Lots of online shopping, working from home, or dealing with private info": 1,
        "Some shopping or checking emails": 0.5,
        "Mostly just browsing or streaming": 0,

        # Device types
        "Things like smart home gadgets (cameras, thermostats, IoT)": 1,
        "Just computers, phones, and tablets": 0.5,
        "Only one type of device (all computers or all tablets)": 0,

        # Network users
        "Many guests or people outside your family use it": 1,
        "Sometimes guests use it": 0.5,
        "Only your family uses it and no one else": 0,

        # Past problems
        "Hacking or viruses before": 1,
        "Some junk mail or ads popping up": 0.5,
        "Never had any problems": 0,

        # Existing security
        "No security stuff like antivirus or firewalls": 1,
        "Some basic security like antivirus software": 0.5,
        "Really good security already (firewall, antivirus, secure router settings)": 0,

        # Online behaviour
        "Often download things from unknown places or click risky links": 1,
        "Careful, but sometimes make mistakes": 0.5,
        "Very careful and never do risky stuff": 0,

        # Updates
        "I rarely update my devices or I disable auto-updates": 1,
        "I sometimes update but not consistently": 0.5,
        "I always install updates ASAP or have auto-updates enabled": 0,

        # Wi-Fi encryption
        "I use outdated security or I'm not sure (e.g., WEP or no password)": 1,
        "I use WPA2 but the password might be weak": 0.5,
        "I use WPA2 or WPA3 with a strong, unique password": 0
    }
    
    total_score = (
        risk_level[data_use] +
        risk_level[device_count] +
        risk_level[network_use] +
        risk_level[device_type] +
        risk_level[network_users] +
        risk_level[past_problems] +
        risk_level[existing_security] +
        risk_level[online_behaviour] +
        risk_level[updates] +
        risk_level[wifi_encryption]
    )
    
    return total_score

def get_recommendations(risk_score):
    """
    Provide recommended steps based on the user's total risk score.
    """
    recommendations = []

    # High-risk user: 8 or more
    if risk_score >= 8:
        recommendations.append("Set up a robust firewall and install reputable antivirus software.")
        recommendations.append("Use a password manager to create and store strong, unique passwords.")
        recommendations.append("Enable WPA2/WPA3 encryption on your router with a strong password.")
        recommendations.append("Create a separate guest Wi-Fi network for visitors.")
        recommendations.append("Enable automatic software updates on all devices.")

    # Moderate-risk user: between 4 and 7
    elif risk_score >= 4:
        recommendations.append("Consider upgrading your router’s firmware and enabling strong Wi-Fi encryption (WPA2 or WPA3).")
        recommendations.append("Use multi-factor authentication (MFA) for important accounts (email, banking, etc.).")
        recommendations.append("Regularly scan your devices with antivirus/anti-malware tools.")
        recommendations.append("Review your IoT device settings and disable any default or weak passwords.")
        recommendations.append("Back up important data to both a cloud service and an external hard drive.")

    # Low-risk user: 3 or less
    else:
        recommendations.append("Keep devices updated with the latest security patches.")
        recommendations.append("Perform periodic security checkups to maintain good security hygiene.")
        recommendations.append("Regularly change your Wi-Fi and account passwords to ensure ongoing protection.")
        recommendations.append("Stay informed about the latest cybersecurity threats and best practices.")

    return recommendations

if __name__ == "__main__":
    main()
