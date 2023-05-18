# Devenir
### Description
This project should facilitate preparation for consulting case interviews by allowing users to track their historical performance on cases. A leader of a prep group should also be able to leverage analytics to target individual and group casing weaknesses in addition to assisting in identifying top candidates.
### Utility
##### User utility
 - Offers ability to track cases online
 - Offers ability to understand weaknesses
 - Ability to be recognized for group leadership
 - Ability to be referred to recruiters
##### Group utility
 - Ability to conduct skills audit
 - Ability to accurately grade case difficulty
 - Ability to forecast top candidates
### Key Requirements
##### High Priority
Users should be able to:
 - Mark a case as completed as an interviewee
 - Record key components as an interviewee such as:
    1. Case name
    2. Case author (b-school)
    3. Case year
    4. Interviewer
    5. Date of casing
    6. Perceived Performance
    7. Perceived Difficulty
    8. Notes
    9. Time taken
 - Be able to grade others as a mock interviewer

Admins should be able to:
 - Add cases to the case database
##### Low Priority
Admins should be able to:
 - View all data
 - View analytics dashboard
### Models
##### User
 - First name
 - Last name
 - Email
 - Password (?)
 - Total cases
 - Total casing time
 - Average grade
 - Admin boolean

##### Case
 - Case name
 - Case book
 - Case year
 - Case tested skills
 - Case average grade
 - Case average perceived difficulty
 - Case frequency

##### Interview
 - Interviewee
 - Interviewer
 - Date
 - Case
 - Interviewee perceived difficulty
 - Interviewee perceived performance
 - Graded performance
    - Structure
    - Math
    - Etc.
 - Duration
 - Interviewee notes
 - Interviewer notes

##### Case book (?)
 - List of cases
 - Number of cases
 - Frequency