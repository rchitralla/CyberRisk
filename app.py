import streamlit as st

def main():
    st.title("Enhanced Home Network Risk Assessment")
    st.write("""
    This assessment gauges how secure your home network might be, based on how you use it and 
    what security measures you have in place. Answer the questions below to receive a risk score 
    and personalized recommendations.

    Created by Regina Chitralla
    """)

    # 1. What Kind of Data Do You Use?
    st.header("1. What Kind of Data Do You Use?")
    data_use = st.radio(
        "Select one:",
        [
            "Highly sensitive data (financial details, personal ID, medical records)",
            "Moderate personal data (shopping, email, social media)",
            "Mostly casual browsing/streaming"
        ]
    )
    st.write("**Why This Matters:** Handling financial or personal data increases your target value for cybercriminals.")

    # 2. How Many Devices Are Connected?
    st.header("2. How Many Devices Are Connected?")
    device_count = st.radio(
        "Select one:",
        [
            "6 or more devices",
            "2-5 devices",
            "Just 1 device"
        ]
    )
    st.write("**Why This Matters:** More devices = broader attack surface. Each device can be an entry point for threats.")

    # 3. How Do You Use Your Network?
    st.header("3. How Do You Use Your Network?")
    network_use = st.radio(
        "Select one:",
        [
            "Heavily (work from home, confidential data, online banking)",
            "Moderate (some shopping, email, occasional downloads)",
            "Light (mostly browsing or streaming)"
        ]
    )
    st.write("**Why This Matters:** Intensive activities like online banking or handling work files can magnify security risks.")

    # 4. What Kinds of Devices Are Connected?
    st.header("4. What Kinds of Devices Are Connected?")
    device_type = st.radio(
        "Select one:",
        [
            "A mix of computers, phones, tablets, and IoT (cameras, smart home, etc.)",
            "Mostly computers, phones, tablets (few or no IoT devices)",
            "Only one type of device (all computers or all tablets)"
        ]
    )
    st.write("**Why This Matters:** IoT devices often have weak default security, adding potential vulnerabilities.")

    # 5. Do You Have a Separate Guest Network?
    st.header("5. Do You Have a Separate Guest Network?")
    guest_network = st.radio(
        "Select one:",
        [
            "No, guests share my main Wi-Fi",
            "Yes, I have a dedicated guest network",
            "I never have guests connecting"
        ]
    )
    st.write("**Why This Matters:** A guest network isolates visitors’ devices from your main network, reducing risk.")

    # 6. Who Else Uses Your Network?
    st.header("6. Who Else Uses Your Network?")
    network_users = st.radio(
        "Select one:",
        [
            "Many guests or people outside your family use it regularly",
            "Sometimes guests use it",
            "Only your household uses it"
        ]
    )
    st.write("**Why This Matters:** The more people using your network, the harder it is to control safe behavior.")

    # 7. Have You Had Problems Before?
    st.header("7. Have You Had Problems Before?")
    past_problems = st.radio(
        "Select one:",
        [
            "Serious incidents (hacking, ID theft, major virus infections)",
            "Minor issues (spam, adware, mild virus, etc.)",
            "Never had any problems"
        ]
    )
    st.write("**Why This Matters:** Past issues might indicate vulnerabilities or risky habits that remain unaddressed.")

    # 8. What Security Do You Already Have?
    st.header("8. What Security Do You Already Have?")
    existing_security = st.radio(
        "Select one:",
        [
            "No security software or firewall at all",
            "Basic antivirus or firewall",
            "Robust security (firewall, antivirus, secure router settings, etc.)"
        ]
    )
    st.write("**Why This Matters:** Antivirus, firewalls, and secure router settings are critical layers of defense.")

    # 9. How Are Your Password Habits?
    st.header("9. How Are Your Password Habits?")
    password_habits = st.radio(
        "Select one:",
        [
            "Re-use passwords or use weak passwords (names, birthdates, etc.)",
            "Try to use strong passwords, but reuse them occasionally",
            "Unique, strong passwords for all accounts (possibly with a password manager)"
        ]
    )
    st.write("**Why This Matters:** Weak or reused passwords are a top reason for account breaches.")

    # 10. Do You Use Multi-Factor Authentication (MFA)?
    st.header("10. Do You Use MFA on Important Accounts?")
    mfa_usage = st.radio(
        "Select one:",
        [
            "No, I rely only on passwords",
            "Sometimes, for critical accounts like banking",
            "Yes, for all major accounts (email, social media, banking, etc.)"
        ]
    )
    st.write("**Why This Matters:** MFA significantly reduces the risk of unauthorized access, even if passwords leak.")

    # 11. Do You Keep Your Software/Devices Updated?
    st.header("11. Do You Keep Your Software/Devices Updated?")
    updates = st.radio(
        "Select one:",
        [
            "I rarely update or disable auto-updates",
            "I sometimes update but not consistently",
            "I install updates ASAP or have auto-updates enabled"
        ]
    )
    st.write("**Why This Matters:** Updates patch known vulnerabilities. Skipping them leaves you open to known exploits.")

    # 12. How About Your Router Firmware and Encryption?
    st.header("12. How About Your Router Firmware and Encryption?")
    router_security = st.radio(
        "Select one:",
        [
            "I never update my router firmware or use outdated Wi-Fi security (like WEP)",
            "I use WPA2, but router firmware updates are sporadic",
            "I use WPA2/WPA3 with regular firmware updates"
        ]
    )
    st.write("**Why This Matters:** The router is your gateway to the internet. Weak router settings can compromise all connected devices.")

    # 13. Do You Regularly Back Up Important Data?
    st.header("13. Do You Regularly Back Up Important Data?")
    backup_practices = st.radio(
        "Select one:",
        [
            "I never back up or rarely do",
            "I back up occasionally to an external drive or cloud",
            "I have an automated backup routine (local + cloud)"
        ]
    )
    st.write("**Why This Matters:** If devices are compromised (e.g., ransomware), backups are your lifeline.")

    # 14. How Careful Are You with Unknown Downloads and Links?
    st.header("14. How Careful Are You with Unknown Downloads and Links?")
    online_behaviour = st.radio(
        "Select one:",
        [
            "I often download files or click links from unknown sources",
            "I’m usually careful, but I slip up sometimes",
            "I’m very cautious; I verify sources before downloading or clicking"
        ]
    )
    st.write("**Why This Matters:** Phishing and malicious downloads remain the most common methods of system compromise.")

    # Final Button to Calculate Risk
    if st.button("Calculate Risk Level"):
        risk_score = calculate_risk_score(
            data_use, device_count, network_use, device_type, guest_network,
            network_users, past_problems, existing_security, password_habits,
            mfa_usage, updates, router_security, backup_practices, online_behaviour
        )

        # Color-coded results for improved UX
        if risk_score >= 10:
            st.markdown(f"<h3 style='color: red;'>Your Total Risk Level Score: {risk_score} (HIGH RISK)</h3>", unsafe_allow_html=True)
            st.error("You should improve your security measures immediately!")
        elif risk_score >= 6:
            st.markdown(f"<h3 style='color: orange;'>Your Total Risk Level Score: {risk_score} (MODERATE RISK)</h3>", unsafe_allow_html=True)
            st.warning("You have some security measures in place, but there’s room for improvement.")
        else:
            st.markdown(f"<h3 style='color: green;'>Your Total Risk Level Score: {risk_score} (LOW RISK)</h3>", unsafe_allow_html=True)
            st.success("Your security looks decent, but stay vigilant!")

        # Provide expanded recommendations
        recommendations = get_recommendations(risk_score, data_use, device_type, past_problems)
        if recommendations:
            st.markdown("### Recommended Next Steps")
            for rec in recommendations:
                st.markdown(f"- {rec}")


def calculate_risk_score(data_use, device_count, network_use, device_type, guest_network,
                         network_users, past_problems, existing_security, password_habits,
                         mfa_usage, updates, router_security, backup_practices, online_behaviour):
    """
    A more granular scoring system, using 0.25 for minimal risks and up to 1.5 for major risks.
    """

    risk_level = {
        # Data Use
        "Highly sensitive data (financial details, personal ID, medical records)": 1.5,
        "Moderate personal data (shopping, email, social media)": 1,
        "Mostly casual browsing/streaming": 0.25,

        # Device Count
        "6 or more devices": 1,
        "2-5 devices": 0.5,
        "Just 1 device": 0,

        # Network Use
        "Heavily (work from home, confidential data, online banking)": 1.5,
        "Moderate (some shopping, email, occasional downloads)": 1,
        "Light (mostly browsing or streaming)": 0.5,

        # Device Types
        "A mix of computers, phones, tablets, and IoT (cameras, smart home, etc.)": 1.5,
        "Mostly computers, phones, tablets (few or no IoT devices)": 1,
        "Only one type of device (all computers or all tablets)": 0.5,

        # Guest Network
        "No, guests share my main Wi-Fi": 1,
        "Yes, I have a dedicated guest network": 0,
        "I never have guests connecting": 0,

        # Network Users
        "Many guests or people outside your family use it regularly": 1,
        "Sometimes guests use it": 0.5,
        "Only your household uses it": 0,

        # Past Problems
        "Serious incidents (hacking, ID theft, major virus infections)": 1.5,
        "Minor issues (spam, adware, mild virus, etc.)": 0.75,
        "Never had any problems": 0,

        # Existing Security
        "No security software or firewall at all": 1.5,
        "Basic antivirus or firewall": 0.75,
        "Robust security (firewall, antivirus, secure router settings, etc.)": 0,

        # Password Habits
        "Re-use passwords or use weak passwords (names, birthdates, etc.)": 1.5,
        "Try to use strong passwords, but reuse them occasionally": 0.75,
        "Unique, strong passwords for all accounts (possibly with a password manager)": 0,

        # MFA Usage
        "No, I rely only on passwords": 1,
        "Sometimes, for critical accounts like banking": 0.5,
        "Yes, for all major accounts (email, social media, banking, etc.)": 0,

        # Updates
        "I rarely update or disable auto-updates": 1,
        "I sometimes update but not consistently": 0.5,
        "I install updates ASAP or have auto-updates enabled": 0,

        # Router Security
        "I never update my router firmware or use outdated Wi-Fi security (like WEP)": 1.5,
        "I use WPA2, but router firmware updates are sporadic": 0.75,
        "I use WPA2/WPA3 with regular firmware updates": 0,

        # Backup Practices
        "I never back up or rarely do": 1,
        "I back up occasionally to an external drive or cloud": 0.5,
        "I have an automated backup routine (local + cloud)": 0,

        # Online Behaviour
        "I often download files or click links from unknown sources": 1,
        "I’m usually careful, but I slip up sometimes": 0.5,
        "I’m very cautious; I verify sources before downloading or clicking": 0
    }

    # Summation
    total_score = (
        risk_level[data_use] +
        risk_level[device_count] +
        risk_level[network_use] +
        risk_level[device_type] +
        risk_level[guest_network] +
        risk_level[network_users] +
        risk_level[past_problems] +
        risk_level[existing_security] +
        risk_level[password_habits] +
        risk_level[mfa_usage] +
        risk_level[updates] +
        risk_level[router_security] +
        risk_level[backup_practices] +
        risk_level[online_behaviour]
    )

    return total_score


def get_recommendations(risk_score, data_use, device_type, past_problems):
    """
    Provide more specific security recommendations based on the user's risk score
    AND certain choices that indicate specialized needs or vulnerabilities.
    """
    recs = []

    # General recommendations based on risk score
    if risk_score >= 10:
        recs.append("Immediately update your router’s firmware and consider upgrading to a model supporting WPA3.")
        recs.append("Install or enhance antivirus/firewall solutions on all devices.")
        recs.append("Use a password manager to create strong, unique passwords.")
        recs.append("Enable MFA on all critical accounts (email, banking, social media).")
        recs.append("Perform regular security audits (e.g., check for unknown devices on your network).")
    elif risk_score >= 6:
        recs.append("Strengthen or update your Wi-Fi encryption settings (WPA2 or WPA3).")
        recs.append("Use multi-factor authentication (MFA) wherever possible, especially for banking and email.")
        recs.append("Regularly back up important data (at least weekly to a secure cloud and/or external drive).")
        recs.append("Schedule routine router firmware updates and check for IoT vulnerabilities.")
        recs.append("Review guest network settings or create a separate guest network if possible.")
    else:
        recs.append("Maintain your current security posture—stay vigilant about software updates.")
        recs.append("Keep using strong passwords and MFA where available.")
        recs.append("Consider automating regular backups (both cloud and local copies).")
        recs.append("Double-check your router is updated for ongoing protection.")

    # Specialized recommendations based on user’s choices
    # Example: If they handle "Highly sensitive data" but didn’t get a high total score
    if data_use == "Highly sensitive data (financial details, personal ID, medical records)":
        recs.append("Consider using a dedicated VPN service for all sensitive transactions or remote work.")
        recs.append("Audit third-party apps/services that have access to personal data.")

    # If the user has many IoT devices
    if device_type.startswith("A mix of computers"):
        recs.append("Change default passwords on IoT devices, and separate them on a different VLAN or guest network.")

    # If the user had serious hacking or identity theft incidents before
    if past_problems == "Serious incidents (hacking, ID theft, major virus infections)":
        recs.append("Monitor your credit reports and consider identity theft protection services.")
        recs.append("Immediately change all important account passwords and check for suspicious logins.")

    return recs

if __name__ == "__main__":
    main()
