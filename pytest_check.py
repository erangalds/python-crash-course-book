from name_function import get_formatted_name

def test_first_last_name():
    """Do namems like 'Janis Joplin' work"""
    formatted_name = get_formatted_name('janis', 'joplin')
    print(formatted_name)
    assert formatted_name == 'Janis Joplin'


test_first_last_name()