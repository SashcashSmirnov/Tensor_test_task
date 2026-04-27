class TensorPage():

    def assert_images_equal_size(test, selector, count=4):
        imgs = test.find_elements(selector)[:count]
        sizes = [(test.execute_script("return arguments[0].width", img), test.execute_script("return arguments[0].height", img)) for img in imgs]
        assert all(s == sizes[0] for s in sizes), f"Размеры: {sizes}"


