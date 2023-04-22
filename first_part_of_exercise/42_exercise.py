
note = str(input("Enter the note :"))
octave = int(input("Enter the number of note : "))
frequency = 2**(4-octave)  # почему 2 ** (4-5) = 0.5 ?

if note == "C":
    frequency = 261.63 / frequency
elif note == "D":
    frequency = 293.66 / frequency
elif note == "E":
    frequency = 329.63 / frequency
elif note == "F":
    frequency = 349.23 / frequency
elif note == "G":
    frequency = 392.00 / frequency
elif note == "A":
    frequency = 440.00 / frequency
elif note == "B":
    frequency = 493.88 / frequency

print(f"The frequncy of note {note}{octave} is {frequency :.2f} Hz")
