An OpenAI function calling agent (as opposed to a ReAct agent) using the following: 
Backend: FastAPI/SQL Model.
Frontent: Jina2, Bootstrap, and fetch().
Security: Oauth2 with password flow using JWT bearer tokens and a remote MariaDB user identity database hosted on a DigitalOcean VPS.


This is a work in progress and will have multiple updates on a weekly basis.
I'm trying to get as "old school"/legacy as possible, so I'm sticking with gpt-3.5-turbo and the completions API (no need for any framework overhead, etc., until absolutely necessary).

Todo list for this week:

1. Get rid of the weather tool, add a search engine tool, and add a few other interesting tools.
2. Do some error handling to address when the LLM decides to make a function call with the wrong arguments.
3. Get all the code out of main.py and organise it.
4. Deploy to AWS lambda using Podman instead of a Zip file.
