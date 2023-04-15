DROP TABLE IF EXISTS notes;
DROP TABLE IF EXISTS Notes;

CREATE TABLE Notes (
  id SERIAL PRIMARY KEY,
  created_at timestamp not null default CURRENT_TIMESTAMP,
  updated_at timestamp not null default CURRENT_TIMESTAMP,
  title VARCHAR(255) NOT NULL,
  notes TEXT NOT NULL,
  is_priority BOOLEAN DEFAULT FALSE,
  due_date DATE
);