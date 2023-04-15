DROP TABLE IF EXISTS notes;

CREATE TABLE notes (
  id SERIAL PRIMARY KEY,
  created_at timestamp not null default CURRENT_TIMESTAMP,
  updated_at timestamp not null default CURRENT_TIMESTAMP,
  title VARCHAR(255) NOT NULL,
  notes TEXT NOT NULL,
  is_priority BOOLEAN DEFAULT FALSE,
  due_date DATE
);