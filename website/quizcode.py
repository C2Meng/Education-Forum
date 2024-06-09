import random
import string

class QuizCodeGenerator:
    def __init__(self, length=6):
        self.length = length
        self.generated_codes = set()

    def generate_code(self):
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=self.length))
        while code in self.generated_codes:
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=self.length))
        self.generated_codes.add(code)
        return code

    def verify_code(self, code):
        return code in self.generated_codes

# Example usage
if __name__ == "__main__":
    generator = QuizCodeGenerator()

    # Generate 10 unique codes
    for _ in range(10):
        print(generator.generate_code())

    # Verify a code
    test_code = "ABC123"
    print(f"Is {test_code} a valid code? {generator.verify_code(test_code)}")
