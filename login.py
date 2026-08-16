def login(username, password):
    if username == "james" and password == "python":
        return "Login successful"
    return "Login failed"


print(login("james", "python"))
