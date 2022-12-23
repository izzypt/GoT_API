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
