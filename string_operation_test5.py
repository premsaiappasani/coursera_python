#The group_list function accepts a group name and a list of members, and returns a string with the format: group_name: member1, member2, … 
#For example, group_list("g", ["a","b","c"]) returns "g: a, b, c".
#Fill in the gaps in this function to do that.


def group_list(group, users):
  i=0
  members= '"' + group + ':'
  for user in users:
    members += ' ' + user 
    i+=1
    if i==len(users):
      return members+'"'
    members+=","
  return members + '"'
  

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"




def group_list(group, users):
  arr=""
  for user in users:
    arr= ", ".join(users)
  members = ''.join(['"',group,": ",arr,'"'])
  return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"
