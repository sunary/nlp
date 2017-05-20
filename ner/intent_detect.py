__author__ = 'sunary'


import string
from datetime import datetime
import sklearn_crfsuite


NOW = datetime.now()


def train_crf(x_train, y_train):
    crf = sklearn_crfsuite.CRF(
        algorithm='lbfgs',
        c1=0.1,
        c2=0.1,
        max_iterations=100,
        all_possible_transitions=True
    )
    return crf.fit(x_train, y_train)


def fearture(sent, index=0):

    word = sent[index]

    return {
        'word': word,
        'is_first': index == 0,
        'is_last': index == len(sent) - 1,
        'is_capitalized': word[0].upper() == word[0],
        'is_second_capitalized': word[1].upper() == word[1] if len(word) > 1 else False,
        'word[:1]': word[:1],
        'word[:2]': word[:2],
        'word[:3]': word[:3],
        'word[:4]': word[:4],
        # 'word[:5]': word[:5],
        # 'word[:6]': word[:6],
        # 'word[:-6]': word[:-6],
        # 'word[-5:]': word[-5:],
        'word[-4:]': word[-4:],
        'word[-3:]': word[-3:],
        'word[-2:]': word[-2:],
        'word[-1:]': word[-1:],
        'word.is_lower': word.islower(),
        'word.is_upper': word.isupper(),
        'word.is_digit': word.isdigit(),
        'prev_word': '' if index == 0 else sent[index - 1],
        'next_word': '' if index == len(sent) - 1 else sent[index + 1],
        'has_hyphen': '-' in word,
        'has_space': '_' in word,
        'is_numeric': word.isdigit(),
        'is_punctuation': word in string.punctuation,
        'is_year': len(word) == 4 and word.isdigit() and NOW.year - 100 < int(word) < NOW.year + 10,
    }


def data_train():
    find_cars = ['tim xe', 'xem xe', 'xe', 'mua xe', 'chi tiet', 'thong tin']
    car_models = ['suzuki', 'madaz 3', 'toyota', 'kia morning', 'bmw']

    car_model_intent = 'B_CAR', 'I_CAR'
    find_car_intent = 'B_FIND', 'I_FIND'
    x_train = []
    y_train = []

    for fc in find_cars:
        _fc = fc
        fc = fc.split(' ')
        for cm in car_models:
            data = []
            lable = []

            sent = _fc + ' ' + cm
            index = 0

            cm = cm.split(' ')

            # find car
            data.append(fearture(sent, index))
            index += 1
            lable.append(find_car_intent[0])

            for _ in fc[1:]:
                data.append(fearture(sent, index))
                index += 1
                lable.append(find_car_intent[1])

            # car model
            data.append(fearture(sent, index))
            index += 1
            lable.append(car_model_intent[0])

            for _ in cm[1:]:
                data.append(fearture(sent, index))
                index += 1
                lable.append(car_model_intent[1])

            x_train.append(data)
            y_train.append(lable)

    return x_train, y_train


def data_test():
    text = 'xe toyota'
    data = []
    for i in range(len(text.split(' '))):
        data.append(fearture(text, i))

    return [data]


if __name__ == '__main__':
    x_train, y_train = data_train()
    crf_model = train_crf(x_train, y_train)
    print crf_model.predict(data_test())