# Analytics Alternatives

This project orginated based on different events in January 2022:
- The Austrian DAP ruled out Google Analytics usage because IP address data can be sent to their us-based servers
- This time it hit the social networks and fired up a lot of discussions
- Legal people commented on it and they all just said: Use Matomo
- Which drove us tracking engineers crazy, since we know that you need to choose your analytics based on multiple needs - privacy, server location are important aspects but not the only ones
- So we need a directory of all different tracking & analytics solutions that provide extensive context about the solutions and not just a name and a link

## Goals
This directory should help everyone who is looking for a tracking and analytics solution: 
- by presenting an extensive list of all possible services & projects
- giving deep context about these services to make it easier to understand if they fit the use case you have in mind
- give feedback about the privacy related setup (server location, type of server, company country, cookie usage)
- give heavy user insights about the services (the good, the bad, the ugly)

## Contribution
Orginally this was just intended as a blog post, but it became clear that this is bigger than just a post. There are too many services, too many details and too many good people with extensive knowledge around.

So an open source directory is a much better way.

Everyone who loves to contribute is welcome here.

At the moment there is no process and guidelines for the contribution. We will work on that.
Technically it's easy: 
- write an issue if spot something and you can't fix it
- fix or extend something and create a pull request

Of course we love to have vendors contributing and we might have discussion in the future about some inputs (which we hope is a good thing).

## The architecture
Still in early early stage. Currently my idea:
- have a folder for services
- use one yaml for a service

An additional layer will be the presentation layer. I would start with a simple NextJS application. Therefore we can create a script that renders a markdown file from the yaml file.

So the yaml files are basically our repo based database and the markdown files the CRM. The separation of both might become benefitial if we want to change how the data is presented.

## The data structure
Also early early stage. In the src folder you find the current version of a sample yaml file. We can work with versions here, so we have an idea which service data is described based on which version (and maybe needs an update).