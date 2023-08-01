# Example of object oriented 




class Flight():
    def __init__(object, capacity):
        object.capacity = capacity
        object.passengers = []

    def add_passenger(object, name):
        if not object.open_seats():
            return False
        object.passengers.append(name)
        return True
    
    def open_seats(object):
        return object.capacity - len(object.passengers)


flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
   
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No availabl seats for {person}")
