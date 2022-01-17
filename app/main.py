from entities.user import User

print("==============")
print("Sign in (S)")
print("Register (R)")
print("==============")

command = input(">>> ").strip().upper()

if command == 'R':
    User.register("data/users.txt")
