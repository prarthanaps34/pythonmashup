
frontend = {"Anu", "Rahul", "Meera", "Arun"}

backend = {"Rahul", "Meera", "Vishnu", "Asha"}

backend.add("Kiran")
frontend.remove("Arun")

both_courses = frontend & backend
print("Students enrolled in both courses:", both_courses)

backend_only = backend - frontend
print("Students enrolled only in Backend:", backend_only)

unique_students = frontend | backend
print("Total number of unique students:", len(unique_students))


course_counts = {
    "Frontend": len(frontend),
    "Backend": len(backend)
}


print("\nCourse-wise student count:")
for course, count in course_counts.items():
    print(course, ":", count)

course_counts_with_fullstack = {
    **course_counts,
    "Fullstack": len(frontend | backend)
}

print("\nCourse counts with Fullstack:", course_counts_with_fullstack)