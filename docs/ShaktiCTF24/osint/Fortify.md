# Fortify

**Description**:  

Greetings, Mission Officer. We have received a report stating that a group of anti-nationals is planning to hold a meetig at a fort in Maharashtra. We have identified three possible locations for the meeting:

```cmake
Location 1: Torna Fort
location 2: Malhargad killa
location 3: Vairatgad Fort
```

However, our officers were unable to find any suspicious activity at these sites. We also know that the group leader is currently in Osaka, Japan and has set the meeting time for 8:00 pm.
But the fort is closed at the time. Now its upto you to find the fourth fort and the right time for the meeting.
Flag format, if the fort is Malhargad killa and the time is 1.30 pm: vidyutctf{malhargad_killa_13:30}

**Author:  [Ath3n1x](https://twitter.com/Ath3n1x)**

**Solution**: 
We are provided with 3 fort locations in Maharashtra. [`Google my maps`](https://www.google.com/maps/d/u/0/) is a tool that I swear by when it comes to map related OSINT challenges. 

1. Create a new map in my maps. First mark the locations of the 3 forts with ``(add marker)`` tool. Then you can connect them using ``(Draw a line)`` tool.
2. 

![image](https://github.com/Ath3n1x/CTF-Write-ups/blob/master/docs/ShaktiCTF24/osint/uploads/forts.png?raw=true)



Now search for `forts in maharashtra`.

![image](https://github.com/Ath3n1x/CTF-Write-ups/blob/master/docs/ShaktiCTF24/osint/uploads/forts_mapped.png?raw=true)


**Inside the triangle**, you can see one fort clearly: `Purandar fort`

2. The time specified is 8 pm in Japan time. It should be converted to 4.30 pm IST as the forts are in India.

3. At last, convert the time to 24 hour format and assemble the flag as: `{purandar_fort_16:30}`

Flag: `shaktictf{purandar_fort_16:30}` 
