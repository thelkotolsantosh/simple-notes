"""Usage example"""
from app.note import Note
from app.storage import Storage


# Create notes
note1 = Note("Meeting", "Discuss project")
note2 = Note("Shopping", "Buy milk")

print("Created notes:")
print(f"  {note1.title}")
print(f"  {note2.title}")

# Save
storage = Storage('example.json')
storage.save([note1, note2])
print("\nSaved to example.json")

# Load
loaded = storage.load()
print("\nLoaded notes:")
for note in loaded:
    print(f"  {note.title}: {note.text}")

# Convert
print("\nAs dict:")
print(f"  {note1.to_dict()}")
