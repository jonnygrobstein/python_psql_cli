# Note Taking Application README

This is a Python-based note taking application that uses the PostgreSQL database to store and retrieve notes. The application provides users with the ability to add, edit, list and search notes.

## Prerequisites

- Python 3.x
- PostgreSQL

## Getting started

1. Clone the repository or download the source code.
2. Create a PostgreSQL database with the name "notes" and set the necessary credentials for database connection in the code.
3. Install the required dependencies from requirements.txt.
4. Run the application from the command line with `python main.py` or `python3 main.py`.

## Usage

### Adding a Note

1. Enter '1' on the main menu to add a note.
2. Enter the note title, content, and if it is a priority or not.
3. The note will be added to the database.

### Editing a Note

1. Enter '2' on the main menu to edit a note.
2. Select the note to be edited by its ID.
3. Enter the updated title, content, and priority. If you do not want to change any of these, just press enter.
4. The note will be updated in the database.

### Listing All Notes

1. Enter '3' on the main menu to list all the notes.
2. All the notes available in the database will be listed with their ID and title.

### Searching Notes

1. Enter '4' on the main menu to search for a note.
2. Enter the search query.
3. All the notes that contain the search query will be listed with their ID and title.

### Quitting the Application

1. Enter '5' on the main menu to quit the application.
