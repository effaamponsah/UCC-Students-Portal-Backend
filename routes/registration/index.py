from flask import Flask, request, jsonify
import pymysql


def _register():
    if request.method == "GET":
        # Do a query from the database and make a logic here to see if the date has not passed.
        # If it has passed, tell user registration is past
        # if there are no dates in db
        courses = [
            {
                "code": "CSC101",
                "title": "Introduction to computing",
                "credithours": 3,
                "compulsory": True,
            },
            {
                "code": "MAT101",
                "title": "Algebra and Trigonometry",
                "credithours": 3,
                "compulsory": True,
            },
            {
                "code": "PHY101",
                "title": "Introduction Physics",
                "credithours": 3,
                "compulsory": True,
            },
            {
                "code": "ASP199",
                "title": "Africa in a Unipolar world",
                "credithours": 2,
                "compulsory": False,
            },
            {
                "code": "ASP100",
                "title": "Africa In Dispersion",
                "credithours": 1,
                "compulsory": False,
            },
        ]

        total = []
        for i in courses:
            if i["compulsory"] == True:
                total.append(i["credithours"])
        return jsonify(
            Success=True,
            Semester="1st Semester 2018",
            Message="Courses for the semester open for registration will be here",
            Period="January 08, 2019 - Febuary 31, 2019",
            Courses=courses,
            Total=sum(total),
            Maximum=10,
        )

    if request.method == "POST":
        body = request.get_json()
        # I will then do what ever it is i want to do using these codes
        for i in body["courseCodes"]:
            print(i)
        return jsonify(Success=True, Message="Registration succcessful")

