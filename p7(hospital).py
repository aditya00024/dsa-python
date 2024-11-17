class Patient:
    def __init__(self,name,condition,disease):
        self.name=name
        self.condition=condition
        self.disease=disease
        self.next=None
class L:
    def __init__(self):
        self.head=None
    def add(self,name,condition,disease):
        new=Patient(name,condition,disease)
        if self.head is None:
            self.head=new
            print(f"{new.name.upper()} is added in the queue ")
        else:
            a=self.head
            if condition=="high":
                if self.head.condition!="high":
                    new.next=self.head
                    self.head=new
                    print(f"{new.name.upper()} is added in the queue ")
                else:
                    while a.next is not None and a.next.condition=="high":
                        a=a.next
                    new.next=a.next
                    a.next=new
                    print(f"{new.name.upper()} is added in the queue ")
            else:
                while a.next is not None:
                    a=a.next
                a.next=new
                print(f"{new.name.upper()} is added in the queue ")

    def remove(self,name):
        a=self.head
        found=False
        if self.head is None:
            return
        else:
            if self.head.name==name:
                found=True
                self.head=self.head.next
            else:
                while a is not None:
                    if a.next.name==name:
                        found=True
                        a.next=a.next.next
                        print(f"{name} is removed from Queue")
                    a=a.next
        if not found:
            print(f"{name } is not found in the queue :: ")
    def search(self,name):
        a=self.head
        found=True
        if self.head is None:
            return
        else:
            if self.head.name==name:
                print(f"{self.head.name} found in the queue with condition {a.condition}")
            else:
                while a is not None:
                    if a.next.name==name:
                        found=True
                        print(f"{a.name} found in the queue with condition {a.condition} ")
                    a=a.next
        if not found:
            print(f"{name } not found in the queue :: ")
    def moveup(self,name):
        found=False
        if self.head is None:
            return
        elif self.head.name==name:
            found=True
            print(f"{self.head.name} your already at first priority :: ")
        else:
            prev=self.head
            a=self.head.next
            while a is not None:
                if a.name==name:
                    found=True
                    if a.condition=="moderate" or a.condition=="low":
                        a.condition="high"
                        prev.next=a.next
                        self.add(a.name,a.condition,a.disease)            
                        return
                prev=prev.next
                a=a.next
        if not found:
            print(f"{name} is not found in the queue :: ")
    def display(self):
        if self.head is None:
            print("Queue is empty :: ")
            return
        else:
            a=self.head
            print("Name\tCondtion\tDisease")
            while a is not None:
                print(f"{a.name.upper()}\t{a.condition.upper()}\t{a.disease.upper()}")
                a=a.next
            
if __name__=="__main__":
    l=L()
    while True:
        c=int(input("Choose from the following ::\n1.Add\n2.Remove\n3.Moveup\n4.Search\n5.Exit\n"))
        match c:
            case 1:
                name=input("Enter your name ")
                condition=input("Enter your Condition\n1.High\n2.Moderate\n3.Low\n")
                if condition.isdigit():
                    print("You should enter string not number ")
                else:    
                    disease=input("Enter you problem :\n")
                    l.add(name.lower().strip(),condition.lower().strip(),disease)
                    l.display()

            case 2:
                name=input("Enter name to remove ")
                l.remove(name.lower().strip())   
                l.display()  
            case 3:
                name=input("Enter your name ")
                l.moveup(name.lower().strip())           
                l.display()
            case 4:
                name=input("Enter your name ")
                l.search(name.lower().strip())           
                l.display()
            case 5:
                print("Exiting.............")
                break
             