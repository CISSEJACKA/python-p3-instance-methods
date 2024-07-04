from lib.dog import Dog

def test_dog_bark():
    fido = Dog()
    assert fido.bark() == "Woof!"

def test_dog_sit():
    fido = Dog()
    assert fido.sit() == "The dog is sitting."


