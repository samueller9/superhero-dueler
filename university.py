
# Campus
#     location
#     name
#     buildings
#     open_spaces
#     neighborhoods
#Building
    #name
    #purpose
#Neighborhood

#Schools
    #name
    #instructors
    #subject
#Staff
    #name
    #staff_id
    #started_on
#Instructor(Staff)
#Security
#President
#Professor
#Counselor
#Nurse
#Librarian
#Coach


#Student
    #name
    #majors
    #minors
    #year_count(int)

    #enroll(course)
    #withdraw(course)
    #join(club)
    #declare_major
    #declare_minor
    #change_major
#Athlete(Student)
    #sport

    #attend_practice
    #compete
    #travel
#Course
    #instructor
    #co_instructor
    #students
    #starts_at
    #ends_at()

#Club
    #name
    #faculty_advisor
