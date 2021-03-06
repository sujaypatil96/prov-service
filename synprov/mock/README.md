### This folder contain script to generate sample data according to the following rules:

## Script
_1. Create sets of entity references:_
```    
for type in entity types:
# eventually we might want to create 100s if not 100s of references;
# I started working with ~5 so I can more easily check what's happening
create and name <num> references
```
_2. Create agent/user pool:_
```
create and name <num> agents
```
_3. Create activities:_
```
while n < <desired number of activities>:
  # depending on the cardinality rules for each activity type, this function
  # will randomly select references from the sets defined above; the 
  # function will also assign the activity a unique ID and format the result
  # as a nested list (which can be easily converted to JSON)
  create_activity(type = <activity type>, 
                  used = <allowed 'used' refs>, 
                  generated = <allowed 'generated' refs>, 
                  agents = <agents pool>)
```       
_4. Create 'ASSOCIATED WITH' relationship:_
```
for each Activity create one relationship:
    Activity -> :WASASSOCIATEDWITH -> Agent
```       
_5. Create 'GENERATED BY' relationship:_
```
for each Reference create one relationship:
    Reference -> :WASGENERATEDBY -> Activity
```       
_6. Create 'USED' relationship:_
```
for each Activity create one relationship:
    Activity -> :USED -> Reference
```       
_7. Create 'ATTRIBUTED TO' relationship:_
```
for each Reference create one relationship:
    Reference -> :ATTRIBUTEDTO -> Agent
```       

           
**Note:** 
- the logic for sample size specified here shouldn't be hardcoded, but either some sort of map or function to lookup numbers based on activity type:

- Output is written directly into console with JSON format.

## Usage
To run the program you need to type in the command line: 
```
>> python main.py <#agents> <#references> <#activities>

# eg. to generate records for 5 agents, 10 references and 30 activities
>> python main.py 5 10 30
```
Program will generate output in json structures for Agents (5 records), References (10 records) and Activities (30 records) and all types of relationsheeps between those entities.

## Program parameters and dictionaries
```
#numer of agents generated by script
#input parameter for the program
NUMAGENTS = 5 // default value

#numer of references generated by script
#input parameter for the program
NUMREFERENCES = 10 // default value

#numer of activities generated by script
#input parameter for the program
NUMACTIVITIES = 30 // default value

#array of Agent roles
#can be changed in the **dict.py** file
agtRoles = ["Role_1", "Role_2", "Role_3", "Role_4", "Role_5"]

#array of Reference roles
#can be changed in the **dict** file
refRoles = ["data", "tool", "state", "message", "report"]

#array of Activities types
#can be changed in the **dict.py** file
actNames = ["Tool session", "Mention", "Report generation"] 

# list of all available relation types
#can be changed in the **dict.py** file
RelationTypes = ["WASASSOCIATEDWITH", "WASGENERATEDBY", "USED", "WASATTRIBUTEDTO"]
``` 

## Sample output
```
# Agent Records
...
{"agtId": "1cba2d84-91b9-11e9-8943-48a4726d43f3", "name": "User_1", ":LABEL": "Agent"}
{"agtId": "1cba2d85-91b9-11e9-aed5-48a4726d43f3", "name": "User_2", ":LABEL": "Agent"}
{"agtId": "1cba2d86-91b9-11e9-829c-48a4726d43f3", "name": "User_3", ":LABEL": "Agent"}
...
```

```
# Reference Records
...
{"refId": "1cb9df36-91b9-11e9-91b2-48a4726d43f3", "target_id": "TargetID_1", "target_version_id": "1.0", "name": "Reference_1", ":LABEL": "Reference"}
{"refId": "1cb9df37-91b9-11e9-bf04-48a4726d43f3", "target_id": "TargetID_2", "target_version_id": "1.0", "name": "Reference_2", ":LABEL": "Reference"}
{"refId": "1cb9df38-91b9-11e9-b156-48a4726d43f3", "target_id": "TargetID_3", "target_version_id": "1.0", "name": "Reference_3", ":LABEL": "Reference"}
...
```

```
# Activity Records
...
{"actId": "1cba2d89-91b9-11e9-820f-48a4726d43f3", "name": "Activity_1", "class": "Tool session", ":LABEL": "Activity"}
{"actId": "1cba2d8a-91b9-11e9-9c12-48a4726d43f3", "name": "Activity_2", "class": "Report generation", ":LABEL": "Activity"}
{"actId": "1cba2d8b-91b9-11e9-9bf2-48a4726d43f3", "name": "Activity_3", "class": "Mention", ":LABEL": "Activity"}
...
```

```
# Relationship 'WASASSOCIATEDWITH' Records
...
{":START_ID": "1cba2d89-91b9-11e9-820f-48a4726d43f3", "roles": "Role_1", ":END_ID": "1cba2d85-91b9-11e9-aed5-48a4726d43f3", ":TYPE": "WASASSOCIATEDWITH"}
{":START_ID": "1cba2d8a-91b9-11e9-9c12-48a4726d43f3", "roles": "Role_1", ":END_ID": "1cba2d88-91b9-11e9-a065-48a4726d43f3", ":TYPE": "WASASSOCIATEDWITH"}
{":START_ID": "1cba2d8b-91b9-11e9-9bf2-48a4726d43f3", "roles": "Role_3", ":END_ID": "1cba2d84-91b9-11e9-8943-48a4726d43f3", ":TYPE": "WASASSOCIATEDWITH"}
...
```

```
# Relationship 'WASGENERATEDBY' Records
...
{":START_ID": "1cb9df36-91b9-11e9-91b2-48a4726d43f3", "roles": "state", ":END_ID": "1cba52f7-91b9-11e9-a0cb-48a4726d43f3", ":TYPE": "WASGENERATEDBY"}
{":START_ID": "1cb9df37-91b9-11e9-bf04-48a4726d43f3", "roles": "tool", ":END_ID": "1cba52e5-91b9-11e9-ba02-48a4726d43f3", ":TYPE": "WASGENERATEDBY"}
{":START_ID": "1cb9df38-91b9-11e9-b156-48a4726d43f3", "roles": "tool", ":END_ID": "1cba52f5-91b9-11e9-a1ea-48a4726d43f3", ":TYPE": "WASGENERATEDBY"}
...
```

```
# Relationship 'USED' Records
...
{":START_ID": "1cba52e5-91b9-11e9-ba02-48a4726d43f3", "roles": "state", ":END_ID": "1cb9df37-91b9-11e9-bf04-48a4726d43f3", ":TYPE": "USED"}
{":START_ID": "1cba52e6-91b9-11e9-95d5-48a4726d43f3", "roles": "report", ":END_ID": "1cba2d82-91b9-11e9-b12c-48a4726d43f3", ":TYPE": "USED"}
{":START_ID": "1cba52e7-91b9-11e9-a1aa-48a4726d43f3", "roles": "message", ":END_ID": "1cba2d81-91b9-11e9-88f4-48a4726d43f3", ":TYPE": "USED"}
...
```

```
# Relationship 'WASATTRIBUTEDTO' Records
...
{":START_ID": "1cb9df36-91b9-11e9-91b2-48a4726d43f3", "roles": "Role_1;state", ":END_ID": "1cba2d84-91b9-11e9-8943-48a4726d43f3", ":TYPE": "WASATTRIBUTEDTO"}
{":START_ID": "1cb9df37-91b9-11e9-bf04-48a4726d43f3", "roles": "Role_1;report", ":END_ID": "1cba2d87-91b9-11e9-b1d7-48a4726d43f3", ":TYPE": "WASATTRIBUTEDTO"}
{":START_ID": "1cb9df38-91b9-11e9-b156-48a4726d43f3", "roles": "Role_5;state", ":END_ID": "1cba2d85-91b9-11e9-aed5-48a4726d43f3", ":TYPE": "WASATTRIBUTEDTO"}
...
```
