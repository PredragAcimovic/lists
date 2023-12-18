#2nd assingment (list)
invitation = []
invitation.append('Nikola Tesla')
invitation.append('Stephen Hawking')
invitation.append('Isaac Newton')
print(f"Dear, {invitation[0].title()}, I would like you to come to dinner with me.")
print(f"\nDear, {invitation[1].title()}, I would like you to come to dinner with me.")
print(f"\nDear, {invitation[2].title()}, I would like you to come to dinner with me.")

cant_come = invitation.pop(1)
print(f"\n{cant_come.title()}, is not able to come to diner.")

invitation.insert(1, 'Elon Musk')

print(f"Dear, {invitation[0].title()}, I would like you to come to dinner with me.")
print(f"\nDear, {invitation[1].title()}, I would like you to come to dinner with me.")
print(f"\nDear, {invitation[2].title()}, I would like you to come to dinner with me.")

print(f"\nMy dear guest's, {invitation[0].title()}, {invitation[1].title()} and {invitation[2].title()}, we will have more guest to come.")
invitation.insert(0, 'Steve Jobs')
invitation.insert(2, 'Michael Jordan')
invitation.append('Ronaldinho')

print(f"Dear, {invitation[0].title()}, I would like you to come to dinner with me.")
print(f"\nDear, {invitation[1].title()}, I would like you to come to dinner with me.")
print(f"\nDear, {invitation[2].title()}, I would like you to come to dinner with me.")
print(f"\nDear, {invitation[3].title()}, I would like you to come to dinner with me.")
print(f"\nDear, {invitation[4].title()}, I would like you to come to dinner with me.")
print(f"\nDear, {invitation[5].title()}, I would like you to come to dinner with me.")


print(f"\nMy dear guest's, I have to infom you that i can invite only two of you.")
invitation_pop1 = invitation.pop(0)
print(f"\nDear, {invitation_pop1.title()}, I have to infom you that you can't come.")
invitation_pop2 = invitation.pop(1)
print(f"\nDear, {invitation_pop2.title()}, I have to infom you that you can't come.")
invitation_pop3 = invitation.pop(2)
print(f"\nDear, {invitation_pop3.title()}, I have to infom you that you can't come.")
invitation_pop4 = invitation.pop(2)
print(f"\nDear, {invitation_pop4.title()}, I have to infom you that you can't come.")

print(f"\nMy friend, {invitation[0].title()} you are still invited to diner.")
print(f"\nMy friend, {invitation[1].title()} you are still invited to diner.")

del invitation[0]
del invitation[0]
print(invitation)