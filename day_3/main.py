with open ("rucksack.txt", "r") as data: 
    rucksack = [line.rstrip('\n') for line in data]


def reorganization(data):
  


  # a - z 1-26;  97 to 122
  # A - Z 27-52  65 to 90

  sum_of_the_priorities = 0
    
  for compartments in data:
    first_compartment = compartments[0:len(compartments)//2]
    second_compartment = compartments[len(compartments)//2:]
    
    intersection = set(first_compartment).intersection(second_compartment).pop()
    
        
    if intersection.isupper():
      sum_of_the_priorities += ord(intersection) - 38
    else:
      sum_of_the_priorities += ord(intersection) - 96

                  
  return f"this is solution to part one: {sum_of_the_priorities}"
      
    
def part_two(data):
  sum_of_the_priorities = 0
  for i in range(0, len(data), 3):
    intersection = set(data[i]).intersection(data[i+1], data[i+2]).pop()
    
    if intersection.isupper():
      sum_of_the_priorities += ord(intersection) - 38
    else:
      sum_of_the_priorities += ord(intersection) - 96
      
  return f"this si solution to part two {sum_of_the_priorities}"
  
print(reorganization(rucksack))
print(part_two(rucksack))