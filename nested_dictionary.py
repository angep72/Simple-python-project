name = input ("What is your name? ")
age = input ("How old are you? ")
Score = input ("how much do you have for you? ")
math = input ("How much do you have for you? ")
physics = input ("How much do you have for you? ")
chemistry = input ("How much do you have for you? ")

result = {
    name: name,
    age: age,
    Score: {
        "math": math,
        "physics": physics,
        "chemistry": chemistry
    }
}
print(result)