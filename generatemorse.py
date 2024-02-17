morse_dict = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': "...--",
    '4': "....-",
    '5': ".....",
    '6': "-....",
    '7': "--...",
    '8': "---..",
    '9': "----.",
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...',
    '"': '.-..-.',
    '$': '...-..-',
    '+': '.-.-.',
    '=': '-...-',
}


class MorseConverter:

    def encode(self, text):
        morse_code = ""
        for char in text:
            if char in morse_dict:
                morse_code += morse_dict[char] + " "
            else:
                morse_code += char
        print(f"morse code: {morse_code}")

    def decode(self, morse):
        text = ""
        for morse_code in morse.split():
            for key, value in morse_dict.items():
                if value == morse_code:
                    text += key
        print(f"decoded message: {text}")
