# taskBoard
Task board application implementing backend web design
# Task Scheme

## Project
Project Class Documentation
This document describes the Project model.  

- ProjectId (Guid): A unique identifier for the project. This property is of type Guid and is always public and accessible.  
- Tasks (ICollection<Tasks>): A collection of Task objects associated with the project. This property allows for null values and should be accessed through the get method only.  
- LastModified (DateTime): The date and time the project was last modified. This property is of type DateTime and is public and accessible.   
- DateCreated (DateOnly): The date the project was created. This property is of type DateOnly and is public and accessible.   
- AuthorId (Guid): The unique identifier of the user who created the project. This property is of type Guid and is public and accessible. 
```C#
 public class Project
    {
        public Guid ProjectId { get; set; }
        [AllowNull]
        public ICollection<Tasks> Tasks { get; set; }
        public DateTime LastModified { get; set; }
        public DateOnly DateCreated { get; set; }
        public Guid AuthorId { get; set; }
    }
```

## Tasks
Tasks model represents a task within a project.

- Status (Status): The current status of the task. This property is of type Status and is public and accessible. The specific values within the Status enum are likely defined elsewhere in the system and could represent different stages a task can be in, such as "Proposed," "In Progress," "Completed," etc.   
- Title (string): The title of the task. This property is a string and is public and accessible.  
- Description (string): A detailed description of the task. This property is a string and is public and accessible.   
- DateCreated (DateOnly): The date the task was created. This property is of type DateOnly and is public and accessible.  
- LastModified (DateTime): The date and time the task was last modified. This property is of type DateTime and is public and accessible.  
- AssigneeId (Guid): The unique identifier of the user assigned to the task. This property is of type Guid and is public and accessible.
- TaskId (Guid): The unique identifier for the task. This property is of type Guid and is always public and accessible.
```C#
 public class Tasks
    {
        public Status Status { get; set; }
        public string Title { get; set; }
        public string Description { get; set; }
        public DateOnly DateCreated { get; set; }
        public DateTime LastModified { get; set; }
        public Guid AssigneeId { get; set; }
        public Guid TaskId { get;set; }
    }
```

## Status
The status enum represents thet state of a particular task within a project. As of right now we support 3 states: 
- Proposed-A proposed task
- InProgress- The current Tasks is in progress 
- Complted- The task was fully completed
```C#
    public enum Status
    {
       Proposed=0,
       InProgress=1,
       Completed=2
    }
```
# Allowed Operations
- Users allowed to create and modify projects. There is no limit to how many projects a user can create.
- Users are not allowed to delete other users' projects, but they are allowed to delete their own projects.
- Users are allowed to create and modify any tasks within a project.
- Users are allowed to filter tasks based on specific keywords.
- There is no plan to support project filtering
