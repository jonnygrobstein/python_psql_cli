TRUNCATE TABLE notes;

ALTER SEQUENCE notes_id_seq restart with 1;

INSERT INTO notes(title, notes, is_priority, due_date) VALUES 
('Go Grocery Shopping', 'Pick up butter, steak, and kimchi', true, '2023-04-16'),
('Call Carrie', 'Reach out to Carrie regarding website dev project', FALSE, '2023-04-16'),
('Final Project Wireframe', 'Need to wireframe potential project layout and see if it is doable.', true, null),
('Date Night Ideas', 'Come up with 3 to 5 date options to do with wifey', FALSE, '2023-04-21');