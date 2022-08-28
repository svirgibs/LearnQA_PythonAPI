

class TestPhrase:
    def test_short_phrase(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, f"Phrase length greater than 15 characters. Phrase: {phrase}"
