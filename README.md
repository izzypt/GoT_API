# GoT_API

### Exercise Description

As we are fans of Game of Thrones, we would like to have an application that can
show the great houses of the Seven Kingdoms with a few members.
The application will have two distinct entities: houses and members. Each house
represents a family: Stark, Lannister, Baratheon, etc) and members must belong to a house -
Ned Stark belongs to House Stark.

### Functionality:

The API must include CRUD (Create Remove Update Delete) operations for both entities
with validation - you can’t leave members without a house!
When fetching a house, the API should also be able to return all its members and when
fetching a member the API should return the data of the house (s)he belongs to.

## FrontEnd Result

<div align="left">
      <a href="https://www.youtube.com/watch?v=e4pwoi3x2vY">
         <img src="https://img.youtube.com/vi/e4pwoi3x2vY/0.jpg" style="width:100%;">
      </a>
</div>

## Backend GraphQL API  

<div align="left">
      <a href="https://www.youtube.com/watch?v=HusM7zZIu3Y">
         <img src="https://img.youtube.com/vi/HusM7zZIu3Y/0.jpg" style="width:100%;">
      </a>
</div>


## Starting backend
  1 - Create virtual environment to keep our dependeciens isolated and avoid packages conflicts
  
    python3 -m venv venv
    
  2 - activate virtual env 
    
     ubuntu/Mac -> "source venv/bin/activate"
     Win -> ".\venv\Scripts\activate"
     
  3 - Install DJango 
  
     $ python -m pip install Django
     
  4 - Install Graphene
  
    $ pip install graphene-django
    
  5 - Install corsheaders to request from  different domain than the one that served the web page
  
    pip install django-cors-headers
    
  5 - Output a file to save/track our current packages
  
    $ pip freeze > requirements.txt
   Later we can install the same packages from it using : pip install -r requirements.txt
    
