# ============================================================
# PYTHON OOP EXERCISE: Phone Call History
# Topics: Classes, Objects, Methods, Lists, Dictionaries
# ============================================================

class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []
    
    def call(self, other_phone):
        """Make a call to another phone"""
        call_record = f"{self.phone_number} called {other_phone.phone_number}"
        print(call_record)
        self.call_history.append(call_record)
        other_phone.call_history.append(f"{self.phone_number} called {other_phone.phone_number} (incoming)")
    
    def show_call_history(self):
        """Display all calls"""
        print(f"\n📞 Call History for {self.phone_number}:")
        if self.call_history:
            for i, call in enumerate(self.call_history, 1):
                print(f"  {i}. {call}")
        else:
            print("  No calls yet.")
    
    def send_message(self, other_phone, content):
        """Send a message to another phone"""
        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(message)
        other_phone.messages.append({
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        })
        print(f"Message sent from {self.phone_number} to {other_phone.phone_number}")
    
    def show_outgoing_messages(self):
        """Show all messages sent from this phone"""
        print(f"\n📤 Outgoing Messages from {self.phone_number}:")
        outgoing = [m for m in self.messages if m["from"] == self.phone_number]
        if outgoing:
            for i, msg in enumerate(outgoing, 1):
                print(f"  {i}. To: {msg['to']} | Message: '{msg['content']}'")
        else:
            print("  No outgoing messages.")
    
    def show_incoming_messages(self):
        """Show all messages received by this phone"""
        print(f"\n📥 Incoming Messages to {self.phone_number}:")
        incoming = [m for m in self.messages if m["to"] == self.phone_number]
        if incoming:
            for i, msg in enumerate(incoming, 1):
                print(f"  {i}. From: {msg['from']} | Message: '{msg['content']}'")
        else:
            print("  No incoming messages.")
    
    def show_messages_from(self, sender_number):
        """Show messages from a specific number"""
        print(f"\n💬 Messages from {sender_number} to {self.phone_number}:")
        filtered = [m for m in self.messages if m["from"] == sender_number and m["to"] == self.phone_number]
        if filtered:
            for i, msg in enumerate(filtered, 1):
                print(f"  {i}. '{msg['content']}'")
        else:
            print(f"  No messages from {sender_number}.")


# ============================================================
# TESTING THE CODE
# ============================================================

print("=" * 60)
print("📱 PHONE CALL HISTORY - TESTING")
print("=" * 60)

# Create phone objects
phone1 = Phone("050-1234567")
phone2 = Phone("050-7654321")
phone3 = Phone("050-9998888")

print(f"\nCreated phones: {phone1.phone_number}, {phone2.phone_number}, {phone3.phone_number}")

# Test calls
print("\n--- Making Calls ---")
phone1.call(phone2)
phone2.call(phone1)
phone1.call(phone3)

# Show call histories
phone1.show_call_history()
phone2.show_call_history()
phone3.show_call_history()

# Test messages
print("\n--- Sending Messages ---")
phone1.send_message(phone2, "Hey, are we meeting today?")
phone2.send_message(phone1, "Yes, at 3 PM!")
phone1.send_message(phone2, "Great, see you then!")
phone3.send_message(phone1, "Hello! This is phone3.")

# Show messages
phone1.show_outgoing_messages()
phone1.show_incoming_messages()

phone2.show_outgoing_messages()
phone2.show_incoming_messages()

# Show messages from specific number
phone2.show_messages_from("050-1234567")

print("\n" + "=" * 60)
print("TESTING COMPLETED! ✅")
print("=" * 60)