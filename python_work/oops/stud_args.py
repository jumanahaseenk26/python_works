def display_student(**args):
    print(args.get("name"))
    print(args.get("course"))

display_student(name="jumana",course="django",roll=100,gender="female")