# Log Parser & Analyzer

I started learning Python around **3 weeks ago**, and I wanted to test myself by actually trying to build something on my own. I decided to make a Log Parser & Analyzer, first researching how server logs are structured and what kind of information I could extract from them, and then trying to build it myself.

This has honestly been one of the most enjoyable things I've worked on so far. I had to figure things out as I went, test different ideas, find bugs and then debug them. It also helped me realise that learning to code isn't just about getting something working, but understanding why it works and how I can improve it.

### What I learned

* Python functions
* Regular expressions
* File handling
* `pathlib`
* Lists and dictionaries
* `collections.Counter`
* Loops and conditionals
* Error handling
* Input validation
* Debugging
* Building a command-line menu
* Organising a larger program into separate functions
* Using the same parsed data for different parts of the program
* Breaking a bigger problem into smaller parts

One thing I tried to follow throughout the project was:

> **ONE job → ONE function**

---

## What I built

For my first version, I built a command-line tool that reads a log file and extracts information from it using **Python, regex, file handling, pathlib and Counter**.

### The program can:

* Parse server log files using regular expressions
* Extract IP addresses
* Extract timestamps
* Extract HTTP requests
* Extract status codes
* Extract response/data sizes
* Count successful requests (`2xx` and `3xx`)
* Count unsuccessful/error requests (`4xx` and `5xx`)
* Count requests by IP address
* Count occurrences of each status code
* Detect invalid log lines
* Display different metrics through an interactive menu
* Display all metrics together
* Save analysis results to a text file
* View previously generated analysis files

I also spent a lot of time testing and debugging the program as I built it, which was probably just as useful as writing the code itself.

---

## What's next?

This is only my **first draft and the beginning of the project**, so there is still a lot I want to improve.

One of the biggest things I want to do is make the project **more visual** instead of everything being displayed in the terminal.

### Things I'd like to add:

* A pop-up GUI instead of only using the terminal
* **Tkinter** or another GUI library
* Graphs and charts using **Matplotlib**
* Traffic by hour
* Peak/busiest hour analysis
* Visual status-code breakdowns
* Visual request/traffic statistics
* Filtering by IP, status code or time
* More detailed security alerts for unusual IP activity
* Better report formatting
* More robust log parsing
* Automated testing
* Possibly exporting results in different formats
* More features as I learn more Python

There are probably plenty of other things I haven't even thought of yet, so I'll keep adding to it as I learn.

I'm not expecting this first version to be perfect, and that's not really the point. I wanted to take what I've learned so far, build something myself and see where I could get with it.

I've really enjoyed making this and I'm looking forward to seeing how different this project looks after I've learned more Python. **This is only version 1. **

If anyone more experienced sees something I could improve or something I've done wrong, please feel free to comment and let me know. I'm still learning, so any advice or constructive feedback is appreciated.

**Thanks for checking it out and stay tuned for the improvements!**
