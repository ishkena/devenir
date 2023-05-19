# Devenir
### Description
This project should facilitate preparation for consulting case interviews by allowing users to track their historical performance on cases. A leader of a prep group should also be able to leverage analytics to target individual and group casing weaknesses in addition to assisting in identifying top candidates.
### Utility
##### User utility
 - Offers ability to track cases online
 - Offers ability to understand weaknesses
 - Ability to be recognized for group leadership
 - Ability to be referred to recruiters
 - Track service hours of interviewers
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
### 8 Models
##### Case
|case_id|INT|
|---|---|
|(FK) book_id|INT|
|name|VARCHAR(50)|
|industry|VARCHAR(50)|
|type|VARCHAR(50)|
|average_grade|DEC(2, 3)|
|average_confidence|DEC(2, 3)|
|frequency|INT|

##### Book
|book_id|INT|
|---|---|
|name|VARCHAR(50)|
|year|INT|
|case_count|INT|
|frequency|INT|
|average_grade|DEC(2, 3)|
|average_confidence|DEC(2, 3)|

##### CaseSkill
|case_skill_id|INT|
|---|---|
|(FK) case_id|INT|
|(FK) skill_id|INT|
|has_skill|BOOL|

##### Skill
|skill_id|INT|
|---|---|
|skill_name|VARCHAR(30)|

##### User
|user_id|INT|
|-----------|---|
|first_name|VARCHAR(30)|
|last_name|VARCHAR(30)|
|email|VARCHAR(50)|
|password|VARCHAR(50)|
|case_count|INT|
|interviewee_time|INT|
|interviewer_time|INT|
|average_grade|DEC(2, 3)|
|average_confidence|DEC(2, 3)|
|is_admin|BOOL|

##### Interview
|interview_id|INT|
|---|---|
|(FK) case_id|INT|
|date|DATETIME|
|grade|DEC(2, 3)|
|duration|INT|

##### Interviewer
|interviewer_id|INT|
|---|---|
|(FK) user_id|INT|
|(FK) interview_id|INT|
|interviewer_notes|VARCHAR(1000)|

##### Interviewee
|interviewee_id|INT|
|---|---|
|(FK) user_id|INT|
|(FK) interview_id|INT|
|difficulty|INT|
|confidence|INT|
|interviewee_notes|VARCHAR(1000)|