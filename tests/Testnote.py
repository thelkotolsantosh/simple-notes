"""Test notes"""

import pytest
from app.note import Note


def test_create():
    note = Note("Title", "Text")
    assert note.title == "Title"
    assert note.text == "Text"


def test_to_dict():
    note = Note("A", "B")
    d = note.to_dict()
    assert d['title'] == "A"


def test_from_dict():
    data = {'id': '123', 'title': 'A', 'text': 'B', 'date': '2024-01-01'}
    note = Note.from_dict(data)
    assert note.id == '123'


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
