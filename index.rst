.. Spotify Player documentation master file, created by
   sphinx-quickstart on Mon Jan 02 21:53:28 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Spotify Player's documentation!
==========================================

A Smart Spotify Player that makes playing songs on Spotify easier than ever.

This application understands the voice commands using Microsoft Speech API and the brain of Microsoft LUIS to paraphrase the voice commands as per the Aritst, Song, Playlist and Album. After understanding which song to play, it goes ahead and uses the Spotify Web API to search for the url of that specific song and loads it up on the web browser. 

Say commands like :   
  
.. :    
   "Play the song everglow by Coldplay from the album a head full of dreams"
   
   "Play songs by the artist Nickelback"
   
   "Play songs from the album Pound Syndrome"
   
or simply say 

.. :"Play hotel california"

Get things rolling with : 

.. code-block:: bash
    
    pip install git+git://github.com/kishorevasan/SpotifyPlayer.git

Just one python package required..

.. code-block:: python
    
    pip install SpeechRecognition
    
Now, you can simply write the command given below on your terminal and start playing songs.

.. code-block:: python
   
   python speech.pyc
   
Happy Listening! 

.. toctree::
   :maxdepth: 1
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
