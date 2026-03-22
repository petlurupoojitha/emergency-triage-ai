def analyze_message(msg):
    msg = msg.lower()

    emergency_keywords = ["help", "accident", "fire", "ambulance", "danger", "police", "emergency"]

    for word in emergency_keywords:
        if word in msg:
            return "🚨 HIGH PRIORITY: Immediate attention required!"

    return "✅ LOW PRIORITY: No immediate danger detected."


print("=== Emergency Triage AI ===")

while True:
    user_input = input("\nEnter message (or type 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("Exiting...")
        break

    result = analyze_message(user_input)
    print("Result:", result)