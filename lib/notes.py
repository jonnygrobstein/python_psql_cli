import datetime
import psycopg2
from peewee import *

conn = psycopg2.connect(
    dbname='notes',
    host='localhost',
    port='5432'
)

DATABASE = PostgresqlDatabase(
    'notes',
    host='localhost',
    port='5432')

class BaseModel(Model):
    class Meta:
        database = DATABASE

class Note(BaseModel):
    title = CharField(max_length=255)
    notes = TextField()
    is_priority = BooleanField(default=False)
    
    def __str__(self):
        return f'{self.title}: {self.notes[:50]}'
    
    class Meta:
        db_table = 'notes'

DATABASE.create_tables([Note])

# function to add a note in the database
def add_note():
    title = input('Enter the note title: ')
    notes = input('Enter the note content: ')
    is_priority = input('Is this note a priority? (y/n): ').lower() == 'y'
    try:
        note = Note.create(title=title, notes=notes, is_priority=is_priority)
        print(f'New note created titled {title}.')
        conn.commit()
        # note.save()
    except IntegrityError:
        DATABASE.rollback()
        note = Note.get(title=title)
        print(f'Note with title {title} already exists in the database.')
    return note

# function to list the notes in the database and return them as a dictionary mapping the ID to the note object
def get_notes():
    notes = Note.select()
    if notes.count() > 0:
        note_dict = {}
        for note in notes:
            note.id_str = str(note.id) # convert the ID to a string and store it as an attribute of the note object
            note_dict[note.id_str] = note
            print(f'{note.id_str}: {note.title}')
        return note_dict
    else:
        print('No notes found in the database.')
        return None
    
# function to update a note in the database
def update_note(note_dict):
    notes = get_notes()
    if notes:
        selection = input('Enter the number of the note you want to edit: ')
        try:
            note = notes[selection] # search for a note with the given ID
        except KeyError:
            print('Note not found.')
            return
        title = input(f'Enter the updated title (press enter to keep current title "{note.title}"): ')
        notes = input(f'Enter the updated notes (press enter to keep current notes "{note.notes}"): ')
        is_priority = input(f'Is this note a priority? (y/n) (current priority: {note.is_priority}): ').lower() == 'y'
        
        try:
            if title:
                note.title = title
            if notes:
                note.notes = notes
            note.is_priority = is_priority
            note.save()
            print(f'Note with title "{note.title}" updated in the database.')
        except IntegrityError:
            print(f'Note with title "{title}" already exists in the database.')

# function to list the notes in the database
def list_notes():
    notes = Note.select()
    if notes.count() > 0:
        print(f'{notes.count()} notes found:')
        for note in notes:
            print(f'{note.id}: {note.title}')
    else:
        print('No notes found in the database.')


# function to search for a note in the database
def search_notes():
    query = input('Enter the search query: ')
    notes = Note.select().where(Note.notes.contains(query))
    if notes.count() > 0:
        print(f'{notes.count()} notes found:')
        for note in notes:
            print(f'{note.id}: {note.title}')
    else:
        print('No notes found matching the query.')

def main():
    with conn:
        if not DATABASE.is_closed():
            DATABASE.close()
        DATABASE.connect()
        while True:
            # show the main menu
            print('What would you like to do?')
            print('1. Add a note')
            print('2. Edit a note (by ID)')
            print('3. List all notes')
            print('4. Search notes')
            print('5. Quit')

            # get the user's choice
            choice = input('Enter the number of your choice: ')

            # handle the user's choice
            if choice == '1':
                # add a note
                add_note()
            elif choice == '2':
                # edit a note
                note_dict = get_notes()
                if note_dict:
                    note_id = input('Enter the ID of the note you want to edit: ')
                    if note_id in note_dict:
                        update_note(note_dict[note_id])
                    else:
                        print(f'Note with ID {note_id} not found.')
            elif choice == '3':
                # list all notes
                get_notes()
            elif choice == '4':
                # search notes
                search_notes()
            elif choice == '5':
                # quit the program
                print('Goodbye!')
                break
            else:
                print('Invalid choice. Please enter a number from 1 to 5.')

if not DATABASE.is_closed():
    DATABASE.close()

if __name__ == '__main__':
    main()