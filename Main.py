class Node:
    def __init__(self, data=None):
        self.data = data
        self.previous = self
        self.next = self


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def add_at_tail(self, data) -> bool:
        temp=Node()
        temp.data = data
        temp.prev = head.prev
        temp.next = head

    def add_at_head(self, data) -> bool:
        temp=Node()
        temp.data = data
        temp.prev = head.prev
        temp.next = head
      
    def add_at_index(self, index, data) -> bool:
        temp=Node()
        temp.next=index
        temp.prev=index.prev
        temp.prev.next=temp
        index.prev=temp

    def get(self, index) -> int:
        temp=Node()
        temp.self.head
        count=0
        i=0
        if(temp != None):
            while (True):
                i += 1
                if(temp.data == index):
                    count += 1
                    break
                temp = temp.next
                if(temp == self.head):
                    break
            if(count == 1):
                print(index,"is found at index =", i)
            else:
                print(index,"is not found in the list.")
         else:
            print("The list is empty.")

    def delete_at_index(self, index) -> bool:
        temp=Node()
        index.prev=index.next
        index.prev=None
        index.next=None

    def get_previous_next(self, index) -> list:
        temp=Node()
        temp.self.head
        count=0
        i=0
        if(temp != None):
            while (True):
                i += 1
                if(temp.data == index):
                    count += 1
                    break
                temp = temp.next
                if(temp == self.head):
                    break
            if(count==1):
                temp.prev=i-1
                temp.next=i+1
        
# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = []
iteration_count = 0

for item in input_data.split(', '):
    inner_list = []
    if item.isnumeric():
        data.append(int(item))
    elif item.startswith('['):
        item = item[1:-1]
        for letter in item.split(','):
            if letter.isnumeric():
                inner_list.append(int(letter))
        data.append(inner_list)

obj = DoublyCircularLinkedList()
result = []
for i in range(len(operations)):
    if operations[i] == "add_at_head":
        result.append(obj.add_at_head(data[i]))
    elif operations[i] == "add_at_tail":
        result.append(obj.add_at_tail(data[i]))
    elif operations[i] == "add_at_index":
        result.append(obj.add_at_index(int(data[i][0]), data[i][1]))
    elif operations[i] == "get":
        result.append(obj.get(data[i]))
    elif operations[i] == "get_previous_next":
        result.append(obj.get_previous_next(data[i]))
    elif operations[i] == 'delete_at_index':
        result.append(obj.delete_at_index(data[i]))

print(result)
