from typing import List

import pymongo


def get_inputs() -> List[str]:
    with open('Puzzle_1/puzzle-inputs.txt', 'r') as f:
        return f.read().split('\n')


def get_collection():
    return pymongo.MongoClient(
        'mongodb://localhost:27017/advent_of_code'
    ).db.day_1


def insert_to_mongo(inputs: List[str]):
    collection = get_collection()
    collection.remove()
    collection.insert_many([dict(input=int(p_input)) for p_input in inputs])


def puzzle_two():
    collection = get_collection()
    cursor = collection.aggregate([
        {'$lookup': {
            'from': collection.name,
            'as': 'input_2',
            'let': {'id': '$_id'},
            'pipeline': [
                {'$match': {
                    '$expr': {'$gt': ['$$id', '$_id']}
                }},
                {'$lookup': {
                    'from': collection.name,
                    'as': 'input_3',
                    'let': {'id2': '$_id', 'input_2': '$input'},
                    'pipeline': [
                        {'$match': {
                            '$expr': {'$gt': ['$$id2', '$_id']}
                        }},
                        {'$unset': ['_id']},
                        {'$match': {
                            '$expr': {'$lte': [
                                {'$add': ['$input', '$$input_2']},
                                2020
                            ]},
                        }},
                    ]
                }},
                {'$unset': ['_id']},
                {'$unwind': '$input_3'},
            ]
        }},
        {'$unwind': '$input_2'},
        {'$project': {
            '_id': 0,
            'input_1': '$input',
            'input_2': '$input_2.input',
            'input_3': '$input_2.input_3.input',
        }},
        {'$match': {
            '$expr': {'$eq': [
                {'$add': ['$input_1', '$input_2', '$input_3']},
                2020
            ]}
        }},
        {'$project': {
            '_id': 0,
            'input_1': 1,
            'input_2': 1,
            'input_3': 1,
            'result': {'$multiply': ['$input_1', '$input_2', '$input_3']},
        }}
    ])

    results = list(cursor)
    for result in results:
        print(f'One solution to puzzle two is input {result["input_1"]}, {result["input_2"]} and {result["input_3"]} with result {result["result"]}')


def puzzle_one():
    collection = get_collection()
    cursor = collection.aggregate([
        {'$lookup': {
            'from': collection.name,
            'as': 'input_2',
            'let': {'id': '$_id'},
            'pipeline': [
                {'$match': {
                    '$expr': {'$gt': ['$$id', '$_id']}
                }},
                {'$unset': ['_id']},
            ]
        }},
        {'$unwind': '$input_2'},
        {'$match': {
            '$expr': {'$eq': [
                {'$add': ['$input_2.input', '$input']},
                2020
            ]}
        }},
        {'$project': {
            '_id': 0,
            'input_1': '$input',
            'input_2': '$input_2.input',
            'result': {'$multiply': ['$input', '$input_2.input']},
        }}
    ])

    results = list(cursor)
    for result in results:
        print(f'One solution to puzzle one is input {result["input_1"]} and {result["input_2"]} with result {result["result"]}')


def main():
    inputs = get_inputs()
    insert_to_mongo(inputs)

    puzzle_one()
    puzzle_two()


if __name__ == '__main__':
    main()
