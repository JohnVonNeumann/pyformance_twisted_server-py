# Pyformance Twisted Server

### Tutorial Used
> http://techtraits.com/programming/monitoring/python/2013/02/17/Monitoring-python-servers-with-pyformance-and-graphite.html

* This repo is an attempt at understanding how twisted works in conjunction with the python port of Code Hale's Metrics library. I have an interest in quantifying problems using code, understanding real data to do with applications and architecture, this repo is a voyage into that space.

* This is proving to be a neat little project, so I'm pretty sure I learnt the differences between synchronous and asynchronous a while ago but now that I have some exposure to both, I get it. So flask as a perfect example, is synchronous, when a request or call is sent, it allocates resources to qualify a response then waits to reply, think of a waitress who takes your breakfast order then waits at the window for the meal, before serving other customers. This is contrasted vs Twisted, which is asynchronous, the waitress takes your order, then comes back with the first decent response, whether that's "your order is underway", "we don't have chicken left" or "here is your meal".

* Removed the public pyformance libraries in order to use the forked version created by the guy who wrote the tutorial, he made some small changes in order to get it to push logs to a hosted graphite server.