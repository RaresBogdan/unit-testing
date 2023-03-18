import string


class StringExercises:

    # 1. Check if a string is a palindrome
    @staticmethod
    def is_str_palindrome(word):
        if not isinstance(word, str):
            raise TypeError("Input argument must be a string")

        if not word or not word.split():
            raise ValueError("Input string cannot be empty")

        clean_word = ''.join(char for char in word if char not in string.punctuation)
        clean_word = clean_word.replace(" ", "").lower()
        reversed_word = ''.join(reversed(clean_word))

        return clean_word == reversed_word

    # 2. Find the longest word in a sentence
    @staticmethod
    def longest_word(sentence):
        if not isinstance(sentence, str):
            raise TypeError("Input argument must be a string")

        if not sentence or not sentence.strip():
            raise ValueError("Input string cannot be empty")

        for punctuation in string.punctuation:
            sentence = sentence.replace(punctuation, "")

        clean_sentence = sentence.split()
        length_dict = {}

        for word in clean_sentence:
            length = len(word)
            if length in length_dict:
                length_dict[length].append(word)
            else:
                length_dict[length] = [word]

        if not length_dict:
            raise ValueError("Sentence must be formed out of words, not punctuation marks")

        longest_length = max(length_dict.keys())
        longest_words = length_dict[longest_length]

        if len(longest_words) == 1:
            return longest_words[0]
        return f"There are multiple same length words: {', '.join(longest_words)}"

    # 3. Reverse a string
    @staticmethod
    def reverse_string(word):
        if not isinstance(word, str):
            raise TypeError("Input argument must be a string")

        if not word or not word.strip():
            raise ValueError("Input string cannot be empty")

        reversed_string = ""

        for i in word:
            reversed_string = i.lower() + reversed_string

        return reversed_string

    # 4.  Find the largest number in a list
    @staticmethod
    def largest_number(number_list):
        if not number_list:
            raise ValueError("Input list cannot be empty")

        if not isinstance(number_list, list):
            raise TypeError("Input must be a list")

        for item in number_list:
            if not isinstance(item, (int, float)):
                raise TypeError("Input list must contain integer or float values")

        return max(number_list)

    # 5.  Find the smallest number in a list
    @staticmethod
    def smallest_number(number_list):
        if not number_list:
            raise ValueError("Input list cannot be empty")

        if not isinstance(number_list, list):
            raise TypeError("Input must be a list containing integers or float values")

        for item in number_list:
            if not isinstance(item, (int, float)):
                raise TypeError("Input list must contain integer or float values")

        return min(number_list)

    # 6. Find the most common word in a phrase
    @staticmethod
    def common_word(phrase):
        if not isinstance(phrase, str):
            raise TypeError("Input argument must be a string")

        if not phrase or not phrase.split():
            raise ValueError("Input string cannot be empty")

        for punctuation in string.punctuation:
            phrase = phrase.replace(punctuation, "")

        words = phrase.split()
        lowercase_words = []
        for word in words:
            lowercase_words.append(word.lower())

        freq = {}
        for word in lowercase_words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1

        if not freq:
            raise ValueError("Sentence must be formed out of words, not punctuation marks")

        max_freq = max(freq.values())
        common_words = [word for word, freq in freq.items() if freq == max_freq]

        if len(common_words) == len(freq):
            return "All the words in the string have the same frequency"

        if len(common_words) == 1:
            return common_words[0]

        return f"There are multiple most common words: {', '.join(common_words)}"

    # 7.  Find the most frequent letter in a string
    @staticmethod
    def most_frequent_letter(word):
        if not isinstance(word, str):
            raise TypeError("Input must be a string")

        if not word or not word.split():
            raise TypeError("Input string cannot be empty")

        for punctuation in string.punctuation:
            word = word.replace(punctuation, "")

        lowercase_word = word.strip().lower()
        letter_dic = {}

        for letter in lowercase_word:
            if letter in letter_dic:
                letter_dic[letter] += 1
            else:
                letter_dic[letter] = 1

        max_freq = max(letter_dic.values())
        frequent_letters = [letter for letter, freq in letter_dic.items() if freq == max_freq]

        if len(frequent_letters) == 1:
            return f"The most frequent letter is {frequent_letters[0]}"
        else:
            return f"There are multiple most frequent letters: {', '.join(frequent_letters)}"

