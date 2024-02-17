from generatemorse import MorseConverter


encoder = MorseConverter().encode
decoder = MorseConverter().decode

program = True

while program:
	direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
	text = input("Type your message:\n").upper()

	if direction == "encode":
		encoder(text)
	elif direction == "decode":
		decoder(text)

	restart = input("Do you want to continue using the program? (yes/no)\n").lower()
	if restart == "no":
		program = False
		print("Thank you for using the encoding/decoding program!")
