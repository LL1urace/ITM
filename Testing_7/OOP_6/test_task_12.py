import pytest
from OOP_6.task_12 import (Parent,
                           ChildUsingParentInit,
                           ChildUsingSuper,
                           D,
                           BX,
                           CX,
                           DX,
                           Tokenizer,
                           WordCounter,
                           Vocabulary,
                           TextDescriber,
                           get_text_describer_data)



def test_parent_and_child_attributes():
    p = Parent()
    assert p.parent_attribute == "I am a parent"
    assert Parent.parent_method() == "Back in my day"

    c1 = ChildUsingParentInit()
    assert c1.parent_attribute == "I am a parent"
    assert c1.child_attribute == "I am a child"

    c2 = ChildUsingSuper()
    assert c2.parent_attribute == "I am a parent"
    assert c2.child_attribute == "I am a child"

def test_multiple_inheritance_methods():
    d = D()
    assert d.b() == "b"
    assert d.c() == "c"
    assert d.d() == "d"

def test_mro_method_resolution_order():
    dx = DX()
    # Метод x() берётся из BX, так как BX стоит первым в списке родителей
    assert dx.x() == "x: B"
    # Проверяем MRO у DX
    assert DX.__mro__ == (DX, BX, CX, object)

def test_text_describer_combined_behavior():
    text = "hello world hello"
    td = TextDescriber(text)

    # Проверяем, что токены корректно разбиты
    assert td.tokens == ["hello", "world", "hello"]

    # Проверяем уникальные слова (set)
    assert td.vocab == {"hello", "world"}

    # Проверяем подсчет слов
    assert td.word_count == 3

    # Проверяем, что MRO корректно показывает цепочку наследования
    expected_mro = (TextDescriber, WordCounter, Vocabulary, Tokenizer, object)
    assert td.__class__.__mro__ == expected_mro

def test_get_text_describer_data_function():
    text = "foo bar foo baz"
    data = get_text_describer_data(text)
    assert data["tokens"] == ["foo", "bar", "foo", "baz"]
    assert data["vocab"] == {"foo", "bar", "baz"}
    assert data["word_count"] == 4
    assert data["mro"] == (TextDescriber, WordCounter, Vocabulary, Tokenizer, object)