import pytest

from main import BooksCollector

class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize("name, expected_result", [
        ("И", True),
        ("", False),  # некорректное имя
        ("Удивительное путешествие Нильса Хольгерссона", False)
    ])
    def test_add_new_book_boundary_values(self, name, expected_result):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert (name in collector.get_books_genre()) == expected_result

    def test_add_new_book_same_book_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Лолита')
        collector.add_new_book('Лолита')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_for_added_book(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_book_genre("Оно") == "Ужасы"

    def test_get_book_genre_not_added_book_none_result(self):
        collector = BooksCollector()
        assert collector.get_book_genre("Ася") is None

    def test_get_books_with_specific_genre_with_horror_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Сияние")
        collector.set_book_genre("Сияние", "Ужасы")
        assert collector.get_books_with_specific_genre("Ужасы") == ["Сияние"]

    def test_get_books_genre_add_to_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book("Коты-воители")
        collector.set_book_genre("Коты-воители", "Фантастика")
        assert collector.get_books_genre() == {"Коты-воители": "Фантастика"}

    def test_get_books_for_children_none_children_books(self):
        collector = BooksCollector()
        collector.add_new_book("Керри")
        collector.set_book_genre("Керри", "Ужасы")
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_same_book_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Машенька')
        collector.add_book_in_favorites('Машенька')
        collector.add_book_in_favorites('Машенька')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Пнин')
        collector.add_book_in_favorites('Пнин')
        collector.delete_book_from_favorites('Пнин')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_add_not_favorite_book(self):
        collector = BooksCollector()
        collector.add_new_book('Бледный огонь')
        assert collector.get_list_of_favorites_books() == []
