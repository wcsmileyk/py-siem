# Build a SIEM from python

## Steps we'll need:

### Syslog Listener. Maybe use sockets. Maybe there's a library?
- Maybe a sockerserver. Seems easiest.
- Library could work if one exists. Can't find one yet
### Logs. And PCAP. Oh. Yeah. Probably
- We'll work this out
### Database? Maybe? Flat file? Somewhere to store and work with logs and events. 
- Probably NOSQL. Right? I dunno. Ugh.
- Why not just start with a flat file? Cause even if it'd work a SIEM can't just be grepping files. That'd defeat the exercise
- Maybe pandas dataframes? Oooooooo, that'll get the data nerds running. 
- So definitely a database. In real world it needs to be fast. Here. Maybe not?
### PCAP analyzer
- We'll get there. I promise
### Event Analyzer
- Leverage the power of regex I think. Maybe pandas? More dataframse! Datanerds will love this talk!
- Need to be able to do this relatively qiucky. Get the known identity data out. Get known event codes out. Move on
### Rules to trigger alerts
- Uh.
- Probably need a data analytics tool for this. Guess I'm going to need to learn that.
### Notification system when bad stuff is happening
- Easy. smtplib. Done. If it has a flask front-end (if it has a flask font end: bigger audience. So yeah. Flask front end) then flask-mail or something like that
### Context! Intel feeds, black lists of some sort. Bad info.
- Oh cool. I know this stuff. Pull down some intel feeds from their APIs, seperate the indicators and throw them in some sort of data store. (Oh man, I'm going to need a database. Crap.)
- Cofense Sales pitch? I won't be that blatant. Well. Maybe. Okay I might be that blatant.
