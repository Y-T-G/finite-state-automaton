# Course Pre-registration State Transition Testing - Code Implementation

**Name:** Yasin Mohammed  
**Matric No.:** 1814111  
**Section:** 1

## Explanation

To register courses for a semester, the students are required to make use of the pre-registration website. The process of course registration has a very defined flow which can be expressed in the form of state transition diagram. The following requirements need to be satisfied to successfully add/reserve a course:

1. Student has to be logged in.
2. Student has to enter the course code.
3. Student has to enter the section.
4. The course code entered should be valid.
5. The pre-requisite for the course need to be fulfilled.
6. The section needs be valid
7. The section needs to have at least one vacancy.
8. The addition of the course should not cause the student to exceed his maximum workload.

## State Transition Diagram

![enter image description here](https://i.postimg.cc/gcT8nhgz/Challenge-1.png)

## State Transition Table

| Condition                            |     |     |     |     |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Student logged in?                   | F   | T   | T   | T   | T   | T   | T   | T   | T   |
| Course code entered?                 | X   | F   | T   | T   | T   | T   | T   | T   | T   |
| Section no. entered?                 | X   | X   | F   | T   | T   | T   | T   | T   | T   |
| Course code valid?                   | X   | X   | X   | F   | T   | T   | T   | T   | T   |
| Pre-requisite met?                   | X   | X   | X   | X   | F   | T   | T   | T   | T   |
| Section valid?                       | X   | X   | X   | X   | X   | F   | T   | T   | T   |
| Section has vacancies?               | X   | X   | X   | X   | X   | X   | F   | T   | T   |
| Sufficient workload space available? | X   | X   | X   | X   | X   | X   | X   | F   | T   |
|<center>**Action**</center>                             |     |     |     |     |     |     |     |     |     |
| Accept                               |     |     |     |     |     |     |     |     | ✔️  |
| Reject                               | ✔️  | ✔️  | ✔️  | ✔️  | ✔️  | ✔️  | ✔️  | ✔️  |     |

## Code

The Python code in the `main.py` file implements the finite state automaton described above. It checks the given input across the four different states of the finite state automaton defined above.

The input is a `list` object with ordered elements describing [`Matric No., Password, Course Code, Section`]. To check the input, we call the `test` function with the input object as the argument. Two example inputs are present in the code.

The code in the `test` function first checks whether the input matric no. is valid by calling the `getUserProfile` function which returns a `dict` object if the profile is found and the password is correct. Otherwise, the function returns an `str` object holding the error message.

Next, the code calls the `getCourseInfo` function to check whether the provided course code is valid. If yes, then it proceeds to check if the provided section is valid for the provided course. If either of the aforementioned check fails, it returns an error.

Lastly, the code checks if the student has sufficient workload space to add the given course. If it finds that the addition of the credit hour of the given course would cause the student to exceed the maximum workload, the course addition process fails with an error message saying that the workload is exceeded.
