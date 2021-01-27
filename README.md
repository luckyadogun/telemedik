
PROJECT
=======
Telemedik is an app that allows Patients book appointments with their Doctors

DATA FLOW
===============
Bookings store appointments (date_objects) with 
Doctors have Bookings. 
Doctor have Patients.
User is an abstract class that both Doctor and Patient extend using composition

Bookings > User(Doctor) > Patients


OBJECTS:
========

USERS:
-----
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
---------
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
--------
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
---------
    - user: user_obj
    - fullname: str

    --------
    Methods:
    --------
    * Patients can cancel their appointment with their Doctor: cancel_appointment()
        This action removes the patient's appointment from the doctor's bookings.