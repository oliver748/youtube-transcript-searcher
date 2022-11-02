# What does it do?

Finds specific sentences or words said in YouTube videos using scrapetube, youtube_transcript_api, and YouTube's own automatic subtitle generator.

# How does it work?

This works by first scraping all the youtube links from the channels the user has inputted themself, and then scraping the transcript from all of the youtube videos there are available - finally it checks for the specific content in all the transcript data available.

# Instructions

1. Install the pip libraries using 'pip install -r requirements.txt'
2. Put in the link to the youtube channels you want to check in channels.txt
3. Run main.py and fill in the details required
4. Sit back, have a cup of coffee, and wait.

If it doesn't work it's either because no subtitles are available or your connection isn't working properly.
