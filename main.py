import morse      
morse_translator = morse.MorseCodeTranslator()
morse_text = morse_translator.english_to_morse("coding time")
english_text = morse_translator.morse_to_english(morse_text) #??
print("morse =", morse_text) 
print("english = ", english_text)

print("수정")
print("수정")
print("수정")