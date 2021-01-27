from datetime import date, time, timedelta

"""
Bookings store appointments (date_objects) with 
Doctors have Bookings. 
Doctor have Patients.
User is an abstract class that both Doctor and Patient extend using composition

    Bookings > User(Doctor) > Patients

    USERS:
    =====
    Abstract class which is used for authentication
        * Has one to one field with doctor
        * Has one to one field with patient

        - id: int (used internally only)
        - key: uuid (external only as pk for security reasons)
        - username: str
        - fullname: str
        - email: str
        - password: hashkey
        --------
        Methods:
        --------
        
        Not Implemented:
        ================
            * update_account(): username, password, fullname, email
            * delete_account(): disable account instead for rollback purpose
            * generate_auth_token()

        Implemeted:
        ===========
            * generate_uuid()
            * save(): stores object to database
            

    BOOKINGS:
    =========
        - id: (internal only)
        - uuid: (external only as pk for security reasons)
        - doctor_obj___has_patients
        - datetime_obj
        
        --------
        Methods:
        --------
        * generate_uuid()
        * save(): stores object to database


    DOCTORS:
    =======
        - user: user_obj
        - specialist_in: [choice_field]
        - availability_periods: [datetime lists]
        - availability_status: [boolean_field]

        --------
        Methods:
        --------
        * Doctors can set their availability period => available_from(start_date, end_date)
        * Doctors can change their availability period => toggle_availability()
        * Doctors can clear their availability period => clear_availabilty(): clear availability
        * Doctors can clear their bookings => cancle_bookings(): deletes all Bookings for this doctor

        * Doctors expose a book(datetime_object) interface that patients can use to create Bookings:
            FAILS:
                If "datetime_obj" doesn't exists in Doctor's availability period OR
                If Doctor's availability status is False 
            PASSES:
                If __NOT__ both constraints exists.
        
        -------------
        Relationship:
        -------------
        * One Doctor can have many Patients +> ForeignKey relationship with Patients
        * One Doctor can have many Bookings +> ForeignKey relationship with Bookings


    PATIENTS:
    =========
        - user: user_obj
        - fullname: str

        --------
        Methods:
        --------
        * Patients can cancel their appointment with their Doctor: cancel_appointment()
            This action removes the patient's appointment from the doctor's bookings.

"""

class BookingException(Exception): pass
class BookingDoesNotExistError(BookingException): pass



class Bookings:
    """
    Stores appointments - which contains a Doctor object and date
    """
    def __init__(self):
        self.store = {}

    def get_appointments(self):
        """
        Returns appointments for doctors or patients
        """
        for appointment in self.store:
            pass


class Doctor:
    """
    A doctor object
    """
    def __init__(self, user, bookings):
        self.user = user
        self.bookings = bookings
        self.available_periods = []
        self.availability_status = True

    def set_available_period(self, start_date, end_date):
        delta = start_date - end_date
        for i in range(delta.days + 1):
            day = start_date + timedelta(days=i)
            self.available_periods.append(day)

    def get_available_periods(self):
        if self.available_periods:
            print(f"You are available from {} - {}".format(
                self.available_periods[0].strftime("%Y-%m-%d"),
                self.available_periods[-1].strftime("%Y-%m-%d"),
            ))

    def change_availability_status(self):
        self.availability_status = not self.availability_status
        return self.availability_status

    def cancle_bookings(self, booking_id=None):
        if booking_id:
            if self.bookings.store.get(booking_id):
                del self.bookings.store[booking_id]
            else:
                raise BookingDoesNotExistError
        else:
            for booking in self.bookings.store.values():
                if booking.doctor:
                    del booking
        
    def reset_avaliability_period(self):
        del self.available_periods

    def book_appointments(self, date_time_obj):
        if not self.availability_status and date_time_obj not in self.available_periods:
            return "Doctor is not available this period!"
        else:
            self.bookings.store.(self)
            return "Appointment Booked"



class Patient:
    """
    a. Patients have appointments
    """

    def __init__(self, user: str):
        self.name = name

    def set_appointment(self, date):
        pass

        
        
        


        