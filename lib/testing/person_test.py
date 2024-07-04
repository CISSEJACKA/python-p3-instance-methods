from lib.person import Person

def test_person_talk():
    john = Person()
    assert john.talk() == "Hello World!"

def test_person_walk():
    john = Person()
    assert john.walk() == "The person is walking."

