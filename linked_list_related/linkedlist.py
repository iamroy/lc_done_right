from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def is_empty_linked_list(self):
        if self.head is None:
            return True
        else:
            return False

    def insert_at_head(self, new_data):
        new_node = Node(new_data)

        if self.is_empty_linked_list():
            self.head = new_node
            return self.head

        new_node.next = self.head
        self.head = new_node

        return self.head

    def append_node(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        return

    def linked_list_length(self):
        length = 0
        if self.is_empty_linked_list():
            return 0

        next_node = self.get_head()

        while next_node is not None:
            length += 1
            next_node = next_node.next

        return length

    def print_linked_list(self):
        if self.is_empty_linked_list():
            print('List is empty')
            return

        temp = self.head
        while temp:
            print(temp.data, end="=>")
            temp = temp.next
        print("None")

    def delete_node_at_head(self):
        first_node = self.get_head()

        if first_node is not None:
            self.head = first_node.next
            first_node.next = None

        return

    def delete_node(self, data):
        deleted = False
        if self.is_empty_linked_list():
            print('List is empty')
            return deleted

        current_node = self.get_head()
        previous_node = None

        if current_node.data == data:
            self.delete_node_at_head()
            deleted = True
            return deleted

        while current_node is not None:
            if current_node.data == data:
                previous_node.next = current_node.next
                current_node.next = None
                deleted = True
                break

            previous_node = current_node
            current_node = current_node.next

        return deleted


    def search_node(self, data):
        if self.is_empty_linked_list():
            print('List is empty')
            return None

        temp_node = self.get_head()

        while temp_node is not None:
            if temp_node.data == data:
                return temp_node

            temp_node = temp_node.next

        print(data, ' is not in the list')
        return None


    def remove_duplicate_nodes(self):

        if self.is_empty_linked_list():
            return

        if self.get_head().next is None:
            return

        next_node = self.get_head()

        node_dict = dict()
        previous = None

        while next_node:

            if str(next_node.data) in node_dict.keys():
                print(str(next_node.data))
                previous.next = next_node.next
                next_node = next_node.next
                continue
            else:
                node_dict[str(next_node.data)] = 1

            previous = next_node
            next_node = next_node.next