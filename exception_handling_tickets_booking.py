#Custom Exception Classes

class BookingError(Exception):
    """Base class for all exception related to ticket booking."""
    pass

class InvalidTicketCountError(BookingError):
    def __init__(self, message="Invalid ticket count"):
        self.message = message
        super().__init__(self.message)

class SeatsNotAvailableError(BookingError):
    def __init__(self, message="Requested seats not available"):
        self.message = message
        super().__init__(self.message)

class BookingLimitExceededError(BookingError):
    def __init__(self, message="Maximum booking limit exceeded"):
        self.message = message
        super().__init__(self.message)


def book_tickets(requested_tickets, available_seats, max_limit):
    if requested_tickets <= 0:
        raise InvalidTicketCountError()
    if requested_tickets > max_limit:
        raise BookingLimitExceededError()
    if requested_tickets > available_seats:
        raise SeatsNotAvailableError()
        
    remaining_seats = available_seats - requested_tickets
    print("Booking successful")
    print(f"Remaining seats : {remaining_seats}")


if __name__ == "__main__":
    total_available_seats = 50
    maximum_booking_limit = 10
    
    print(f"___show setup__")
    print(f"Available seats : {total_available_seats} | Max limit Booking :{maximum_booking_limit}\n")

    try:
        user_input = input("Enter the number of tickets to book : ")
        tickets_requested = int(user_input)
        book_tickets(tickets_requested, total_available_seats, maximum_booking_limit)
        
    except ValueError:
        print("please enter the numeric values only :")
    except (InvalidTicketCountError, SeatsNotAvailableError, BookingLimitExceededError) as e:
        print(e.message)   
    finally:
        print("Booking session ended")
