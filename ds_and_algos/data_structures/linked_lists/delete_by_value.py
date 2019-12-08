#Access head_node => list.get_head()
#Check if list is empty => list.is_empty()
#Delete at head => list.delete_at_head()
#Search for element => list.search()
#Node class  { int data ; Node next_element;}
def delete(lst, value):
  if lst.is_empty():
    return False

  node = lst.get_head()
  previous_node = None

  while node != None:
    if node.data == value:
      break
    previous_node = node
    node = node.next_element

  if not node:
    return False

  if node.next_element == None:
    previous_node.next = None
    return True

  elif node.next_element != None:
    node.data = node.next_element.data
    node.next_element = node.next_element.next_element
    return True