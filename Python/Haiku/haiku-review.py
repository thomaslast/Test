class Haiku:
    def haiku_checker(self, haiku):
        self.haiku = haiku
        self.total_len = len(haiku)
        haiku = self.haiku.split(r"/")
        self.haiku_lines = len(haiku)
        self.validator()
        haiku_syl1 = self.syllable_checker(haiku[0])
        haiku_syl2 = self.syllable_checker(haiku[1])
        haiku_syl3 = self.syllable_checker(haiku[2])
        if haiku_syl1 == 5 and haiku_syl2 == 7 and haiku_syl3 == 5:
            haiku_state = "Yes"
        else:
            haiku_state = "No"
        return [haiku_syl1, haiku_syl2, haiku_syl3, haiku_state]
    
    def syllable_checker(self, string):
        vowels = ["a", "e", "i", "o", "u", "y"]
        syllables=0
        for i in range(0,len(string)):
            if i > 0:
                if string[i] in vowels and string[i-1] not in vowels: 
                    syllables += 1 
            elif i == 0:
                if string[i] in vowels:
                    syllables += 1 
        return syllables
          
    def validator(self):
        if type(self.haiku) != str:
            raise TypeError("Input is NOT a string")
        if self.total_len > 200:
            raise ValueError("Haiku is too long")
        elif self.total_len < 3:
            raise ValueError("Haiku is too short")
        if self.haiku_lines != 3:
            raise ValueError("Haiku is not the correct no of lines")
haiku = 1234
test = Haiku()
print(test.haiku_checker(haiku))