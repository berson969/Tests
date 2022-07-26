documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "insurance", "number": "106", "name": "Аристарх Петров"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


# people name
def people(document_number):
    for document in documents:
        if document['number'] == document_number:
            doc_name = document['name']
            # print(f'Name of this document is {doc_name}')
            return doc_name
    # print('Wrong number of document')
    return None


# command shelf
def shelf(document_number):
    for key, values in directories.items():
        if document_number in values:
            # print(f'Document number {document_number} is on shelf number {key} ')
            return key
    # print(f'Document number {document_number} is not in the archive ')
    return None


# command for print list of all documents
def all_list():
    full_doc_list = []
    for document in documents:
        doc_list = list(document.values())
        full_doc_list.append(doc_list)
        # print(f'{doc_list[0]} "{doc_list[1]}" "{doc_list[2]}" ')
    return full_doc_list


def add_new(type, number, name, shelf_):
    for document in documents:
        if number == document['number']:
            return None
    documents.append({"type": type, "number": number, "name": name})
    if shelf_ in directories.keys():
        directories[shelf_].append(number)
        doc_on_shelf = directories[shelf_]
        # print('The document has been successfully entered into the database')
        # print(directories)
        return doc_on_shelf
    else:
        print('Wrong number of the shelf')
        return None


def delete_doc(doc_number):
    for document in documents:
        if doc_number in document['number']:
            documents.remove(document)
            deleted_name = document['name']
            # print(documents)
    for value in directories.values():
        if doc_number in value:
            value.remove(doc_number)
            # print(directories)
            # print(f'Document number {doc_number} was deleted from the database')
            return deleted_name
    # print('Wrong the number of doc')
    return None


def move_doc(doc_number, shelf_number):
    for document in documents:
        if doc_number in document['number']:
            if shelf_number in directories.keys():
                for key, values in directories.items():
                    if doc_number in values:
                        values.remove(doc_number)
                        directories[shelf_number].append(doc_number)
                        # print(directories)
                        # print(f'Document number {doc_number} remove to shelf number {shelf_number}')
                        return directories
            # print('Wrong number of shelf')
            return None
    # print('Document not found')
    return None


def add_shelf(new_shelf):
    if new_shelf not in directories.keys():
        directories[new_shelf] = []
        # print(directories)
        # print('New shelf was added')
        return directories
    else:
        # print('Wrong! This shelf already exists')
        return directories


def help_():
    print(
        f'List of commands:\n p - show personal name of the document \n'
        f' s - show number of the shelf, where is the document \n l - list of all documents \n'
        f' a - add new document to the shelf \n d - delete document from documents and shelf\n'
        f' m - move document to another shelf \n as -create new shelf \n q - exit')


# main command
def main():
    command_dict = {'p': people, 's': shelf, 'l': all_list, 'a': add_new,
                    'd': delete_doc, 'm': move_doc, 'as': add_shelf, 'h': help_}

    command = input('Input command ( for help push h): ').lower()
    if command in ('p', 's', 'l', 'd'):
        document_number = input('Input number of the document: ')
        command_dict[command](document_number)
        return command_dict[command]
    elif command == 'a':
        type_new = input('Input type of new document: ')
        number_new = input('Input number of new document: ')
        name_new = input('Input name from new document: ')
        shelf_new = input('Input number of the shelf: ')
        command_dict[command](type_new, number_new, name_new, shelf_new)
        return command_dict[command]
    elif command == 'as':  # as
        new_shelf = input('Input number of new shelf: ')
        command_dict[command](new_shelf)
        return command_dict[command]
    else:
        return command


if __name__ == '__main__':
    while True:
        if main() == 'q':
            break
