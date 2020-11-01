# beta24_LazyLeaves

## Simpli-Map :
It is a Offline SMS service which helps in finding the routes from source to destination entered by the user. The user can search for the route by sending his current location and destination location. After querying via sms the directions will be received by the user via SMS.  


## TECH STACK

Python  
Nltk  
Natural Language Processing (NLP)  
Twilio-SMS-API  
OpenMapQuest Api  
OpenStreet Api  
Intellexer Api  
AWS lambda  


## WORK FLOW

First we are creating a messaging service using Twilio.   
The received message is then pre-processed to remove any unwanted symbols and words.  
The query is then extracted from the pre-processed data .  
The source and destination locations are then identified from the query.  
The longitudes and latitudes of source and destination are then fetched using Open Street Map Api.  
After this the directions are fetched using the Mapquest Api require as longitude and latitude as parameters.  
The fetched directions are then sent to the user using Twilio and AWS lambda.  
An additional feature for searching nearby places has also been implemented.  



## SAMPLE QUERY TYPES FOR GOING FROM POINT A TO POINT B  

from indore to bhopal  
Take me to goa from mumbai  
take me from howrah bridge to dumdum kolkata  
I wish to go to bhopal from indore  
from chennai to banglore  
Show me directions from Mata Mandir bhopal to palasia Indore  
Take me from palasia indore to bhopal  
get directions from Victoria Memorial Kolkata to Howrah Bridge  
Route me to Howrah Bridge from Lake town kolkata  
get directions from andheri mumbai to bandra mumbai  
show me the directions from palasia indore to rajwada indore  
travel from Nariman Point Mumbai to Bandra East Mumbai  
I am currently standing on Bandra Mumbai I want to reach Taj Hotel Mumbai  

  

## SAMPLE QUERY TYPES FOR NEARBY PLACES SEARCH  
  
restaurants near palasia indore  
Search for Schools near Tatibandh Raipur  
cafes near manit bhopal  
banks near Bandra Mumbai  
restaurants near mata mandir bhopal  
restaurants near manit bhopal  
Search mall around palasia indore  
Look for popular cafes near Nariman point mumbai  
Is there any good college around Howrah Bridge kolkata  
Doctors near Victoria Memorial Kolkata  
what are the banks near mata mandir bhopal  
Cafes near Taj Hotel mumbai  
Post offices close to Howrah Bridge  
Airport close to palasia indore  
show banks near mata mandir  
show all the Police station near MANIT bhopal  
banks near Mall Road, Shimla  
police station near db city bhopal  
banks near The Ridge, Shimla  
banks near Calangute Beach goa  
cafes near Fort Aguada goa  



## Some Common Locations   

mata mandir bhopal  
dumdum kolkata  
db city bhopal  
palasia indore  
taj hotel mumbai  
bandra mumbai   
goregaon mumbai  
Nariman point mumbai  
andheri mumbai  
juhu beach mumbai   
rajwada indore  
connaught place delhi  
Chandni Chowk delhi  
Howrah Bridge kolkata  
Victoria Memorial Kolkata  
Mall Road, Shimla  
The Ridge, Shimla  
Calangute Beach goa  
Fort Aguada goa  
