from werkzeug.security import generate_password_hash

# Generate hashed versions of our test passwords
password1 = generate_password_hash('Password!1')
password2 = generate_password_hash('Password!2')

# Print the INSERT statement with hashed passwords
print(f"""
INSERT INTO users (username, email, password_hash) VALUES
    ('johndoe', 'johndoe@example.com', '{password1}'),
    ('janedoe', 'janedoe@example.com', '{password2}');
""")