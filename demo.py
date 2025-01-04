'''
a= 12
b=13
sum = a+b
print(sum)
name= 'Gautam Jha'
age= 12
city='jaipur'
print(name ,age , city)

#simple text output
print("Hello Gautam Jha")

print("Jha")

#Printing Multiple Line
#name = "Kanak LLp"
#age = 15
print("Name:",name, "Age:",age)

#Seperation
#Custom Seperation(sep)
print("Apple","Banana","Milk", sep=", ")

#Custon end Character (end)
print("Hello", end=" ")
print("world,kanak LLP!")

#String formatting (F- strings)
print(f"Age: {age}, Name: {name}")

#Print(age)

#print function
if __name__ == '__main__':
    n = int(input())
    
    # Print numbers consecutively without spaces
    for i in range(1, n + 1):
        print(i, end="")
    #Batch Apex
public class ContactBatch implements Database.Batchable<sObject>{
    public Database.QueryLocator start(Database.BatchableContext BC){
        return Database.getQueryLocator('Select id from Contact');
    }
    Public void execute(database.BatchableContext BC, List<contact> scope){
        for(Contact con : scope){
            con.Title = 'JHA'; 
          }
             Update scope;   
   }
    public void finish(database.BatchableContext BC){
         system.debug('Contacts Updated Successfully');    
    }
}

'''
public class ContactBatch implements Database.Batchable<sObject>{
    public Database.QueryLocator start(Database.BatchableContext BC){
        return Database.getQueryLocator('Select id from Contact');
    }
    Public void execute(database.BatchableContext BC, List<contact> scope){
        for(Contact con : scope){
            con.Title = 'JHA'; 
            con.Email = 'Jhagautam62@gmail.com';
          }
             Update scope;   
   }
    public void finish(database.BatchableContext BC){
         system.debug('Contacts Updated Successfully');    
    }
}
