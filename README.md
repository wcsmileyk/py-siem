# Build a SIEM from python

## Steps we'll need:

### Syslog Listener. Maybe use sockets. Maybe there's a library?
- Maybe a sockerserver. Seems easiest.
    - Starting here. Forked a good script and it was done. Boom.
- Library could work if one exists. Can't find one yet
- Meh not super important yet. But yeah sure
### Logs. And PCAP. Oh. Yeah. Probably
- Start with t-pot basic honeypot, but better stuff later
### Database? Maybe? Flat file? Somewhere to store and work with logs and events. 
- ELK seems to be most reasonable. Maybe do a simple nosql db
### PCAP analyzer
- ELK to start
### Event Analyzer
- ELK to start
- Jupyter notebook
### Rules to trigger alerts
- Uh.
- Probably need a data analytics tool for this. Guess I'm going to need to learn that.
### Notification system when bad stuff is happening
- Easy. smtplib. Done. If it has a flask front-end (if it has a flask font end: bigger audience. So yeah. Flask front end) then flask-mail or something like that
### Context! Intel feeds, black lists of some sort. Bad info.
- Oh cool. I know this stuff. Pull down some intel feeds from their APIs, seperate the indicators and throw them in some sort of data store. (Oh man, I'm going to need a database. Crap.)
- Cofense Sales pitch? I won't be that blatant. Well. Maybe. Okay I might be that blatant.
