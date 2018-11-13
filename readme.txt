Model which conatins tables and keys


Table - MainCategory
id - Integer PK
storeid-  Integer FK
name - Char
description - Text
image - Text

Table - SubCategory
id - Integer
storeid-  Integer FK
name - Char
description - Text
maincategoryid -  Integer FK

Table - Store 

id - Interger (PK)
name - Char
description - Text
address - Text
area - Char
city - Char 
areaPostalCode - IntergerField
avgRating- TextField
avgRatingString - TextField
slug - - TextField
is_open - BooleanField
image - Text 
pickup_point - Char 
lat - Decimal 
long - Decimal 


Table- Items
id - IntergerField (PK)
name - CharField
description - TextField
Price - IntergerField
ImageUrl - CharField
Description -CharField
Diet Type - IntergerField Flag(1 for veg, 0 for non veg)
Recommended -IntergerField Flag(1 for recommended, 0 for nonrecommended)
Available -IntergerField Flag(1 for available, 0 for not available stock field from json)
nextAvailableAtMessage -CharField
displayOrder -IntergerField Flag(1 for available, 0 for not available display field from json)
price - CharField




