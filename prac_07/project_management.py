"""Current time 3:54pm
Estimated time: 50 mins
End time: 8:15pm
"""

from datetime import datetime
from operator import attrgetter
from prac_07.project import Project


MENU = (
    "- (L)oad projects\n"
    "- (S)ave projects\n"
    "- (D)isplay projects\n"
    "- (F)ilter projects by date\n"
    "- (A)dd new project\n"
    "- (U)pdate project\n"
    "- (Q)uit"
)


def main():
    """Opens up a menu for project management"""
    print("Welcome to Pythonic Project Management")
    projects = load_projects("projects.txt")
    print(f"Loaded {len(projects)} projects from projects.txt")

    print(MENU)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "l":
            filename = input("Filename: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")

        elif choice == "s":
            filename = input("Save to: ")
            save_projects(filename, projects)
            print(f"Saved to {filename}")

        elif choice == "d":
            display_projects(projects)

        elif choice == "f":
            filter_projects(projects)

        elif choice == "a":
            add_project(projects)

        elif choice == "u":
            update_project(projects)

        else:
            print("Invalid choice")

        print(MENU)
        choice = input(">>> ").lower()

    # Quit
    save_prompt = input("Would you like to save to projects.txt? ")
    if save_prompt.lower().startswith("y"):
        save_projects("projects.txt", projects)
    print("Thank you for using custom-built project management software.")

def load_projects(filename):
    """loads projects from a text file"""
    projects = []
    try:
        with open(filename, "r") as file:
            next(file)  # Skip header line
            for line in file:
                name, date, priority, cost, completion = line.strip().split("\t")
                projects.append(Project(name, date, priority, cost, completion))
    except FileNotFoundError:
        print("File not found.")
    return projects

def save_projects(filename, projects):
    """saves project"""
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion\n")
        for p in projects:
            file.write(
                f"{p.name}\t{p.start_date.strftime('%d/%m/%Y')}\t"
                f"{p.priority}\t{p.cost_estimate:.2f}\t{p.completion}\n"
            )

def display_projects(projects):
    """displays projects and information"""
    incomplete = [p for p in projects if p.completion < 100]
    completed = [p for p in projects if p.completion == 100]

    incomplete.sort(key=attrgetter("priority"))
    completed.sort(key=attrgetter("priority"))

    print("Incomplete projects:")
    for p in incomplete:
        print(f"  {p}")

    print("Completed projects:")
    for p in completed:
        print(f"  {p}")

def filter_projects(projects):
    """filters projects by date"""
    date_string = input("Show projects that start after date (dd/mm/yy): ")

    # Allow 2-digit or 4-digit year
    day, month, year = date_string.split("/")
    if len(year) == 2:
        filter_date = datetime.strptime(date_string, "%d/%m/%y")
    else:
        filter_date = datetime.strptime(date_string, "%d/%m/%Y")

    filtered = [p for p in projects if p.start_date >= filter_date]
    filtered.sort(key=attrgetter("start_date"))

    for p in filtered:
        print(p)


def add_project(projects):
    """adds a new project"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yy): ")

    # Accept 2-digit or 4-digit year
    day, month, year = start_date_str.split("/")
    if len(year) == 2:
        start_date = datetime.strptime(start_date_str, "%d/%m/%y")
    else:
        start_date = datetime.strptime(start_date_str, "%d/%m/%Y")

    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))

    # FIX: pass datetime object, NOT the raw text string
    projects.append(Project(name, start_date, priority, cost, completion))


def update_project(projects):
    """updates a project"""
    for i, p in enumerate(projects):
        print(f"{i} {p}")

    index = int(input("Project choice: "))
    project = projects[index]

    print(project)

    new_percentage = input("New Percentage: ")
    if new_percentage.strip():
        project.completion = int(new_percentage)

    new_priority = input("New Priority: ")
    if new_priority.strip():
        project.priority = int(new_priority)


if __name__ == "__main__":
    main()
