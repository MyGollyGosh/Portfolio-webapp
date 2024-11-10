-- Reset the database to ensure a fresh state by deleting tables and sequences
DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS tasks_id_seq;
DROP SEQUENCE IF EXISTS users_id_seq;

-- Recreate the users table with an auto-incrementing primary key
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL
);

-- Recreate the tasks table with foreign key referencing users
CREATE SEQUENCE IF NOT EXISTS tasks_id_seq;
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    description TEXT NOT NULL,
    due_date DATE NOT NULL,
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    priority INT DEFAULT 1 CHECK (priority BETWEEN 1 AND 5),
    status TEXT DEFAULT 'pending',
    CONSTRAINT fk_user FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE
);

-- Seed data for users
INSERT INTO users (username, email, password_hash) VALUES
    ('johndoe', 'johndoe@example.com', 'hashedpassword1'),
    ('janedoe', 'janedoe@example.com', 'hashedpassword2');

-- Seed data for tasks
INSERT INTO tasks (user_id, description, due_date, date_added, priority, status) VALUES
    (1, 'Complete Flask web app project', '2024-11-15', CURRENT_TIMESTAMP, 3, 'pending'),
    (1, 'Prepare presentation for project', '2024-11-10', CURRENT_TIMESTAMP, 2, 'in-progress'),
    (2, 'Review portfolio projects', '2024-11-20', CURRENT_TIMESTAMP, 1, 'pending'),
    (2, 'Update resume', '2024-11-12', CURRENT_TIMESTAMP, 3, 'completed');
