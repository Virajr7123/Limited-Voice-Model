import speech_recognition as sr

print("--- Finding all available microphones ---")

# This will list every microphone Python can see
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"Mic index {index}: {name}")

print("-----------------------------------------")
print("\nLook for your 'real' microphone in the list and remember its index number.")