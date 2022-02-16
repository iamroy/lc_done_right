#21. Merge Two Sorted Lists

import linkedlist as l

#21. Merge Two Sorted Lists
def merge_sorted_list(head_list1, head_list2):

    node1 = head_list1
    node2 = head_list2

    new_list = l.LinkedList()

    while node1 and node2:
        if node1.data>node2.data:
            new_list.append_node(node2.data)
            node2 = node2.next
        else:
            new_list.append_node(node1.data)
            node1 = node1.next

    if not node1:
        tmp = node2
    else:
        tmp = node1

    while tmp:
        new_list.append_node(tmp.data)
        tmp = tmp.next

    return new_list

if __name__ == '__main__':

    list1 = l.LinkedList()
    list1.append_node(1)
    list1.append_node(2)
    list1.append_node(4)

    list2 = l.LinkedList()
    list2.append_node(1)
    list2.append_node(3)
    list2.append_node(4)
    list2.append_node(5)

    merged_list = merge_sorted_list(list1.head, list2.head)

    list1.print_linked_list()
    list2.print_linked_list()
    merged_list.print_linked_list()