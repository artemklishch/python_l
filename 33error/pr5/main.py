def image_info(dict):
    if not dict.get('image_id'):
        raise TypeError("Dictionary does not have id")
    if not dict.get('image_title'):
        raise TypeError("Dictionary does not have title")
    return f"Image '{dict['image_title']}' has id {5136}"


try:
    image_info({'image_id': '123', 'image_title': 'My title'})
except Exception as e:
    print(e)

try:
    print(image_info({'image_id': '123'}))
except Exception as e:
    print(e)

