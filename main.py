import capture_window
import info_finder


def main():
    dimensions, image = capture_window.get_mswug_window()
    letter_box = capture_window.get_letter_box(image)
    # words_box = capture_window.get_words_box(image)
    letters = info_finder.find_letters(letter_box)


if __name__ == '__main__':
    main()
