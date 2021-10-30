# Virtual-AI-assistant
This repository contains my Bachelor's degree final year project

In this project we create a virtual assistant that can hear, think and respond to the user. User can ask general queries (in natural language) about various flights and the virtual assitant will respond appropriately using its knowledge (the database). It also generates the face emoji based animation with voice as an output.

The chatbot is currently trained for atis_flight dataset and hence it can only answer the queries for flights.

Follow How to run section to see the bot in action. It is super easy to run and fun to talk to it. The code is fully tested in google colab.

## Sample output
https://user-images.githubusercontent.com/37477321/139559197-7170118d-a3b1-4ac0-ad50-c83beed70a78.mp4

## Queries this bot can answer
This bot was made to help passengers book flights. It has it's own database that consists cities, flights and other related details for India. We will release the full structure of database soon. But, to test the bot you can ask it the following queries -

Database - 
Cities : Pune, Mumbai, Nagpur
Flight IDs: 6, 9, 10, 11
Flight companies: Air India, Go Air, King Fisher, Indigo
Classes: Business, Economy

Type 1 - hello show me flights from <city> to <city>.

Type 2 - hello can you give me minimum fare for flights from <city> to <city> in the <class> class

Type 3 - hello can you give me <flight company> flights from <city> to <city>

Type 4 - show me details for flight with id <flight id>

Type 6 - hello how many seats are available for flights from <city> to <city>

Currently the bot is trained only on these 6 typed of queries and its variations. You can ask variations of the queries in natural language. Try to see in what scenarios the bot is not able to undertand you.

## How to run
Just run the 'Virtual_assistant_notebook.ipynb' notebook in the main folder of this repository in Colab.

1. Start executing all the cells one by one.

2. When you execute the last cell, it will automatically start recording your voice. When this happens you will see a button that says 'Recording' and you have to say your query at this point.

3. After you are done saying your query, you need to click the button to stop the recording.

4. The bot will show the results of your query and generate an animated face video with it's voice.

## System Architecture
<img src='assets/sys_arch.png'>
  
## Thanks to -
  
1. NVIDIA Flowtron - https://github.com/NVIDIA/flowtron
2. Joint BERT - https://github.com/monologg/JointBERT
3. Speech Recognition python library - https://github.com/Uberi/speech_recognition
  
Virtual-AI-assistant was made possible because of the repositories mentioned above!
